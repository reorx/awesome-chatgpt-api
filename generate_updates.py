import os
import time
import re
import shlex
import datetime
import subprocess
import logging
from collections import OrderedDict
from ai import ChatSession


lg = logging.getLogger(__name__)

posts_dir = 'site/content/posts'


def main():
    logging.basicConfig(level=logging.INFO)

    session = ChatSession(
        os.environ.get('OPENAI_API_BASE_URL', 'https://api.openai.com/v1/'),
        os.environ['OPENAI_API_KEY'],
        params={
            'temperature': 0.7,
        }
    )

    rc, out, err = run_cmd('git log --pretty=format:"%h %ad %s" --date=short --first-parent', shlex_reformat=True, logger=lg)
    # print(out)

    date_hashs_map = OrderedDict()

    min_date = '2023-03-05'

    line_regex = re.compile(r'(?P<hash>\w+) (?P<date>\d{4}-\d{2}-\d{2}) (?P<msg>.*)')
    for line in out.strip().splitlines():
        rv = line_regex.match(line)
        hash, date = rv.group('hash'), rv.group('date')
        if date_str_greater_than(min_date, date):
            # ignore min_date greater than date
            continue

        hashs = date_hashs_map.setdefault(date, [])
        hashs.append(hash)

    print(date_hashs_map)

    posts_map = get_posts()
    for date, hashs in date_hashs_map.items():
        if date in posts_map:
            # ignore existing posts
            continue
        create_post(date, hashs, 'README.md', session)


def create_post(date, hashs, filename, session, create_cn=False):
    lg.info(f'create post for {date}')
    diff = get_diff_for_hashs(hashs, filename)
    if not diff:
        lg.info(f'no diff for {date}, skip create_post')
        return

    print('diff:\n', diff)
    post_dir = os.path.join(posts_dir, date)
    ensure_dir(post_dir)

#     generator_prompt = """\
# Write a changelog based on the following diff. organize the items in markdown list, each item starts with a markdown link, and a descripition is added below. The generated text starts with "Here's the projects added or updated today:"
# """
    generator_prompt = """\
Write a changelog based on the following diff. You should be aware that diff is a format to show the changes of two commits, only the lines starts with + are the added content. You should only extract the added content, organize the items in markdown list, each item starts with a markdown link, and a descripition is added below. The generated text starts with "Here's the projects added or updated today:"
"""
    generator_message = session.chat({
        'role': 'user',
        'content': f'{generator_prompt}\n{diff}',
    })
    content = generator_message['content'].strip()
    print('content:\n', content)

    summary_prompt = """Generate a summary within 25 words for the following blog content, using a tone of conscious and informative. Assuming the audiences know the context, ignore words about "using ChatGPT API".\n"""
    summary_message = session.chat({
        'role': 'user',
        'content': f'{summary_prompt}\n{content}',
    })
    summary = summary_message['content'].strip()

    post = f"""\
---
title: "Updates for {date}"
date: {date}
summary: "{summary}"
---
{content}
"""
    filename = f'{post_dir}/index.md'
    lg.info(f'write post {filename}')
    with open(filename, 'w') as f:
        f.write(post)

    if create_cn:
        translator_prompt = """\
    翻译下面的英文，生成中文的更新日志。
    """
        translator_message = session.chat({
            'role': 'user',
            'content': f'{translator_prompt}\n{content}',
        })
        content_cn = translator_message['content'].strip()
        summary_cn = session.chat({
            'role': 'user',
            'content': f'翻译下面的英文:\n{summary}',
        })['content'].strip()

        post_cn = f"""\
    ---
    title: "{date} 项目更新"
    date: {date}
    summary: {summary_cn}
    ---
    {content_cn}
"""
        filename_cn = f'{post_dir}/index.cn.md'
        lg.info(f'write post {filename_cn}')
        with open(filename_cn, 'w') as f:
            f.write(post_cn)


def get_diff_for_hashs(hashs, filename):
    # git diff 3b9a293..9d02879~1
    cmd = ['git', 'diff', '--minimal', '-U2', f'{hashs[-1]}~1..{hashs[0]}', '--', filename]
    rc, out, err = run_cmd(cmd, logger=lg)
    if rc != 0:
        raise RuntimeError(f'git diff failed: {err}')
    return out.strip()


def get_posts():
    posts = {}
    with os.scandir(posts_dir) as entries:
        for entry in entries:
            if entry.is_dir():
                posts[entry.name] = 1
    return posts


def date_str_greater_than(s0, s1, format='%Y-%m-%d'):
    d0 = datetime.datetime.strptime(s0, format)
    d1 = datetime.datetime.strptime(s1, format)
    return d0 > d1


def run_cmd(cmd, shlex_reformat=False, shell=False, logger=None, **kwargs):
    if shlex_reformat and shell:
        raise ValueError('shlex_reformat and shell are mutually exclusive')

    if shell:
        if not isinstance(cmd, str):
            raise ValueError('cmd must be str when shell=True')
        kwargs['shell'] = shell

    # reformat cmd
    if shlex_reformat:
        if isinstance(cmd, list):
            cmd_str = ' '.join(cmd)
        else:
            cmd_str = cmd
        cmd = shlex.split(cmd_str)

    if logger:
        logger.info('cmd: %s, %s', cmd, kwargs)

    extra_env = kwargs.pop('env', {})
    if extra_env:
        env = os.environ.copy()
        env.update(extra_env)
        kwargs['env'] = env

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
    out, err = p.communicate()
    out, err = out.decode(), err.decode()

    if logger:
        logger.debug('cmd=%s returncode=%s out=%s err=%s', cmd, p.returncode, out, err)
    return p.returncode, out, err


def ensure_dir(path):
    # lg.debug('ensure dir: {}'.format(path))
    if os.path.exists(path):
        if not os.path.isdir(path):
            raise IOError('ensure_dir: {} must be a directory'.format(path))
    else:
        lg.debug('mkdir %s', path)
        try:
            os.makedirs(path)
        except OSError as e:
            lg.info('ignore os.makedirs OSError: %s', e)


if __name__ == '__main__':
    main()

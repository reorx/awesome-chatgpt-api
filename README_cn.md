# Awesome ChatGPT API

基于 [ChatGPT API](https://platform.openai.com/docs/api-reference/chat)，且允许配置自己的 [API key](https://platform.openai.com/account/api-keys) 的工具和应用的精选列表。其中也包含一些[开发](#development)相关的项目和文章。

由 [![Twitter](https://img.shields.io/twitter/url.svg?label=%40novoreorx&style=social&url=https%3A%2F%2Ftwitter.com-novoreorx)](https://twitter.com/novoreorx) 收集整理，欢迎在 Twitter 或通过 PR 向我提交新的作品。


## 插件和扩展

- Chrome 扩展

    - [Glarity](https://glarity.app/)

        使用 ChatGPT API 生成 Google 搜索结果或 YouTube 视频的摘要。该扩展还支持 ChatGPT Webapp 的 API，无需配置即可使用。

    - [ChatGPT Sidebar](https://chatgpt-sidebar.com/)

        在任何网页中打开侧边栏，询问 ChatGPT 关于页面内容的任何事情，如解释、翻译、概括或重写。你可以自定义 prompts 以便更轻松地使用。该扩展还支持 ChatGPT Webapp 的 API，无需配置即可使用。

- [Obsidian](https://obsidian.md/) 插件

    - [Obsidian Text Generator Plugin](https://github.com/nhaouari/obsidian-textgenerator-plugin)

        在 Obsidian 中根据你的笔记生成想法、头条、摘要、大纲和整段文字。

- [Logseq](https://logseq.com/) 插件

    - [Logseq Plugin GPT3 OpenAI](https://github.com/briansunter/logseq-plugin-gpt3-openai)

        在 Logseq 中使用 ChatGPT 以及其他 AI 模型的插件。

- [Popclip](https://pilotmoon.com/popclip/) 扩展

    - [ChatGPT — PopClip Extensions](https://pilotmoon.com/popclip/extensions/page/ChatGPT)

        将所选文本发送到 ChatGPT 并将回复粘贴在后面。

    - [ChatGPT Proofreader extension for Popclip](https://reorx.com/makers-daily/003-chatgpt-proofreader-extension-popclip/)

        通过 ChatGPT API 对选中文本进行校对和润色，并将修改后的文本粘贴在后面。

    - [ChatGPT Grammar Check PopClip Extension](https://github.com/hirakujira/ChatGPT-Grammar-Check-PopClip-Extension)

        和 ChatGPT Proofreader extension 类似的扩展，提供可下载的安装包。

- [Drafts](https://getdrafts.com/) Actions

    - [ChatGPT Conversation | Drafts Directory](https://directory.getdrafts.com/a/2HJ)

        在 Drafts 笔记中与 ChatGPT 进行对话，新的回复将附加在末尾。支持定义和修改 system, assistant, user 角色的消息块。

- [Bob](https://bobtranslate.com/) 插件

    - [OpenAI Translator Bob Plugin](https://github.com/yetone/bob-plugin-openai-translator)

        基于 ChatGPT API 的文本翻译、文本润色、语法纠错 Bob 插件。另有一个专注于润色的衍生版本: [OpenAI Polisher Bob Plugin](https://github.com/yetone/bob-plugin-openai-polisher)。

- 苹果捷径

    - [ChatGPT Siri](https://github.com/Yue-Yang/ChatGPT-Siri)

        通过 Siri 启动「快捷指令」连接 ChatGPT API，让 Siri 变身 AI 聊天助手。你可以直接和 Siri 说出你的问题，Siri 会回答你。

    - [Siri Pro](https://www.icloud.com/shortcuts/6889d862918e479693be11fd9a0293b2)

        可随时唤起文字和语音两种输入方式，快速响应，支持多次问答，支持预设调教，跟人工智障说拜拜。 原推: [@DottChen](https://twitter.com/DottChen/status/1631309329684123650)

- [Keyboard Maestro](https://www.keyboardmaestro.com/) 宏

    - [Copy to Ask ChatGPT](https://blog.retompi.com/post/use-chatgpt-api/#keyboard-maestro)

        使用键盘快捷方式选择并复制文本以向 ChatGPT 提问。[下载链接](https://p15.p3.n0.cdn.getcloudapp.com/items/geuEZvwA/aeed10cb-a35d-404f-a17f-da1d46c9c9c7.kmmacros)。


## CLI

- [bilingual\_book\_maker](https://github.com/yihong0618/bilingual_book_maker)

    用于制作双语 epub 电子书的 Python 脚本。原推: [@yihong0618](https://twitter.com/yihong0618/status/1630948132564631552)

    Web UI [streamlit](https://goldengrape-bilingual-book-maker-streamlit-app-x7nhof.streamlit.app/)。原推: [tweet](https://twitter.com/goldengrape/status/1631549869306572800).
    
- [ChatGPT-for-Translation](https://github.com/Raychanan/ChatGPT-for-Translation)
    
    对文本文件进行翻译的 Python 脚本。同时提供双语翻译、多线程和自动处理过高的请求频率。

- [AI Commits](https://github.com/Nutlope/aicommits)

    一个用 ChatGPT API 生成 Git 提交消息的命令行工具。

- [xiaogpt](https://github.com/yihong0618/xiaogpt)

    通过小米音响的小爱同学与 ChatGPT 对话。

- [AI Vocabulary Builder](https://github.com/piglei/ai-vocabulary-builder)

    一个利用了 AI 技术的智能生词本工具，可以帮你快速构建起自己的生词库，学习起来事半功倍。

- [cz-git](https://github.com/Zhengqbbb/cz-git)

    一个 Commitizen 适配器与命令行工具使用 OpenAI API 生成 Git 约定式提交格式提交消息。 [文档/OpenAI](https://cz-git.qbb.sh/zh/recipes/openai)

- [verdverm/chatgpt](https://github.com/verdverm/chatgpt)

    通过命令行与 ChatGPT API 进行交互式会话，支持通过文件输入上下文。

- [ai-cli](https://github.com/yufeikang/ai-cli)

    这个cli工具可以让你方便的在命令行中使用chatGPT。你可以和他聊天支持上下文，也可以让他帮你回答单个问题。也可以帮你翻译文本。并且支持markdown在终端中的渲染。

## 应用

- [OpenCat](https://opencat.app/)

    MacOS 原生的 ChatGPT API 客户端应用。

- [OpenAI Translator](https://translator.lance.moe/)

    基于 ChatGPT API 的翻译应用，支持 PWA。源码: [LanceMoe/openai-translator](https://github.com/LanceMoe/openai-translator)

- [BiliGPT](https://b.jimmylv.cn/)

    一键总结含字幕的哔哩哔哩视频内容。源码: [JimmyLv/BiliGPT](https://github.com/JimmyLv/BiliGPT)

- [ResearchGPT](https://researchgpt.ue.r.appspot.com/)

    使你可以与 PDF 文件对话的应用，适合论文阅读和研究等学习需求。源码: [ResearchGPT](https://github.com/mukulpatnaik/researchgpt)

    作者和其他推友关于这个应用实现细节的技术讨论: [@mukul0x](https://twitter.com/mukul0x/status/1625673579399446529), [@goldengrape](https://twitter.com/goldengrape/status/1632184344881274882)

- [NITM GPT](https://github.com/deskbtm/nitmgpt)

    通过 GPT3 过滤广告通知和垃圾消息的安卓应用。


## 聊天机器人

- Telegram
    - [karfly/chatgpt\_telegram\_bot](https://github.com/karfly/chatgpt_telegram_bot)
    - [n3d1117/chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot)
    - [RainEggplant/chatgpt-telegram-bot](https://github.com/RainEggplant/chatgpt-telegram-bot)
- WeChat
    - [zhayujie/chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)
    - [ChatGPT for Wechat](https://chatgpt4wechat.aow.me/)
- Feishu
    - [bestony/ChatGPT-Feishu](https://github.com/bestony/ChatGPT-Feishu)
    - [Leizhenpeng feishu-chatGpt](https://github.com/Leizhenpeng/feishu-chatGpt)
    - [key7men/openai-feishu-bot](https://github.com/key7men/openai-feishu-bot)


## 开发

### 开源项目

- [ChatGPT-API Demo - ddiu8081/chatgpt-demo](https://github.com/ddiu8081/chatgpt-demo)

    ChatGPT web 应用 demo，使用 Astro 和 TypeScript 开发。

- [ChatGPT Web](https://github.com/Chanzhaoyu/chatgpt-web)

    ChatGPT web 应用 demo，使用 Vue3 和 Express 开发。

- [Paul Graham GPT](https://github.com/mckaywrigley/paul-graham-gpt)

    搜索和提问 Paul Graham 的所有文章。这个项目很好地展示了如何通过
    [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
    技术将大规模文本压缩成 ChatGPT API token 限制范围内（4096 个）的 prompt。

    一些与这个项目和突破 token 数量限制相关的推文:
    [@chuangbo](https://twitter.com/chuangbo/status/1631461656151887873), [@dotey](https://twitter.com/dotey/status/1631779232455053313)

- [LlamaIndex 🦙 \(GPT Index\)](https://github.com/jerryjliu/gpt_index)

    LlamaIndex (原名 GPT Index) 是一个用于处理 LLM 外部数据的工具库。
    它提供一系列数据结构帮助开发者为各种 LLM 任务索引数据，解决 prompt 大小限制的问题。

- [Tiktokenizer](https://tiktokenizer.vercel.app/)

    在线的 tiktoken 库使用界面，帮助你计算 prompt 的 token 数量。源码: [dqbd/tiktokenizer](https://github.com/dqbd/tiktokenizer)


### 技术文章

- [I got early access to ChatGPT API and then pushed it to it’s limits. Here’s what you need to know. — Buildt](https://www.buildt.ai/blog/vm3qozd4qfrbbyzukqhynrwm9vb9tq)
- [Thread: ChatGPT API 相比 ChatGPT 的一些优点](https://twitter.com/novoreorx/status/1631250035852861440)

#!/bin/bash

target_dir=site/content/posts/the-awesome

echo "---
title: Awesome ChatGPT API
date: 2023-03-04
---
" > $target_dir/index.md
cat README.md | tail -n +4 >> $target_dir/index.md

echo "---
title: Awesome ChatGPT API
date: 2023-03-04
---
" > $target_dir/index.cn.md
cat README.cn.md | tail -n +2 >> $target_dir/index.cn.md

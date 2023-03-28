---
title: Awesome ChatGPT API
date: 2023-03-04
---


基于 [ChatGPT API](https://platform.openai.com/docs/api-reference/chat)，且允许配置自己的 [API key](https://platform.openai.com/account/api-keys) 的工具和应用的精选列表。其中也包含一些[开发](#development)相关的项目和文章。

> 由 [Reorx](https://reorx.com) 收集整理，欢迎在 Twitter 或通过 PR 向我提交新的作品，但请确保您已经阅读了[提交须知](https://github.com/reorx/awesome-chatgpt-api/issues/21)。


## 插件和扩展

- Chrome 扩展

    - [Glarity](https://glarity.app/)

        使用 ChatGPT API 生成 Google 搜索结果或 YouTube 视频的摘要，同时支持 Yahoo! JAPAN ニュース、PubMed、PMC、NewsPicks、Github、Nikkei、Bing、Google Patents。该扩展还支持 ChatGPT Webapp 的 API，无需配置即可使用。

    - [ChatGPT Sidebar](https://chatgpt-sidebar.com/)

        在任何网页中打开侧边栏，询问 ChatGPT 关于页面内容的任何事情，如解释、翻译、概括或重写。你可以自定义 prompts 以便更轻松地使用。该扩展还支持 ChatGPT Webapp 的 API，无需配置即可使用。

    - [ChatHub](https://chrome.google.com/webstore/detail/chathub-all-in-one-chatbo/iaakpnchhognanibcahlpcplchdfmgma)

        ChatHub是一款多合一聊天机器人客户端，目前支持ChatGPT和新的Bing Chat。它允许同时与多个聊天机器人进行交流，方便比较它们的答案。 Source code: [chathub-dev/chathub](https://github.com/chathub-dev/chathub)

    - [OpenAI Translator](https://github.com/yetone/openai-translator)

        使用 OpenAI API 翻译文本的 Chrome 扩展，并具有润色和摘要等其他功能。

- [Obsidian](https://obsidian.md/) 插件

    - [Obsidian Text Generator Plugin](https://github.com/nhaouari/obsidian-textgenerator-plugin)

        在 Obsidian 中根据你的笔记生成想法、头条、摘要、大纲和整段文字。

- [Logseq](https://logseq.com/) 插件

    - [Logseq Plugin GPT3 OpenAI](https://github.com/briansunter/logseq-plugin-gpt3-openai)

        在 Logseq 中使用 ChatGPT 以及其他 AI 模型的插件。

- [Roam Research](https://roamresearch.com/) Plugins

    - [roam-ai](https://github.com/LayBacc/roam-ai)

        包含三个功能: 根据当前块生成文本；使用DALL-E 2生成图像；重新表述。

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

    - [我的六個專屬 ChatGPT 助手](https://pinchlime.com/newsletters/my-six-chatgpt-assistants/)

- GitHub App

    - [CR.GPT](https://github.com/apps/cr-gpt)

        由 ChatGPT 驱动的代码审查机器人


## 应用

- [ChatPDF](https://www.chatpdf.com/)

    基于 ChatGPT API 的 PDF 内容分析工具。上传 PDF 文件后，可以对它提问任何关于这份 PDF 的问题，适合快速提取各种 paper 论文的摘要，支持中文输出。

- [ChatBox](https://github.com/Bin-Huang/chatbox)

    ChatBox 是一个 OpenAI API 的跨平台桌面客户端，也是一个 prompt 调试和管理工具。

- [ChatKit](https://chatkit.app/)

    一个轻量的 ChatGPT Web UI，可设定 URL 作为讨论的上下文。

- [Chat with GPT](https://chatwithgpt.netlify.app)

    一个开源的 ChatGPT Web UI，具有 TTS 等附加功能。源码: [cogentapps/chat-with-gpt](https://github.com/cogentapps/chat-with-gpt)

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

- [ChatGPT Translator](https://github.com/simpleapples/chatgpt-translator)

    ChatGPT Translator 是一个基于 ChatGPT 和 Electron 的开源、跨平台桌面翻译软件。

- [AI字幕翻译](https://ai.cgsv.top/)

    利用GPT-3.5翻译本地字幕文件或者B站/油管字幕。源码 [AI Subtitle](https://github.com/cgsvv/AISubtitle)

- [Visual ChatGPT](https://github.com/microsoft/visual-chatgpt)

    Visual ChatGPT是一个Web应用程序，它连接ChatGPT和一系列视觉基础模型，使得在聊天过程中可以发送和接收图像。

- [TypingMind](https://www.typingmind.com/)

    更好的 ChatGPT 界面，具有快速响应、聊天搜索、集成、提示库等增强功能。


## CLI

- [bilingual\_book\_maker](https://github.com/yihong0618/bilingual_book_maker)

    用于制作双语 epub 电子书的 Python 脚本。原推: [@yihong0618](https://twitter.com/yihong0618/status/1630948132564631552)

    Web UI [streamlit](https://goldengrape-bilingual-book-maker-streamlit-app-x7nhof.streamlit.app/)。原推: [tweet](https://twitter.com/goldengrape/status/1631549869306572800).

- [AI Commits](https://github.com/Nutlope/aicommits)

    一个用 ChatGPT API 生成 Git 提交消息的命令行工具。

- [cz-git](https://github.com/Zhengqbbb/cz-git)

    一个 Commitizen 适配器与命令行工具使用 OpenAI API 生成 Git 约定式提交格式提交消息。 [文档/OpenAI](https://cz-git.qbb.sh/zh/recipes/openai)

- [turbocommit](https://github.com/Sett17/turboCommit)

    CLI，使用阶段性差异和可选信息来创建常规提交。

- [xiaogpt](https://github.com/yihong0618/xiaogpt)

    通过小米音响的小爱同学与 ChatGPT 对话。

- [AI Vocabulary Builder](https://github.com/piglei/ai-vocabulary-builder)

    一个利用了 AI 技术的智能生词本工具，可以帮你快速构建起自己的生词库，学习起来事半功倍。

- [verdverm/chatgpt](https://github.com/verdverm/chatgpt)

    通过命令行与 ChatGPT API 进行交互式会话，支持通过文件输入上下文。

- [ai-cli](https://github.com/yufeikang/ai-cli)

    这个cli工具可以让你方便的在命令行中使用chatGPT。你可以和他聊天支持上下文，也可以让他帮你回答单个问题。也可以帮你翻译文本。并且支持markdown在终端中的渲染。

- [chatgpt-cli](https://github.com/efJerryYang/chatgpt-cli/)

    支持 Markdown 的 ChatGPT CLI 工具，使用 OpenAI 官方 API。提供多个命令实现官方 web 客户端近似的功能以方便使用，会话以 JSON 格式保存到本地。

- [chatGPT-shell-cli](https://github.com/0xacx/chatGPT-shell-cli)

    一个简单、轻量级的 shell 脚本，可从终端使用 OpenAI 的 ChatGPT 和 DALL-E。

- [i18n-cli](https://github.com/pandodao/i18n-cli)

    在命令行使用 OpenAI API 翻译 JSON 格式的本地化文件。

- [ChatGPT-for-Translation](https://github.com/Raychanan/ChatGPT-for-Translation)

    对文本文件进行翻译的 Python 脚本。同时提供双语翻译、多线程和自动处理过高的请求频率。

- [subtitle-translator](https://github.com/gnehs/subtitle-translator)

    使用ChatGPT翻译字幕，使用 NodeJS 开发的基于 ChatGPT 的字幕翻译 CLI 工具。它同时还有一个使用 Electron 开发的桌面版本 [subtitle-translator-electron](https://github.com/gnehs/subtitle-translator-electron)

- [README-AI](https://github.com/eli64s/README-AI)

    使用 OpenAI 语言模型 API，为编写美观、结构化和信息丰富的 README.md 文件而设计的命令行工具。


## 聊天机器人

- Telegram
    - [karfly/chatgpt\_telegram\_bot](https://github.com/karfly/chatgpt_telegram_bot): 开发语言 **Python**.
    - [n3d1117/chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot): 开发语言 **Python**.
    - [RainEggplant/chatgpt-telegram-bot](https://github.com/RainEggplant/chatgpt-telegram-bot): 开发语言 **JavaScript**.
    - [leafduo/chatgpt-telegram-bot](https://github.com/leafduo/chatgpt-telegram-bot): 开发语言 **Go**.
    - [TBXark/ChatGPT-Telegram-Workers](https://github.com/TBXark/ChatGPT-Telegram-Workers): 在 Cloudflare Workers 上部署自己的 Telegram ChatGPT 机器人。
    - [franalgaba/chatgpt-telegram-bot-serverless](https://github.com/franalgaba/chatgpt-telegram-bot-serverless): 在 AWS Lambda 上部署自己的 Telegram ChatGPT 机器人。
- WeChat
    - [zhayujie/chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)
    - [ChatGPT for Wechat](https://chatgpt4wechat.aow.me/)
- Feishu
    - [bestony/ChatGPT-Feishu](https://github.com/bestony/ChatGPT-Feishu)
    - [Leizhenpeng feishu-chatGpt](https://github.com/Leizhenpeng/feishu-chatGpt)
    - [go-zoox/chatgpt-for-chatbot-feishu](https://github.com/go-zoox/chatgpt-for-chatbot-feishu)
    - [key7men/openai-feishu-bot](https://github.com/key7men/openai-feishu-bot)
- DingTalk
    - [eryajf/chatgpt-dingtalk](https://github.com/eryajf/chatgpt-dingtalk): 开发语言 **Go**.
- Teams
    - [formulahendry/chatgpt-teams-bot](https://github.com/formulahendry/chatgpt-teams-bot)


## 开发

### 开源项目

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

    OpenAI 官方示例和指南，介绍如何使用 OpenAI API，包括如何嵌入长输入、流式完成、格式化更好的输入等等。

- [DocsGPT](https://github.com/arc53/docsgpt)

    使用 OpenAI API 构建文档的搜索和聊天助手。

- [Paul Graham GPT](https://github.com/mckaywrigley/paul-graham-gpt)

    搜索和提问 Paul Graham 的所有文章。这个项目很好地展示了如何通过
    [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
    技术将大规模文本压缩成 ChatGPT API token 限制范围内（4096 个）的 prompt。

    一些与这个项目和突破 token 数量限制相关的推文:
    [@chuangbo](https://twitter.com/chuangbo/status/1631461656151887873), [@dotey](https://twitter.com/dotey/status/1631779232455053313)

- [Elasticsearch + GPT3 Answerer](https://github.com/hunkim/es-gpt)

    拦截 Elasticsearch 的结果并将其发送到 GPT3，以提供准确和相关的答案来回答您的查询。

- [ChatGPT-API Demo - ddiu8081/chatgpt-demo](https://github.com/ddiu8081/chatgpt-demo)

    ChatGPT web 应用 demo，使用 Astro 和 TypeScript 开发。

- [ChatGPT Web](https://github.com/Chanzhaoyu/chatgpt-web)

    ChatGPT web 应用 demo，使用 Vue3 和 Express 开发。

- [GPT3.5-H5-lite-page](https://jichao99.github.io/GPT3.5-H5-lite-page/)

    一个 GPT3.5 的轻量级网页应用，可直接静态部署无需服务端，只使用了 HTML, CSS, jQuery。 源码: [JiChao99/GPT3.5-H5-lite-page](https://github.com/JiChao99/GPT3.5-H5-lite-page)

### 工具

- [LlamaIndex 🦙 \(GPT Index\)](https://github.com/jerryjliu/gpt_index)

    LlamaIndex (原名 GPT Index) 是一个用于处理 LLM 外部数据的工具库。
    它提供一系列数据结构帮助开发者为各种 LLM 任务索引数据，解决 prompt 大小限制的问题。

- [Tiktokenizer](https://tiktokenizer.vercel.app/)

    在线的 tiktoken 库使用界面，帮助你计算 prompt 的 token 数量。源码: [dqbd/tiktokenizer](https://github.com/dqbd/tiktokenizer)

- [OpenAI GPT-3.5 Price Calculator](https://openai.deepakness.com/)

    计算使用 OpenAI GPT-3.5 API 生成特定数量单词的成本。

### 技术文章

- [I got early access to ChatGPT API and then pushed it to it’s limits. Here’s what you need to know. — Buildt](https://www.buildt.ai/blog/vm3qozd4qfrbbyzukqhynrwm9vb9tq)
- [Thread: ChatGPT API 相比 ChatGPT 的一些优点](https://twitter.com/novoreorx/status/1631250035852861440)

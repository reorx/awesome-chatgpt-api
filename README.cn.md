# 超棒的ChatGPT API

> [English](README.md)

这是一个应用和工具的精选列表，它们不仅使用新的[ChatGPT API](https://platform.openai.com/docs/api-reference/chat)，而且允许用户配置自己的[API密钥](https://platform.openai.com/account/api-keys)，从而实现免费和按需使用自己的配额。

还有一个[开发](#development)部分，为开发人员提供了一系列项目和文章，帮助他们构建更好的应用。

访问网站以获取最新更新：[awesome-chatgpt-api.top](https://awesome-chatgpt-api.top/)

> 由[Reorx](https://reorx.com)精选，欢迎通过Twitter或PR提出新项目，但请确保您已阅读[收集标准](https://github.com/reorx/awesome-chatgpt-api/issues/21)。

**目录**

- [插件和扩展](#plugins-and-extensions)
- [Web应用](#web-apps)
  - [ChatGPT-like Web UI](#chatgpt-like-web-ui)
  - [特殊用途](#special-purpose)
- [桌面和移动应用](#desktop--mobile-apps)
  - [ChatGPT-like Web UI](#chatgpt-like-web-ui)
  - [特殊用途](#special-purpose)
- [CLI](#cli)
- [聊天机器人](#chatbots)
- [开发](#development)
  - [项目](#projects)
  - [工具](#tools)
  - [文章](#articles)


## 插件和扩展

- Chrome扩展

    - [ChatGPT Box](https://github.com/josStorer/chatGPTBox)

        在您的浏览器中深度集成ChatGPT。支持在任何页面上随时调用聊天对话框，在右键菜单中总结任何页面，独立的对话页面，多个API等等。此扩展程序适用于Chrome、Edge、Safari和Firefox。

    - [Glarity](https://glarity.app/)

        使用ChatGPT API总结Google搜索结果或YouTube视频，还支持Yahoo! ニュース、PubMed、PMC、NewsPicks、Github、Nikkei、Bing、Google Patents。此扩展还支持ChatGPT Webapp的API，无需配置。

    - [ChatGPT Sidebar](https://chatgpt-sidebar.com/)

        在任何网页中打开侧边栏，并向ChatGPT询问有关页面内容的任何内容。例如解释、翻译、总结或重写。您可以自定义提示以便更轻松地访问。此扩展还支持ChatGPT Webapp的API，无需配置。

    - [ChatHub](https://chrome.google.com/webstore/detail/chathub-all-in-one-chatbo/iaakpnchhognanibcahlpcplchdfmgma)

        ChatHub是一个全能聊天机器人客户端，目前支持ChatGPT和新的Bing Chat。它允许同时与多个聊天机器人聊天，方便比较它们的答案。源代码：[chathub-dev/chathub](https://github.com/chathub-dev/chathub)

    - [TeamSmart AI](https://www.teamsmart.ai/)

        TeamSmart AI是一个Chrome浏览器扩展，旨在提高您的生产力并增强您的ChatGPT体验。它允许您组建一个AI助手团队，帮助您完成日常任务。它可以与您自己的OpenAI API密钥一起使用。

    - [OpenAI Translator](https://github.com/yetone/openai-translator)

        一个使用OpenAI API进行文本翻译的Chrome扩展，还具有诸如润色和总结等其他功能。

    - [ChatGPT » summarize everything!](https://chrome.google.com/webstore/detail/chatgpt-%C2%BB-summarize-every/cbgecfllfhmmnknmamkejadjmnmpfjmp)

        一个Chrome扩展，可以使用ChatGPT总结任何网站。其他功能包括总结任何Youtube视频的剪辑和自定义模板。此扩展还支持ChatGPT Webapp的API，无需配置。


- [Emacs](https://www.gnu.org/software/emacs/) 插件

    - [GPTel](https://github.com/karthink/gptel)
    
        为 Emacs 添加了一个新的 major mode, 可以像 ChatGPT 网页一样聊天，支持多个聊天会话，支持将选中的任意文本发送给 ChatGPT, 以得到回答、请求润色、代码建议，等等。
        
    - [org-ai](https://github.com/rksm/org-ai) 
    
        为 Emacs 下的笔记插件 org-mode 添加了一个新的自定义块，在该块中可以和 ChatGPT 聊天，可以使用 DALL-E 生成图片。可以使用语音输入，可以将 ChatGPT 的回答用语音播放。

- [Obsidian](https://obsidian.md/) 插件

    - [Obsidian Text Generator Plugin](https://github.com/nhaouari/obsidian-textgenerator-plugin)

        基于Obsidian笔记生成想法、有吸引力的标题、摘要、大纲和整段文字。

- [Logseq](https://logseq.com/) 插件

    - [Logseq Plugin GPT3 OpenAI](https://github.com/briansunter/logseq-plugin-gpt3-openai)

        用于Logseq中GPT-3 AI辅助笔记的插件。

- [Roam Research](https://roamresearch.com/) 插件

    - [roam-ai](https://github.com/LayBacc/roam-ai)

        基于当前块生成文本；使用DALL-E 2生成图像；改写

- [Popclip](https://pilotmoon.com/popclip/) 扩展

    - [ChatGPT — PopClip Extensions](https://pilotmoon.com/popclip/extensions/page/ChatGPT)

        将所选文本发送到ChatGPT并附加响应。

    - [ChatGPT Proofreader extension for Popclip](https://reorx.com/makers-daily/003-chatgpt-proofreader-extension-popclip/)

        对所选文本进行校对并附加增强结果。

    - [ChatGPT Grammar Check PopClip Extension](https://github.com/hirakujira/ChatGPT-Grammar-Check-PopClip-Extension)

        类似于ChatGPT Proofreader扩展，但具有不同的提示和可下载的包。

- [Drafts](https://getdrafts.com/) 操作

    - [ChatGPT Conversation | Drafts Directory](https://directory.getdrafts.com/a/2HJ)

        在Drafts笔记中与ChatGPT进行对话，新的响应将附加在末尾。支持声明和修改系统、助手和用户角色消息块。

- [Bob](https://bobtranslate.com/) 插件

    - [OpenAI Translator Bob Plugin](https://github.com/yetone/bob-plugin-openai-translator)

        基于ChatGPT API的Bob插件，用于文本翻译、文本精炼和语法纠正。它有一个派生版本，专门强调校对任务：[OpenAI Polisher Bob Plugin](https://github.com/yetone/bob-plugin-openai-polisher)。

- Apple快捷方式

    - [ChatGPT Siri](https://github.com/Yue-Yang/ChatGPT-Siri)

        Siri的快捷方式，连接ChatGPT 3.5 turbo模型，支持连续对话

    - [Siri Pro](https://www.icloud.com/shortcuts/6889d862918e479693be11fd9a0293b2)

        基于**ChatGPT Siri**的增强快捷方式。原始推文：[@DottChen](https://twitter.com/DottChen/status/1631309329684123650)

    - [Share to ChatGPT](https://github.com/reorx/Share-to-ChatGPT-Shortcut)

        Share to ChatGPT是一个Apple快捷方式，允许用户将突出显示的文本分享到ChatGPT，同时包括个性化提示，响应消息将自动复制到用户的剪贴板。


- [Keyboard Maestro](https://www.keyboardmaestro.com/) 宏

## Web应用

### ChatGPT类UI

- [ChatKit](https://chatkit.app/)

    一个轻量级的ChatGPT Web UI，允许将URL设置为对话的上下文。

- [TypingMind](https://www.typingmind.com/)

    一个更好的ChatGPT UI，具有快速响应、聊天搜索、集成、提示库等增强功能。

- [ChatGPT Next Web](https://github.com/Yidadaa/ChatGPT-Next-Web)<img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    一键部署精美的ChatGPT Web UI到Vercel。该界面经过优化，支持响应式设计、暗模式和PWA。具有内置提示库、对话压缩和将聊天历史记录导出为Markdown文件等功能。

- [Chatbot UI](https://github.com/mckaywrigley/chatbot-ui) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    Chatbot UI是一个基于Chatbot UI Lite构建的OpenAI聊天模型的高级聊天机器人工具包，使用Next.js、TypeScript和Tailwind CSS。

- [Chat with GPT](https://chatwithgpt.netlify.app) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    一个开源的ChatGPT Web UI，具有TTS等附加功能。源代码：[cogentapps/chat-with-gpt](https://github.com/cogentapps/chat-with-gpt)

- [ChatGPT Web](https://github.com/Chanzhaoyu/chatgpt-web) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    一个使用Vue3和Express构建的ChatGPT Web应用程序演示。

- [Next.js ChatGPT](https://github.com/enricoros/nextjs-chatgpt-app) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    使用Next.js和TypeScript构建，这是一个由OpenAI的GPT-4驱动的响应式聊天Web应用程序，具有聊天流、代码高亮、代码执行、开发预设等功能。

- [ChatGPT-API Demo](https://github.com/ddiu8081/chatgpt-demo) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    一个使用Astro和TypeScript构建的ChatGPT Web应用程序演示。

    相关项目：[ChatGPT-Vercel](https://github.com/ourongxing/chatgpt-vercel)是另一个基于ddiu8081/chatgpt-demo的ChatGPT Web应用程序，专门用于在Vercel上部署。


### 特定用途

- [ChatFiles](https://github.com/guangzhengli/ChatFiles)

    一个Web应用程序，让您上传文件并与之交谈。该存储库使用jerryjliu/llama_index来拆分大文本，基于mckaywrigley/chatbot-ui，并受到madawei2699/myGPTReader的启发。

- [ChatPDF](https://www.chatpdf.com/)

    ChatPDF是一种创新工具，允许用户与其PDF文件进行口头交流，从而更轻松地从大型文档（如手册、法律合同和研究论文）中提取信息。

- [OpenAI Translator](https://translator.lance.moe/)

    一款使用OpenAI GPT-3进行语言翻译的翻译应用程序。它是一个可以安装在手机或桌面上的PWA。源代码：[LanceMoe/openai-translator](https://github.com/LanceMoe/openai-translator)

- [BiliGPT](https://b.jimmylv.cn/)

    一键总结带字幕的Bilibili视频。源代码：[JimmyLv/BiliGPT](https://github.com/JimmyLv/BiliGPT)

- [ResearchGPT](https://researchgpt.ue.r.appspot.com/)

    这是一个flask应用程序，提供了一个界面，可以与研究论文进行交流。源代码：[mukulpatnaik/ResearchGPT](https://github.com/mukulpatnaik/researchgpt)。

    作者探索了利用与原始推文中的提示密切匹配的文本派生的向量嵌入的利用：[@mukul0x](https://twitter.com/mukul0x/status/1625673579399446529)

- [ChatGPT Academic](https://github.com/binary-husky/chatgpt_academic)

    专门用于科学研究工作的专业ChatGPT应用程序，针对学术论文校对体验进行了优化，支持自定义快捷按钮，支持Markdown表格显示，Tex公式双重显示，改进的代码显示功能，添加了本地Python项目分析/自我分析功能。

- [AI Subtitle Translator](https://ai.cgsv.top/)

    使用GPT-3.5 API翻译本地或Youtube/Bilibili字幕。源代码：[AI Subtitle](https://github.com/cgsvv/AISubtitle)

- [Visual ChatGPT](https://github.com/microsoft/visual-chatgpt)

    Visual ChatGPT是一个Web应用程序，将ChatGPT和一系列Visual Foundation模型连接起来，使得在聊天过程中可以发送和接收图像。


## 桌面和移动应用程序


### ChatGPT类UI

- [ChatBox](https://github.com/Bin-Huang/chatbox)

    ChatBox是一个跨平台的OpenAI API桌面客户端，也是一个提示调试和管理工具。

- [OpenCat](https://opencat.app/)

    一个本地的ChatGPT客户端，利用您自己的API密钥，提供更快速和增强的聊天体验。

- [MacGPT](https://www.macgpt.com/)

    一个本地的ChatGPT应用程序，具有全局访问ChatGPT的功能，可以通过MacGPT Inline直接将ChatGPT带入您的文本字段，并可以快速从菜单栏访问ChatGPT。

- [AssisChat](https://assischat.com)

    运行在iOS上的ChatGPT API客户端。它可以利用系统的共享功能，在不离开其他应用程序的情况下进行翻译和润色文本。

- [OpenChit](https://apps.apple.com/cn/app/openchit/id6446192123)

    运行在iOS上的ChatGPT API客户端。具有语音输入和TTS等功能。


### 特定用途

- [ChatGPT Translator](https://github.com/simpleapples/chatgpt-translator)

    ChatGPT Translator是一款开源的桌面应用程序，允许您使用GPT语言模型翻译文本。

- [OpenAI Translator](https://github.com/yetone/openai-translator)

    基于ChatGPT API的浏览器扩展和跨平台桌面应用程序。

# 使用GPT AI过滤广告、垃圾邮件和通知的Android应用程序。

## CLI

- [bilingual\_book\_maker](https://github.com/yihong0618/bilingual_book_maker)

    使用AI翻译制作双语epub书籍。原始推文[@yihong0618](https://twitter.com/yihong0618/status/1630948132564631552)

    作者在[streamlit](https://goldengrape-bilingual-book-maker-streamlit-app-x7nhof.streamlit.app/)上制作了一个Web UI，推文作者是[这个](https://twitter.com/goldengrape/status/1631549869306572800)。

- [AI Commits](https://github.com/Nutlope/aicommits)

    一个CLI，使用AI为您编写git提交消息。

- [cz-git](https://github.com/Zhengqbbb/cz-git)

    一个Commitizen CLI和Commitizen适配器，使用AI生成标准化的提交消息。[Recipes/OpenAI](https://cz-git.qbb.sh/recipes/openai)

- [turbocommit](https://github.com/Sett17/turboCommit)

    使用暂存差异和可选消息创建常规提交的CLI。

- [xiaogpt](https://github.com/yihong0618/xiaogpt)

    与小米AI音箱一起玩ChatGPT。

- [AI Vocabulary Builder](https://github.com/piglei/ai-vocabulary-builder)

    一个CLI，帮助您使用AI构建词汇表。

- [verdverm/chatgpt](https://github.com/verdverm/chatgpt)

    用于与ChatGPT API交互或在基于文件的会话中工作的CLI应用程序。支持提示工程和大多数配置。

- [ai-cli](https://github.com/yufeikang/ai-cli)

    此CLI工具允许您轻松在命令行中使用chatGPT。您可以与它聊天，问它问题并获得文本翻译。它还支持在终端中呈现Markdown。

- [chatgpt-cli](https://github.com/efJerryYang/chatgpt-cli/)

    一个支持Markdown的命令行界面工具，使用OpenAI的API密钥连接到ChatGPT。提供的命令使您可以像使用官方Web客户端一样使用此工具。对话以JSON格式保存在您的计算机上。

- [chatGPT-shell-cli](https://github.com/0xacx/chatGPT-shell-cli)

    一个简单，轻量级的shell脚本，可从终端使用OpenAI的chatGPT和DALL-E。

- [i18n-cli](https://github.com/pandodao/i18n-cli)

    一个命令行界面（CLI）工具，利用OpenAI API根据JSON格式翻译区域设置文件。

- [ChatGPT-for-Translation](https://github.com/Raychanan/ChatGPT-for-Translation)

    用于翻译文本文件的Python工具。它提供双语翻译，多线程和自动处理过度请求频率。

- [subtitle-translator](https://github.com/gnehs/subtitle-translator)

    基于ChatGPT开发的字幕翻译CLI工具，使用NodeJS。它还有一个Electron GUI版本[subtitle-translator-electron](https://github.com/gnehs/subtitle-translator-electron)

- [Multimedia GPT](https://github.com/fengyuli2002/multimedia-gpt)

    Multimedia GPT将OpenAI GPT与视觉和音频连接起来。用户现在可以发送图像，视频和音频录音，并以文本和图像格式获得响应。

- [README-AI](https://github.com/eli64s/README-AI)

    用于制作美观，结构化和信息丰富的README.md文件的命令行工具。由OpenAI的语言模型API提供支持。

- [GPTerminator](https://github.com/AineeJames/ChatGPTerminator)

    GPTerminator是一个Python包，它提供了一种方便的方式，使用命令行界面与OpenAI的聊天完成和图像生成API进行交互。

- [naming](https://github.com/davidleitw/naming)

    naming是一个命令行工具，为您的函数和变量建议直观和描述性的名称，提高代码的可读性。它使用ChatGPT API生成针对您的代码量身定制的程序命名建议。

- [AI Shell](https://github.com/BuilderIO/ai-shell)

    一个CLI，将自然语言转换为shell命令。受Github Copilot X CLI的启发，但对所有人开放源代码。

- [DoctorGPT](https://github.com/ingyamilmolinar/doctorgpt)

    DoctorGPT将GPT引入生产环境，用于应用程序日志错误诊断。

## Chatbots

- 电报
    - [karfly/chatgpt\_telegram\_bot](https://github.com/karfly/chatgpt_telegram_bot)：用**Python**编写。
    - [n3d1117/chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot)：用**Python**编写。
    - [RainEggplant/chatgpt-telegram-bot](https://github.com/RainEggplant/chatgpt-telegram-bot)：用**JavaScript**编写。
    - [leafduo/chatgpt-telegram-bot](https://github.com/leafduo/chatgpt-telegram-bot)：用**Go**编写。
    - [TBXark/ChatGPT-Telegram-Workers](https://github.com/TBXark/ChatGPT-Telegram-Workers)：这个是专门为**Cloudflare Workers**制作的。
    - [franalgaba/chatgpt-telegram-bot-serverless](https://github.com/franalgaba/chatgpt-telegram-bot-serverless)：免费的AWS无服务器机器人，用**Python**编写。
    - [iamwavecut/telegram-chatgpt-bot](https://github.com/iamwavecut/telegram-chatgpt-bot)：用**Go**编写，并附带**Dockerfile**以便轻松设置。
- Slack
    - [myGPTReader](https://github.com/madawei2699/myGPTReader)

        myGPTReader是一个Slack机器人，可以阅读任何网页，电子书，视频（YouTube）或文档，并使用chatGPT进行摘要。它还可以使用频道中的内容通过语音与您交谈。
- 微信
    - [zhayujie/chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)
    - [ChatGPT for Wechat](https://chatgpt4wechat.aow.me/)
- 飞书
    - [bestony/ChatGPT-Feishu](https://github.com/bestony/ChatGPT-Feishu)
    - [Leizhenpeng feishu-chatGpt](https://github.com/Leizhenpeng/feishu-chatGpt)
    - [go-zoox/chatgpt-for-chatbot-feishu](https://github.com/go-zoox/chatgpt-for-chatbot-feishu)
    - [key7men/openai-feishu-bot](https://github.com/key7men/openai-feishu-bot)
- 钉钉
    - [eryajf/chatgpt-dingtalk](https://github.com/eryajf/chatgpt-dingtalk)：用**Go**编写。
- Teams
    - [formulahendry/chatgpt-teams-bot](https://github.com/formulahendry/chatgpt-teams-bot)


## 开发

### 项目

# 开源项目和工具，帮助你更好地使用 OpenAI API

以下是一些有用的开源项目和工具，可以帮助你更好地使用 OpenAI API。

## 开源项目

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

    官方示例和指南，介绍如何使用 OpenAI API，包括如何嵌入长输入、流式完成、更好地格式化输入等等。

- [DocsGPT](https://github.com/arc53/docsgpt)

    一个开源解决方案，简化了在项目文档中查找信息的过程。通过强大的 GPT 模型，开发人员可以轻松地提出关于项目的问题并获得准确的答案。

- [Paul Graham GPT](https://github.com/mckaywrigley/paul-graham-gpt)

    基于人工智能的搜索和聊天工具，用于搜索 Paul Graham 的文章。这是一个非常好的演示，展示了如何使用 [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings) 将大量文本数据压缩为 ChatGPT API 的 4096 个令牌限制内的提示。

    关于这个项目和令牌限制的一些有见地的推文：[@chuangbo](https://twitter.com/chuangbo/status/1631461656151887873)，[@dotey](https://twitter.com/dotey/status/1631779232455053313)

- [Elasticsearch + GPT3 Answerer](https://github.com/hunkim/es-gpt)

    拦截 Elasticsearch 的结果并将其发送到 GPT3，以提供准确和相关的答案。

## 工具

- [LlamaIndex 🦙 \(GPT Index\)](https://github.com/jerryjliu/gpt_index)

    LlamaIndex (GPT Index) 是一个项目，提供了一个中央接口，将你的 LLM 与外部数据连接起来。它有一组数据结构，允许你为各种 LLM 任务索引你的数据，并消除提示大小限制的问题。

- [gptcache](https://github.com/zilliztech/gptcache) ⭐️

    一个强大的缓存库，可用于加速和降低依赖 LLM 服务的聊天应用程序的成本。GPT Cache 作为 AIGC 应用程序的 memcache，类似于 Redis 用于传统应用程序。

- [Tiktokenizer](https://tiktokenizer.vercel.app/)

    OpenAI 的 tiktoken 库的在线游乐场，计算给定提示的正确令牌数。源代码：[dqbd/tiktokenizer](https://github.com/dqbd/tiktokenizer)

- [ChatGPT Wrapper](https://github.com/mmabrouk/chatgpt-wrapper)

    ChatGPT Wrapper 是一个开源的非官方 Power CLI、Python API 和 Flask API，可以让你以编程方式与 ChatGPT/GPT4 进行交互。支持连接到 ChatGPT 模型的多个不同后端，包括基于浏览器和基于 REST 的选项。

- [OpenAI GPT-3.5 价格计算器](https://openai.deepakness.com/)

    计算使用 OpenAI GPT-3.5 API 生成一定数量的单词将花费多少钱。

- [OpenAI proxy](https://github.com/egoist/openai-proxy)

    一个可以部署在 Cloudflare Workers 和 Vercel Edge 上的 OpenAI API 反向代理。有助于绕过网络限制或 IP 速率限制。

## 文章

- [我获得了 ChatGPT API 的早期访问权限，然后将其推向了极限。这是你需要知道的。— Buildt](https://www.buildt.ai/blog/vm3qozd4qfrbbyzukqhynrwm9vb9tq)
- [线程：ChatGPT API 相对于 ChatGPT 的优势](https://twitter.com/novoreorx/status/1631250035852861440)
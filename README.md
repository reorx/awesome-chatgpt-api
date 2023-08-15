# Awesome ChatGPT API

> [中文](README.cn.md)

Curated list of apps and tools that not only use the new [ChatGPT API](https://platform.openai.com/docs/api-reference/chat), but also allow users to configure their own [API keys](https://platform.openai.com/account/api-keys), enabling free and on-demand usage of their own quota.

There's also a [Development](#development) section that provides developers with a collection of projects and articles to help them build better.

Visit the website to get latest updates: [awesome-chatgpt-api.top](https://awesome-chatgpt-api.top/)

> Curated by [Reorx](https://reorx.com), you are welcome to suggest new projects via Twitter or PRs, but please ensure you have read the [Collection Standard](https://github.com/reorx/awesome-chatgpt-api/issues/21).


**Table of Contents**

- [Plugins and Extensions](#plugins-and-extensions)
- [Web Apps](#web-apps)
  - [ChatGPT-like Web UI](#chatgpt-like-web-ui)
  - [Special-purpose](#special-purpose)
- [Desktop & Mobile Apps](#desktop--mobile-apps)
  - [ChatGPT-like Web UI](#chatgpt-like-web-ui)
  - [Special-purpose](#special-purpose)
- [CLI](#cli)
- [Chatbots](#chatbots)
- [Development](#development)
  - [Projects](#projects)
  - [Tools](#tools)
  - [Articles](#articles)


## Plugins and Extensions

- Chrome Extensions

    - [Immersive Translate](https://github.com/immersive-translate/immersive-translate)

        A dual web page translation extension with immersive reading experience, you can add your own OpenAI key to use ChatGPT as a translation provider.

    - [ChatGPT Box](https://github.com/josStorer/chatGPTBox)

        Deep ChatGPT integrations in your browser. Supports call up the chat dialog box on any page at any time, summarize any page with right-click menu, Independent conversation page, multiple API and much more. This extension is available on Chrome, Edge, Safari and Firefox.

    - [Glarity](https://glarity.app/)

         Summarize Google search results or YouTube videos with ChatGPT API, also supports Yahoo! ニュース、PubMed、PMC、NewsPicks、Github、Nikkei、 Bing、Google Patents. This extension also supports ChatGPT Webapp's API which requires no configuration.

    - [ChatGPT Sidebar](https://chatgpt-sidebar.com/)

        Open a sidebar in any webpage, and ask ChatGPT for anything about the content of the page. Like explain, translate, summarize or rewrite it. You can customize prompts for easier access. This extension also supports ChatGPT Webapp's API that requires no configuration.

    - [ChatHub](https://chrome.google.com/webstore/detail/chathub-all-in-one-chatbo/iaakpnchhognanibcahlpcplchdfmgma)

        ChatHub is an all-in-one chatbot client currently supporting ChatGPT and the new Bing Chat. It allows for chatting with multiple chatbots simultaneously, making it easy to compare their answers. Source code: [chathub-dev/chathub](https://github.com/chathub-dev/chathub)

    - [TeamSmart AI](https://www.teamsmart.ai/)

        TeamSmart AI is a Chrome browser extension designed to boost your productivity and enhance your ChatGPT experience. It allows you to assemble a team of AI assistants to help you with your daily tasks. It can be used with your own OpenAI API key.

    - [OpenAI Translator](https://github.com/yetone/openai-translator)

        A Chrome extension that uses the OpenAI API to translate text, with additional features like polishing and summarization.

    - [ChatGPT » summarize everything!](https://chrome.google.com/webstore/detail/chatgpt-%C2%BB-summarize-every/cbgecfllfhmmnknmamkejadjmnmpfjmp)

        A Chrome extension that summarizes any website with ChatGPT.
        Other features including summarizes the transcript of any Youtube Video and customizes template. This extension also supports ChatGPT Webapp's API which requires no configuration.

- [Emacs](https://www.gnu.org/software/emacs/) Packages

    - [GPTel](https://github.com/karthink/gptel)
    
        Add a major mode to Emacs that acts similar to ChatGPT web page. It supports multiple chat sessions and can send any text selection to ChatGPT API to get answers, proofreading, code suggestions, etc. 
        
    - [org-ai](https://github.com/rksm/org-ai) 
    
        Add a block to Emacs note-taking package org-mode that can chat with ChatGPT and use DALL-E to generate an image. It supports speech-to-text input and text-to-speech reading out.

- [Obsidian](https://obsidian.md/) Plugins

    - [Obsidian Text Generator Plugin](https://github.com/nhaouari/obsidian-textgenerator-plugin)

        Generate ideas, attractive titles, summaries, outlines, and whole paragraphs based on your notes in Obsidian.

- [Logseq](https://logseq.com/) Plugins

    - [Logseq Plugin GPT3 OpenAI](https://github.com/briansunter/logseq-plugin-gpt3-openai)

        A plugin for GPT-3 AI assisted note taking in Logseq.

- [Roam Research](https://roamresearch.com/) Plugins

    - [roam-ai](https://github.com/LayBacc/roam-ai)

        Generate text based on the current block; Generate an image using DALL-E 2; Rephrase

- [Popclip](https://pilotmoon.com/popclip/) Extensions

    - [ChatGPT — PopClip Extensions](https://pilotmoon.com/popclip/extensions/page/ChatGPT)

        Send the selected text to ChatGPT and append the response.

    - [ChatGPT Proofreader extension for Popclip](https://reorx.com/makers-daily/003-chatgpt-proofreader-extension-popclip/)

        Proofread the selected text and append the enhanced result.

    - [ChatGPT Grammar Check PopClip Extension](https://github.com/hirakujira/ChatGPT-Grammar-Check-PopClip-Extension)

        Similar to the ChatGPT Proofreader extension, with a different prompt and a downloadable package.

- [Drafts](https://getdrafts.com/) Actions

    - [ChatGPT Conversation | Drafts Directory](https://directory.getdrafts.com/a/2HJ)

        Have a conversation with ChatGPT in the Drafts note, new responses will be appended at the end. Supports declaring and modifying system, assistant and user role message blocks.

- [Bob](https://bobtranslate.com/) Plugins

    - [OpenAI Translator Bob Plugin](https://github.com/yetone/bob-plugin-openai-translator)

        ChatGPT API based Bob plugin for text translation, text refinement, and grammar correction. It has a derived version that specifically emphasizes the task of proofreading: [OpenAI Polisher Bob Plugin](https://github.com/yetone/bob-plugin-openai-polisher).

- Apple Shortcuts

    - [ChatGPT Siri](https://github.com/Yue-Yang/ChatGPT-Siri)

        Shortcuts for Siri to connect ChatGPT 3.5 turbo model, supports continuous conversations

    - [Siri Pro](https://www.icloud.com/shortcuts/6889d862918e479693be11fd9a0293b2)

        A enhanced shortcut based on **ChatGPT Siri**. Original tweet: [@DottChen](https://twitter.com/DottChen/status/1631309329684123650)

    - [Share to ChatGPT](https://github.com/reorx/Share-to-ChatGPT-Shortcut)

        Share to ChatGPT is an Apple Shortcut that allows users to share highlighted text to ChatGPT while also including personalized prompts, the response message will automatically be copied to the user's clipboard.

- [Keyboard Maestro](https://www.keyboardmaestro.com/) Macros

    - [Copy to Ask ChatGPT](https://blog.retompi.com/post/use-chatgpt-api/#keyboard-maestro)

        Select and copy texts to ask ChatGPT with a keyboard shortcut. [Download link](https://p15.p3.n0.cdn.getcloudapp.com/items/geuEZvwA/aeed10cb-a35d-404f-a17f-da1d46c9c9c7.kmmacros)

    - [My Six ChatGPT Assistants](https://pinchlime.com/newsletters/my-six-chatgpt-assistants/)

- GitHub App

    - [CR.GPT](https://github.com/apps/cr-gpt)

        A code review robot powered by ChatGPT

- [LaunchBar](https://www.obdev.at/products/launchbar/) Actions

    - [ChipiChat](https://github.com/quinncomendant/ChipiChat.lbaction)

        A LaunchBar action to interact with the ChatGPT API. Responses are received directly in LaunchBar and can be browsed, opened, previewed with Quick Look, inserted, or sent to another action. Conversation history is preserved for context. ChatGPT system messages are configurable via personas.


## Web Apps


### ChatGPT-like UI

- [ChatKit](https://chatkit.app/)

    A lightweight ChatGPT Web UI that allows setting URLs as context for conversations.

- [TypingMind](https://www.typingmind.com/)

    A better UI for ChatGPT, with enhanced features like fast response, chat search, integrations, prompt library, etc.

- [ChatGPT Next Web](https://github.com/Yidadaa/ChatGPT-Next-Web)<img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    One-Click to deploy well-designed ChatGPT web UI on Vercel. The interface is polished to support pesponsive design, dark mode and PWA. With features like builtin prompts library, conversation compression, and export chat history as Markdown file.

- [Chatbot UI](https://github.com/mckaywrigley/chatbot-ui) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    Chatbot UI is an advanced chatbot kit for OpenAI's chat models built on top of Chatbot UI Lite using Next.js, TypeScript, and Tailwind CSS.

- [Chat with GPT](https://chatwithgpt.netlify.app) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    An open source ChatGPT web UI with additional features like TTS. Source code: [cogentapps/chat-with-gpt](https://github.com/cogentapps/chat-with-gpt)

- [ChatGPT Web](https://github.com/Chanzhaoyu/chatgpt-web) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    A ChatGPT web app demo built with Vue3 and Express.

- [Next.js ChatGPT](https://github.com/enricoros/nextjs-chatgpt-app) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    Built using Next.js and TypeScript, this is a responsive chat web application powered by OpenAI's GPT-4, with chat streaming, code highlighting, code execution, development presets, and more.

- [ChatGPT-API Demo](https://github.com/ddiu8081/chatgpt-demo) <img src="https://img.shields.io/badge/-self--hosted-1adc61" />

    A ChatGPT web app demo built with Astro and TypeScript.

    Related project: [ChatGPT-Vercel](https://github.com/ourongxing/chatgpt-vercel) is another ChatGPT web app based on ddiu8081/chatgpt-demo, specifically made for deploying on Vercel.


### Special-purpose

- [ChatFiles](https://github.com/guangzhengli/ChatFiles)

    A web app that let you upload your file and have a conversation with it.
    This repository uses jerryjliu/llama_index to split large text, is based on mckaywrigley/chatbot-ui, and is inspired by madawei2699/myGPTReader

- [ChatPDF](https://www.chatpdf.com/)

    ChatPDF is an innovative tool that allows users to verbally communicate with their PDF files, making it easier to extract information from large documents such as manuals, legal contracts, and research papers.

- [OpenAI Translator](https://translator.lance.moe/)

    A translator app that uses OpenAI GPT-3 to translate between languages. It is a PWA that can be installed on your phone or desktop. Source code: [LanceMoe/openai-translator](https://github.com/LanceMoe/openai-translator)

- [BiliGPT](https://b.jimmylv.cn/)

    One-click summary of the subtitled Bilibili Video. Source code: [JimmyLv/BiliGPT](https://github.com/JimmyLv/BiliGPT)

- [ResearchGPT](https://researchgpt.ue.r.appspot.com/)

    This is a flask app provides an interface to enable a conversation with a research paper.
    Source code: [mukulpatnaik/ResearchGPT](https://github.com/mukulpatnaik/researchgpt).

    The author explored the utilization of vector embeddings derived from the text that closely matches the prompt in the original tweet: [@mukul0x](https://twitter.com/mukul0x/status/1625673579399446529)

- [ChatGPT Academic](https://github.com/binary-husky/chatgpt_academic)

    Specialized ChatGPT application for scientific research work, optimized for academic paper proofreading experience, supports custom shortcut buttons, supports markdown table display, Tex formula dual display, improved code display function, added local Python project analysis/self-analysis function.

- [AI Subtitle Translator](https://ai.cgsv.top/)

    Translate local or Youtube/Bilibili subtitle using GPT-3.5 API. Source Code: [AI Subtitle](https://github.com/cgsvv/AISubtitle)

- [Visual ChatGPT](https://github.com/microsoft/visual-chatgpt)

    Visual ChatGPT is a web app that connects ChatGPT and a series of Visual Foundation Models to enable sending and receiving images during chatting.


## Desktop & Mobile Apps


### ChatGPT-like UI

- [ChatBox](https://github.com/Bin-Huang/chatbox)

    ChatBox is a cross-platform desktop client for OpenAI API, also a prompt debugging and management tool.

- [OpenCat](https://opencat.app/)

    A native desktop ChatGPT client that utilizes your own API key, providing a faster and enhanced chat experience.

- [MacGPT](https://www.macgpt.com/)

    A native desktop ChatGPT app, with features like access ChatGPT from anywhere on your Mac with the Global, bring ChatGPT directly into your textfields with MacGPT Inline, and quickly access chatGPT from your menu bar.

- [AssisChat](https://assischat.com)

    A ChatGPT API client running on the iOS. It can be used to translate and polish text without leaving other apps by utilizing the system's share feature.

- [OpenChit](https://apps.apple.com/cn/app/openchit/id6446192123)

    A ChatGPT API client running on the iOS. With features like voice input and TTS.

- [MindMac](https://mindmac.app)

    Effortlessly manage your chats and folders while monitoring costs with intuitive macOS app, powered by ChatGPT API and designed for maximum productivity. Built-in prompt templates, support GPT-3.5 and GPT-4.
  
- [EasyChat AI](https://easychat-ai.app)

    A native Windows desktop app for using ChatGPT using the latest Windows 11 UI design principles.

- [WristAssist](https://github.com/DevEmperor/WristAssist)

  A powerful ChatGPT app for all WearOS devices

### Special-purpose

- [ChatGPT Translator](https://github.com/simpleapples/chatgpt-translator)

    ChatGPT Translator is an open-source desktop app that allows you to translate text using GPT language model.

- [OpenAI Translator](https://github.com/yetone/openai-translator)

    Browser extension and cross-platform desktop application for translation based on ChatGPT API.
    
- [Polyglot](https://github.com/liou666/polyglot) 

    Desktop AI language practice application based on ChatGPT API and Azure TTS

- [NITM GPT](https://github.com/deskbtm/nitmgpt)

    An Android application that filters ads, spam, notifications using GPT AI.

- [CommuniqAI](https://play.google.com/store/apps/details?id=dev.mtc.ga)

    An Android application that helps you stay in touch by scheduling and automating SMS text messages (and calls and email) while leveraging ChatGPT for message generation.


## CLI

- [ShellGPT](https://github.com/TheR1D/shell_gpt)

    A command-line productivity tool powered by ChatGPT. Features include generate shell commands, code snippets, comments, and documentation.

- [bilingual\_book\_maker](https://github.com/yihong0618/bilingual_book_maker)

    Make bilingual epub books Using AI translate. Original tweet [@yihong0618](https://twitter.com/yihong0618/status/1630948132564631552)

    There's a web UI at [streamlit](https://goldengrape-bilingual-book-maker-streamlit-app-x7nhof.streamlit.app/), made by the author of this [tweet](https://twitter.com/goldengrape/status/1631549869306572800).

- [AI Commits](https://github.com/Nutlope/aicommits)

    A CLI that writes your git commit messages for you with AI.

- [cz-git](https://github.com/Zhengqbbb/cz-git)

    A Commitizen CLI and Commitizen adapter generate standardized commit messages with AI. [Recipes/OpenAI](https://cz-git.qbb.sh/recipes/openai)

- [turbocommit](https://github.com/Sett17/turboCommit)

    CLI that uses the staged diff and optional message to create Conventional commits.

- [xiaogpt](https://github.com/yihong0618/xiaogpt)

    Play ChatGPT with Xiaomi AI Speaker.

- [AI Vocabulary Builder](https://github.com/piglei/ai-vocabulary-builder)

    A CLI that helps you build your vocabulary with AI.

- [verdverm/chatgpt](https://github.com/verdverm/chatgpt)

    CLI application for working with ChatGPT API interactively or in file based sessions. Supports promt engineering and most configurations.

- [ai-cli](https://github.com/yufeikang/ai-cli)

    This CLI tool allows you to easily use chatGPT in the command line. You can chat with it, ask it questions, and get text translations. It also supports rendering Markdown in the terminal.

- [chatgpt-cli](https://github.com/efJerryYang/chatgpt-cli/)

    A markdown-supported command-line interface tool that connects to ChatGPT using OpenAI's API key. Commands provided enable you to use this tool much like you would use the official web client. Conversations are saved as JSON format in your machine.

- [chatGPT-shell-cli](https://github.com/0xacx/chatGPT-shell-cli)

    A simple, lightweight shell script to use OpenAI's chatGPT and DALL-E from the terminal.

- [i18n-cli](https://github.com/pandodao/i18n-cli)

    A command-line interface (CLI) tool that utilizes the OpenAI API to translate locale files based on JSON format.

- [ChatGPT-for-Translation](https://github.com/Raychanan/ChatGPT-for-Translation)

    Python tool for translating text files. It provides bilingual translation, multithreading, and automatic handling of excessive request frequency.

- [subtitle-translator](https://github.com/gnehs/subtitle-translator)

    A subtitle translation CLI tool based on ChatGPT developed using NodeJS. It also has a Electron GUI version [subtitle-translator-electron](https://github.com/gnehs/subtitle-translator-electron)

- [Multimedia GPT](https://github.com/fengyuli2002/multimedia-gpt)

    Multimedia GPT connects OpenAI GPT with vision and audio. Users can now send images, videos, and audio recordings and get a response in both text and image formats.

- [README-AI](https://github.com/eli64s/README-AI)

    Command-line tool for crafting aesthetic, structured, and informative README.md files. Powered by OpenAI's language model API.

- [GPTerminator](https://github.com/AineeJames/ChatGPTerminator)

    GPTerminator is a python package that provides a convenient way to interact with OpenAI's chat completion and image generation API's using your command line interface.

- [naming](https://github.com/davidleitw/naming)

    naming is a command line tool that suggests intuitive and descriptive names for your functions and variables, improving the readability of your code. It uses ChatGPT API to generate program naming suggestions tailored to your code.
    
- [AI Shell](https://github.com/BuilderIO/ai-shell)

    A CLI that converts natural language to shell commands. Inspired by the Github Copilot X CLI, but open source for everyone.

- [DoctorGPT](https://github.com/ingyamilmolinar/doctorgpt)

    DoctorGPT brings GPT into production for application log error diagnosing.

- [aider](https://github.com/paul-gauthier/aider)

    aider is a command-line chat tool that allows you to code with GPT-4 in the terminal. Ask GPT for features, improvements, or bug fixes and aider will apply the suggested changes to your source files. Each change is automatically committed to git with a descriptive commit message.

- [mods](https://github.com/charmbracelet/mods)

    mods works by reading standard in and prefacing it with a prompt supplied in the mods arguments. Optionally it formats output as Markdown, which you can pipe to markdown rendering CLIs. Example: `mods -f "what are your thoughts on improving this code?" < main.go | glow`

## Chatbots

- Telegram
    - [karfly/chatgpt\_telegram\_bot](https://github.com/karfly/chatgpt_telegram_bot): Written in **Python**.
    - [n3d1117/chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot): Written in **Python**.
    - [RainEggplant/chatgpt-telegram-bot](https://github.com/RainEggplant/chatgpt-telegram-bot): Written in **JavaScript**.
    - [leafduo/chatgpt-telegram-bot](https://github.com/leafduo/chatgpt-telegram-bot): Written in **Go**.
    - [TBXark/ChatGPT-Telegram-Workers](https://github.com/TBXark/ChatGPT-Telegram-Workers): This one has been specifically made for **Cloudflare Workers**.
    - [franalgaba/chatgpt-telegram-bot-serverless](https://github.com/franalgaba/chatgpt-telegram-bot-serverless): Free and in AWS serverless bot in **Python**.
    - [iamwavecut/telegram-chatgpt-bot](https://github.com/iamwavecut/telegram-chatgpt-bot): Written in **Go** and comes with the **Dockerfile** for easy setup.
- Slack
    - [myGPTReader](https://github.com/madawei2699/myGPTReader)

        myGPTReader is a slack bot that can read any webpage, ebook, video(YouTube) or document and summarize it with chatGPT. It can also talk to you via voice using the content in the channel.
- WeChat
    - [zhayujie/chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)
    - [ChatGPT for Wechat](https://chatgpt4wechat.aow.me/)
- Feishu
    - [bestony/ChatGPT-Feishu](https://github.com/bestony/ChatGPT-Feishu)
    - [Leizhenpeng feishu-chatGpt](https://github.com/Leizhenpeng/feishu-chatGpt)
    - [go-zoox/chatgpt-for-chatbot-feishu](https://github.com/go-zoox/chatgpt-for-chatbot-feishu)
    - [key7men/openai-feishu-bot](https://github.com/key7men/openai-feishu-bot)
- DingTalk
    - [eryajf/chatgpt-dingtalk](https://github.com/eryajf/chatgpt-dingtalk): Written in **Go**.
- Teams
    - [formulahendry/chatgpt-teams-bot](https://github.com/formulahendry/chatgpt-teams-bot)


## Development

### Projects

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

    Official examples and guides for using the OpenAI API, including how to embedding long inputs, stream completions, format better inputs and much more.

- [DocsGPT](https://github.com/arc53/docsgpt)

    An open-source solution that streamlines the process of finding information in project documentation. With its integration of the powerful GPT models, developers can easily ask questions about a project and receive accurate answers.

- [Paul Graham GPT](https://github.com/mckaywrigley/paul-graham-gpt)

    AI-powered search and chat for Paul Graham's essays. This is a excellent demo
    on how to use [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
    to compress large text data into prompts within the limit of ChatGPT API's 4096 tokens limit.

    Some insightful tweets about this project and token limitation: [@chuangbo](https://twitter.com/chuangbo/status/1631461656151887873), [@dotey](https://twitter.com/dotey/status/1631779232455053313)

- [Elasticsearch + GPT3 Answerer](https://github.com/hunkim/es-gpt)

    Intercepts Elasticsearch results and sends them to GPT3 to provide accurate and relevant answers to your queries.


### Tools

- [LlamaIndex 🦙 \(GPT Index\)](https://github.com/jerryjliu/gpt_index)

    LlamaIndex (GPT Index) is a project that provides a central interface to connect your LLM's with external data. It has a set of data structures that allow you to index your data for various LLM tasks, and remove concerns over prompt size limitations.

- [gptcache](https://github.com/zilliztech/gptcache) ⭐️

    a powerful caching library that can be used to speed up and lower the cost of chat applications that rely on the LLM service. GPT Cache works as a memcache for AIGC applications, similar to how Redis works for traditional applications.

- [Embedchain](https://github.com/embedchain/embedchain) 

    Framework to create LLM-powered ChatGPT like bots over your dataset

- [Tiktokenizer](https://tiktokenizer.vercel.app/)

    Online playground for openai's tiktoken library, calculating the correct number of tokens for a given prompt. Source code: [dqbd/tiktokenizer](https://github.com/dqbd/tiktokenizer)

- [ChatGPT Wrapper](https://github.com/mmabrouk/chatgpt-wrapper)

    ChatGPT Wrapper is an open-source unofficial Power CLI, Python API and Flask API that lets you interact programmatically with ChatGPT/GPT4. Several different backends are supported to connect to the ChatGPT models, including browser-based and REST-based options.

- [OpenAI GPT-3.5 Price Calculator](https://openai.deepakness.com/)

    Calculate how much it will cost to generate certain number of words by using OpenAI GPT-3.5 API.

- [OpenAI proxy](https://github.com/egoist/openai-proxy)

    An OpenAI API reverse proxy that can be deployed on Cloudflare Workers and Vercel Edge.
    Helpful for bypassing network restrictions or IP rate limits.


### Articles

- [I got early access to ChatGPT API and then pushed it to it’s limits. Here’s what you need to know. — Buildt](https://www.buildt.ai/blog/vm3qozd4qfrbbyzukqhynrwm9vb9tq)
- [Thread: Advantages of ChatGPT API compared to ChatGPT](https://twitter.com/novoreorx/status/1631250035852861440)

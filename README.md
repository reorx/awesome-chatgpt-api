# Awesome ChatGPT API

> [中文](README_cn.md)

Curated list of apps and tools, that not only use the new [ChatGPT API](https://platform.openai.com/docs/api-reference/chat), but also allow users to configure their own [API keys](https://platform.openai.com/account/api-keys), enabling free and on-demand usage of their own quota.

There's also a [Development](#development) section that provides developers with a collection of projects and articles to help them build better.

Curated by [Reorx](https://reorx.com), you are welcome to suggest new projects via Twitter or PRs, but please ensure you have read the [Collection Standard](https://github.com/reorx/awesome-chatgpt-api/issues/21).


## Plugins and Extensions

- Chrome Extensions

    - [Glarity](https://glarity.app/)

        Summary for Google search results or YouTube Videos with ChatGPT API. This extension also supports ChatGPT Webapp's API that requires no configuration.

    - [ChatGPT Sidebar](https://chatgpt-sidebar.com/)

        Open a sidebar in any webpage, and ask ChatGPT for anything about the content of the page. Like explain, translate, summarize or rewrite it. You can customize prompts for easier access. This extension also supports ChatGPT Webapp's API that requires no configuration.

- [Obsidian](https://obsidian.md/) Plugins

    - [Obsidian Text Generator Plugin](https://github.com/nhaouari/obsidian-textgenerator-plugin)

        Generate ideas, attractive titles, summaries, outlines, and whole paragraphs based on your notes in Obsidian.

- [Logseq](https://logseq.com/) Plugins

    - [Logseq Plugin GPT3 OpenAI](https://github.com/briansunter/logseq-plugin-gpt3-openai)

        A plugin for GPT-3 AI assisted note taking in Logseq.

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

- [Keyboard Maestro](https://www.keyboardmaestro.com/) Macros

    - [Copy to Ask ChatGPT](https://blog.retompi.com/post/use-chatgpt-api/#keyboard-maestro)

        Select and copy texts to ask ChatGPT with a keyboard shortcut. [Download link](https://p15.p3.n0.cdn.getcloudapp.com/items/geuEZvwA/aeed10cb-a35d-404f-a17f-da1d46c9c9c7.kmmacros)

    - [My Six ChatGPT Assistants](https://pinchlime.com/newsletters/my-six-chatgpt-assistants/)


## Apps

- [ChatPDF](https://www.chatpdf.com/)

    ChatPDF is an innovative tool that allows users to verbally communicate with their PDF files, making it easier to extract information from large documents such as manuals, legal contracts, and research papers.

- [ChatBox](https://github.com/Bin-Huang/chatbox)

    ChatBox is a cross-platform desktop client for OpenAI API, also a prompt debugging and management tool.

- [ChatKit](https://chatkit.app/)

    A lightweight ChatGPT Web UI that allows setting URLs as context for conversations.

- [Chat with GPT](https://chatwithgpt.netlify.app)

    An open source ChatGPT web UI with additional features like TTS. Source code: [cogentapps/chat-with-gpt](https://github.com/cogentapps/chat-with-gpt)

- [OpenCat](https://opencat.app/)

    A native desktop ChatGPT client that utilizes your own API key, providing a faster and enhanced chat experience.

- [OpenAI Translator](https://translator.lance.moe/)

    A translator app that uses OpenAI GPT-3 to translate between languages. It is a PWA that can be installed on your phone or desktop. Source code: [LanceMoe/openai-translator](https://github.com/LanceMoe/openai-translator)

- [BiliGPT](https://b.jimmylv.cn/)

    One-click summary of the subtitled Bilibili Video. Source code: [JimmyLv/BiliGPT](https://github.com/JimmyLv/BiliGPT)

- [ResearchGPT](https://researchgpt.ue.r.appspot.com/)

    This is a flask app provides an interface to enable a conversation with a research paper.
    Source code: [ResearchGPT](https://github.com/mukulpatnaik/researchgpt).

    The author explored the utilization of vector embeddings derived from the text that closely matches the prompt in the original tweet: [@mukul0x](https://twitter.com/mukul0x/status/1625673579399446529)

- [NITM GPT](https://github.com/deskbtm/nitmgpt)

    An Android application that filters ads, spam, notifications using GPT AI.

- [ChatGPT Translator](https://github.com/simpleapples/chatgpt-translator)

    ChatGPT Translator is an open-source desktop app that allows you to translate text using GPT language model.


## CLI

- [bilingual\_book\_maker](https://github.com/yihong0618/bilingual_book_maker)

    Make bilingual epub books Using AI translate. Original tweet [@yihong0618](https://twitter.com/yihong0618/status/1630948132564631552)

    There's a web UI at [streamlit](https://goldengrape-bilingual-book-maker-streamlit-app-x7nhof.streamlit.app/), made by the author of this [tweet](https://twitter.com/goldengrape/status/1631549869306572800).

- [AI Commits](https://github.com/Nutlope/aicommits)

    A CLI that writes your git commit messages for you with AI.

- [turbocommit](https://github.com/Sett17/turboCommit)

    CLI that uses the staged diff and optional message to create Conventional commits.

- [xiaogpt](https://github.com/yihong0618/xiaogpt)

    Play ChatGPT with Xiaomi AI Speaker.

- [AI Vocabulary Builder](https://github.com/piglei/ai-vocabulary-builder)

    A CLI that helps you build your vocabulary with AI.

- [cz-git](https://github.com/Zhengqbbb/cz-git)

    A Commitizen CLI and Commitizen adapter generate standardized commit messages with AI. [Recipes/OpenAI](https://cz-git.qbb.sh/recipes/openai)

- [i18n-cli](https://github.com/pandodao/i18n-cli)

    A command-line interface (CLI) tool that utilizes the OpenAI API to translate locale files based on JSON format.

- [verdverm/chatgpt](https://github.com/verdverm/chatgpt)

    CLI application for working with ChatGPT API interactively or in file based sessions. Supports promt engineering and most configurations.

- [ai-cli](https://github.com/yufeikang/ai-cli)

    This CLI tool allows you to easily use chatGPT in the command line. You can chat with it, ask it questions, and get text translations. It also supports rendering Markdown in the terminal.

- [ChatGPT-for-Translation](https://github.com/Raychanan/ChatGPT-for-Translation)

    Python tool for translating text files. It provides bilingual translation, multithreading, and automatic handling of excessive request frequency.


## Chatbots

- Telegram
    - [karfly/chatgpt\_telegram\_bot](https://github.com/karfly/chatgpt_telegram_bot): Written in **Python**.
    - [n3d1117/chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot): Written in **Python**.
    - [RainEggplant/chatgpt-telegram-bot](https://github.com/RainEggplant/chatgpt-telegram-bot): Written in **JavaScript**.
    - [leafduo/chatgpt-telegram-bot](https://github.com/leafduo/chatgpt-telegram-bot): Written in **Go**.
    - [TBXark/ChatGPT-Telegram-Workers](https://github.com/TBXark/ChatGPT-Telegram-Workers): This one has been specifically made for **Cloudflare Workers**.
    - [franalgaba/chatgpt-telegram-bot-serverless](https://github.com/franalgaba/chatgpt-telegram-bot-serverless): Free and in AWS serverless bot in **Python**.
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

- [ChatGPT-API Demo - ddiu8081/chatgpt-demo](https://github.com/ddiu8081/chatgpt-demo)

    A ChatGPT web app demo built with Astro and TypeScript.

- [ChatGPT Web](https://github.com/Chanzhaoyu/chatgpt-web)

    A ChatGPT web app demo built with Vue3 and Express.

- [GPT3.5-H5-lite-page](https://jichao99.github.io/GPT3.5-H5-lite-page/)

    A GPT3.5 web page that is highly lightweight and can be deployed statically without requiring a server. Only HTML, CSS, and jQuery is used. Source code: [JiChao99/GPT3.5-H5-lite-page](https://github.com/JiChao99/GPT3.5-H5-lite-page)

### Tools

- [LlamaIndex 🦙 \(GPT Index\)](https://github.com/jerryjliu/gpt_index)

    LlamaIndex (GPT Index) is a project that provides a central interface to connect your LLM's with external data. It has a set of data structures that allow you to index your data for various LLM tasks, and remove concerns over prompt size limitations.

- [Tiktokenizer](https://tiktokenizer.vercel.app/)

    Online playground for openai's tiktoken library, calculating the correct number of tokens for a given prompt. Source code: [dqbd/tiktokenizer](https://github.com/dqbd/tiktokenizer)

- [OpenAI GPT-3.5 Price Calculator](https://openai.deepakness.com/)

    Calculate how much it will cost to generate certain number of words by using OpenAI GPT-3.5 API.

### Articles

- [I got early access to ChatGPT API and then pushed it to it’s limits. Here’s what you need to know. — Buildt](https://www.buildt.ai/blog/vm3qozd4qfrbbyzukqhynrwm9vb9tq)
- [Thread: Advantages of ChatGPT API compared to ChatGPT](https://twitter.com/novoreorx/status/1631250035852861440)

<!--@nrg.languages=en,cn-->
<!--@nrg.defaultLanguage=en-->
# Awesome ChatGPT API<!--en-->
<!--en-->
> [中文](README.cn.md)<!--en-->
<!--en-->
Curated list of apps and tools that not only use the new [ChatGPT API](https://platform.openai.com/docs/api-reference/chat), but also allow users to configure their own [API keys](https://platform.openai.com/account/api-keys), enabling free and on-demand usage of their own quota.<!--en-->
<!--en-->
There's also a [Development](#development) section that provides developers with a collection of projects and articles to help them build better.<!--en-->
<!--en-->
Visit the website to get latest updates: [awesome-chatgpt-api.top](https://awesome-chatgpt-api.top/)<!--en-->
<!--en-->
> Curated by [Reorx](https://reorx.com), you are welcome to suggest new projects via Twitter or PRs, but please ensure you have read the [Collection Standard](https://github.com/reorx/awesome-chatgpt-api/issues/21).<!--en-->
<!--en-->
<!--en-->
**Table of Contents**<!--en-->
<!--en-->
- [Plugins and Extensions](#plugins-and-extensions)<!--en-->
- [Web Apps](#web-apps)<!--en-->
  - [ChatGPT-like Web UI](#chatgpt-like-web-ui)<!--en-->
  - [Special-purpose](#special-purpose)<!--en-->
- [Desktop & Mobile Apps](#desktop--mobile-apps)<!--en-->
  - [ChatGPT-like Web UI](#chatgpt-like-web-ui)<!--en-->
  - [Special-purpose](#special-purpose)<!--en-->
- [CLI](#cli)<!--en-->
- [Chatbots](#chatbots)<!--en-->
- [Development](#development)<!--en-->
  - [Projects](#projects)<!--en-->
  - [Tools](#tools)<!--en-->
  - [Articles](#articles)<!--en-->
<!--en-->
<!--en-->
## Plugins and Extensions<!--en-->
<!--en-->
- Chrome Extensions<!--en-->
<!--en-->
    - [Immersive Translate](https://github.com/immersive-translate/immersive-translate)<!--en-->
<!--en-->
        A dual web page translation extension with immersive reading experience, you can add your own OpenAI key to use ChatGPT as a translation provider.<!--en-->
<!--en-->
    - [ChatGPT Box](https://github.com/josStorer/chatGPTBox)<!--en-->
<!--en-->
        Deep ChatGPT integrations in your browser. Supports call up the chat dialog box on any page at any time, summarize any page with right-click menu, Independent conversation page, multiple API and much more. This extension is available on Chrome, Edge, Safari and Firefox.<!--en-->
<!--en-->
    - [Glarity](https://glarity.app/)<!--en-->
<!--en-->
         Summarize Google search results or YouTube videos with ChatGPT API, also supports Yahoo! ニュース、PubMed、PMC、NewsPicks、Github、Nikkei、 Bing、Google Patents. This extension also supports ChatGPT Webapp's API which requires no configuration.<!--en-->
<!--en-->
    - [ChatGPT Sidebar](https://chatgpt-sidebar.com/)<!--en-->
<!--en-->
        Open a sidebar in any webpage, and ask ChatGPT for anything about the content of the page. Like explain, translate, summarize or rewrite it. You can customize prompts for easier access. This extension also supports ChatGPT Webapp's API that requires no configuration.<!--en-->
<!--en-->
    - [ChatHub](https://chrome.google.com/webstore/detail/chathub-all-in-one-chatbo/iaakpnchhognanibcahlpcplchdfmgma)<!--en-->
<!--en-->
        ChatHub is an all-in-one chatbot client currently supporting ChatGPT and the new Bing Chat. It allows for chatting with multiple chatbots simultaneously, making it easy to compare their answers. Source code: [chathub-dev/chathub](https://github.com/chathub-dev/chathub)<!--en-->
<!--en-->
    - [OpenAI Translator](https://github.com/yetone/openai-translator)<!--en-->
<!--en-->
        A Chrome extension that uses the OpenAI API to translate text, with additional features like polishing and summarization.<!--en-->
<!--en-->
    - [ChatGPT » summarize everything!](https://chrome.google.com/webstore/detail/chatgpt-%C2%BB-summarize-every/cbgecfllfhmmnknmamkejadjmnmpfjmp)<!--en-->
<!--en-->
        A Chrome extension that summarizes any website with ChatGPT.<!--en-->
        Other features including summarizes the transcript of any Youtube Video and customizes template. This extension also supports ChatGPT Webapp's API which requires no configuration.<!--en-->
<!--en-->
- [Emacs](https://www.gnu.org/software/emacs/) Packages<!--en-->
<!--en-->
    - [GPTel](https://github.com/karthink/gptel)<!--en-->
    <!--en-->
        Add a major mode to Emacs that acts similar to ChatGPT web page. It supports multiple chat sessions and can send any text selection to ChatGPT API to get answers, proofreading, code suggestions, etc. <!--en-->
        <!--en-->
    - [org-ai](https://github.com/rksm/org-ai) <!--en-->
    <!--en-->
        Add a block to Emacs note-taking package org-mode that can chat with ChatGPT and use DALL-E to generate an image. It supports speech-to-text input and text-to-speech reading out.<!--en-->
<!--en-->
- [Obsidian](https://obsidian.md/) Plugins<!--en-->
<!--en-->
    - [Obsidian Text Generator Plugin](https://github.com/nhaouari/obsidian-textgenerator-plugin)<!--en-->
<!--en-->
        Generate ideas, attractive titles, summaries, outlines, and whole paragraphs based on your notes in Obsidian.<!--en-->
<!--en-->
- [Logseq](https://logseq.com/) Plugins<!--en-->
<!--en-->
    - [Logseq Plugin GPT3 OpenAI](https://github.com/briansunter/logseq-plugin-gpt3-openai)<!--en-->
<!--en-->
        A plugin for GPT-3 AI assisted note taking in Logseq.<!--en-->
<!--en-->
- [Roam Research](https://roamresearch.com/) Plugins<!--en-->
<!--en-->
    - [roam-ai](https://github.com/LayBacc/roam-ai)<!--en-->
<!--en-->
        Generate text based on the current block; Generate an image using DALL-E 2; Rephrase<!--en-->
<!--en-->
- [Popclip](https://pilotmoon.com/popclip/) Extensions<!--en-->
<!--en-->
    - [ChatGPT — PopClip Extensions](https://pilotmoon.com/popclip/extensions/page/ChatGPT)<!--en-->
<!--en-->
        Send the selected text to ChatGPT and append the response.<!--en-->
<!--en-->
    - [ChatGPT Proofreader extension for Popclip](https://reorx.com/makers-daily/003-chatgpt-proofreader-extension-popclip/)<!--en-->
<!--en-->
        Proofread the selected text and append the enhanced result.<!--en-->
<!--en-->
    - [ChatGPT Grammar Check PopClip Extension](https://github.com/hirakujira/ChatGPT-Grammar-Check-PopClip-Extension)<!--en-->
<!--en-->
        Similar to the ChatGPT Proofreader extension, with a different prompt and a downloadable package.<!--en-->
<!--en-->
- [Drafts](https://getdrafts.com/) Actions<!--en-->
<!--en-->
    - [ChatGPT Conversation | Drafts Directory](https://directory.getdrafts.com/a/2HJ)<!--en-->
<!--en-->
        Have a conversation with ChatGPT in the Drafts note, new responses will be appended at the end. Supports declaring and modifying system, assistant and user role message blocks.<!--en-->
<!--en-->
- [Bob](https://bobtranslate.com/) Plugins<!--en-->
<!--en-->
    - [OpenAI Translator Bob Plugin](https://github.com/yetone/bob-plugin-openai-translator)<!--en-->
<!--en-->
        ChatGPT API based Bob plugin for text translation, text refinement, and grammar correction. It has a derived version that specifically emphasizes the task of proofreading: [OpenAI Polisher Bob Plugin](https://github.com/yetone/bob-plugin-openai-polisher).<!--en-->
<!--en-->
- [Easydict](https://github.com/tisfeng/Easydict)<!--en-->
<!--en-->
    A concise and elegant dictionary and translation app for macOS that supports multiple translation services including OpenAI API, with features like OCR recognition and input translation.<!--en-->
<!--en-->
- [pot-desktop](https://github.com/pot-app/pot-desktop)<!--en-->
<!--en-->
    A cross-platform (Windows/macOS/Linux) desktop translation and OCR tool that supports customizable ChatGPT API for text translation, with features like selection translation, input translation, and clipboard listening.<!--en-->
<!--en-->
- Apple Shortcuts<!--en-->
<!--en-->
    - [ChatGPT Siri](https://github.com/Yue-Yang/ChatGPT-Siri)<!--en-->
<!--en-->
        Shortcuts for Siri to connect ChatGPT 3.5 turbo model, supports continuous conversations<!--en-->
<!--en-->
    - [Siri Pro](https://www.icloud.com/shortcuts/6889d862918e479693be11fd9a0293b2)<!--en-->
<!--en-->
        A enhanced shortcut based on **ChatGPT Siri**. Original tweet: [@DottChen](https://twitter.com/DottChen/status/1631309329684123650)<!--en-->
<!--en-->
    - [Share to ChatGPT](https://github.com/reorx/Share-to-ChatGPT-Shortcut)<!--en-->
<!--en-->
        Share to ChatGPT is an Apple Shortcut that allows users to share highlighted text to ChatGPT while also including personalized prompts, the response message will automatically be copied to the user's clipboard.<!--en-->
<!--en-->
- [Keyboard Maestro](https://www.keyboardmaestro.com/) Macros<!--en-->
<!--en-->
    - [Copy to Ask ChatGPT](https://blog.retompi.com/post/use-chatgpt-api/#keyboard-maestro)<!--en-->
<!--en-->
        Select and copy texts to ask ChatGPT with a keyboard shortcut. [Download link](https://p15.p3.n0.cdn.getcloudapp.com/items/geuEZvwA/aeed10cb-a35d-404f-a17f-da1d46c9c9c7.kmmacros)<!--en-->
<!--en-->
    - [My Six ChatGPT Assistants](https://pinchlime.com/newsletters/my-six-chatgpt-assistants/)<!--en-->
<!--en-->
- GitHub App<!--en-->
<!--en-->
    - [CR.GPT](https://github.com/apps/cr-gpt)<!--en-->
<!--en-->
        A code review robot powered by ChatGPT<!--en-->
<!--en-->
- [LaunchBar](https://www.obdev.at/products/launchbar/) Actions<!--en-->
<!--en-->
    - [ChipiChat](https://github.com/quinncomendant/ChipiChat.lbaction)<!--en-->
<!--en-->
        A LaunchBar action to interact with the ChatGPT API. Responses are received directly in LaunchBar and can be browsed, opened, previewed with Quick Look, inserted, or sent to another action. Conversation history is preserved for context. ChatGPT system messages are configurable via personas.<!--en-->
<!--en-->
<!--en-->
## Web Apps<!--en-->
<!--en-->
<!--en-->
### ChatGPT-like UI<!--en-->
<!--en-->
- [ChatKit](https://chatkit.app/)<!--en-->
<!--en-->
    A lightweight ChatGPT Web UI that allows setting URLs as context for conversations.<!--en-->
<!--en-->
- [TypingMind](https://www.typingmind.com/)<!--en-->
<!--en-->
    A better UI for ChatGPT, with enhanced features like fast response, chat search, integrations, prompt library, etc.<!--en-->
<!--en-->
- [ChatGPT Next Web](https://github.com/Yidadaa/ChatGPT-Next-Web)<img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--en-->
<!--en-->
    One-Click to deploy well-designed ChatGPT web UI on Vercel. The interface is polished to support pesponsive design, dark mode and PWA. With features like builtin prompts library, conversation compression, and export chat history as Markdown file.<!--en-->
<!--en-->
- [Chatbot UI](https://github.com/mckaywrigley/chatbot-ui) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--en-->
<!--en-->
    Chatbot UI is an advanced chatbot kit for OpenAI's chat models built on top of Chatbot UI Lite using Next.js, TypeScript, and Tailwind CSS.<!--en-->
<!--en-->
- [Chat with GPT](https://chatwithgpt.netlify.app) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--en-->
<!--en-->
    An open source ChatGPT web UI with additional features like TTS. Source code: [cogentapps/chat-with-gpt](https://github.com/cogentapps/chat-with-gpt)<!--en-->
<!--en-->
- [ChatGPT Web](https://github.com/Chanzhaoyu/chatgpt-web) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--en-->
<!--en-->
    A ChatGPT web app demo built with Vue3 and Express.<!--en-->
<!--en-->
- [Next.js ChatGPT](https://github.com/enricoros/nextjs-chatgpt-app) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--en-->
<!--en-->
    Built using Next.js and TypeScript, this is a responsive chat web application powered by OpenAI's GPT-4, with chat streaming, code highlighting, code execution, development presets, and more.<!--en-->
<!--en-->
- [ChatGPT-API Demo](https://github.com/ddiu8081/chatgpt-demo) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--en-->
<!--en-->
    A ChatGPT web app demo built with Astro and TypeScript.<!--en-->
<!--en-->
    Related project: [ChatGPT-Vercel](https://github.com/ourongxing/chatgpt-vercel) is another ChatGPT web app based on ddiu8081/chatgpt-demo, specifically made for deploying on Vercel.<!--en-->
<!--en-->
<!--en-->
### Special-purpose<!--en-->
<!--en-->
- [ChatFiles](https://github.com/guangzhengli/ChatFiles)<!--en-->
<!--en-->
    A web app that let you upload your file and have a conversation with it.<!--en-->
    This repository uses jerryjliu/llama_index to split large text, is based on mckaywrigley/chatbot-ui, and is inspired by madawei2699/myGPTReader<!--en-->
<!--en-->
- [ChatPDF](https://www.chatpdf.com/)<!--en-->
<!--en-->
    ChatPDF is an innovative tool that allows users to verbally communicate with their PDF files, making it easier to extract information from large documents such as manuals, legal contracts, and research papers.<!--en-->
<!--en-->
- [OpenAI Translator](https://translator.lance.moe/)<!--en-->
<!--en-->
    A translator app that uses OpenAI GPT-3 to translate between languages. It is a PWA that can be installed on your phone or desktop. Source code: [LanceMoe/openai-translator](https://github.com/LanceMoe/openai-translator)<!--en-->
<!--en-->
- [BiliGPT](https://b.jimmylv.cn/)<!--en-->
<!--en-->
    One-click summary of the subtitled Bilibili Video. Source code: [JimmyLv/BiliGPT](https://github.com/JimmyLv/BiliGPT)<!--en-->
<!--en-->
- [ResearchGPT](https://researchgpt.ue.r.appspot.com/)<!--en-->
<!--en-->
    This is a flask app provides an interface to enable a conversation with a research paper.<!--en-->
    Source code: [mukulpatnaik/ResearchGPT](https://github.com/mukulpatnaik/researchgpt).<!--en-->
<!--en-->
    The author explored the utilization of vector embeddings derived from the text that closely matches the prompt in the original tweet: [@mukul0x](https://twitter.com/mukul0x/status/1625673579399446529)<!--en-->
<!--en-->
- [ChatGPT Academic](https://github.com/binary-husky/chatgpt_academic)<!--en-->
<!--en-->
    Specialized ChatGPT application for scientific research work, optimized for academic paper proofreading experience, supports custom shortcut buttons, supports markdown table display, Tex formula dual display, improved code display function, added local Python project analysis/self-analysis function.<!--en-->
<!--en-->
- [AI Subtitle Translator](https://ai.cgsv.top/)<!--en-->
<!--en-->
    Translate local or Youtube/Bilibili subtitle using GPT-3.5 API. Source Code: [AI Subtitle](https://github.com/cgsvv/AISubtitle)<!--en-->
<!--en-->
- [Visual ChatGPT](https://github.com/microsoft/visual-chatgpt)<!--en-->
<!--en-->
    Visual ChatGPT is a web app that connects ChatGPT and a series of Visual Foundation Models to enable sending and receiving images during chatting.<!--en-->
<!--en-->
- [GEO/AEO Tracker](https://github.com/danishashko/geo-aeo-tracker)<!--en-->
<!--en-->
    Open-source, local-first AI visibility dashboard. Track brand mentions across ChatGPT, Perplexity, Gemini, Copilot, Google AI Overview, and Grok. BYOK, self-hosted, $0/month.<!--en-->
<!--en-->
<!--en-->
## Desktop & Mobile Apps<!--en-->
<!--en-->
<!--en-->
### ChatGPT-like UI<!--en-->
<!--en-->
- [ChatBox](https://github.com/Bin-Huang/chatbox)<!--en-->
<!--en-->
    ChatBox is a cross-platform desktop client for OpenAI API, also a prompt debugging and management tool.<!--en-->
<!--en-->
- [OpenCat](https://opencat.app/)<!--en-->
<!--en-->
    A native desktop ChatGPT client that utilizes your own API key, providing a faster and enhanced chat experience.<!--en-->
<!--en-->
- [MacGPT](https://www.macgpt.com/)<!--en-->
<!--en-->
    A native desktop ChatGPT app, with features like access ChatGPT from anywhere on your Mac with the Global, bring ChatGPT directly into your textfields with MacGPT Inline, and quickly access chatGPT from your menu bar.<!--en-->
<!--en-->
- [AssisChat](https://assischat.com)<!--en-->
<!--en-->
    A ChatGPT API client running on the iOS. It can be used to translate and polish text without leaving other apps by utilizing the system's share feature.<!--en-->
<!--en-->
- [OpenChit](https://apps.apple.com/cn/app/openchit/id6446192123)<!--en-->
<!--en-->
    A ChatGPT API client running on the iOS. With features like voice input and TTS.<!--en-->
<!--en-->
- [MindMac](https://mindmac.app)<!--en-->
<!--en-->
    Effortlessly manage your chats and folders while monitoring costs with intuitive macOS app, powered by ChatGPT API and designed for maximum productivity. Built-in prompt templates, support GPT-3.5 and GPT-4.<!--en-->
  <!--en-->
- [EasyChat AI](https://easychat-ai.app)<!--en-->
<!--en-->
    A native Windows desktop app for using ChatGPT using the latest Windows 11 UI design principles.<!--en-->
<!--en-->
- [WristAssist](https://github.com/DevEmperor/WristAssist)<!--en-->
<!--en-->
  A powerful ChatGPT app for all WearOS devices<!--en-->
<!--en-->
- [SpeakGPT](https://github.com/AndraxDev/speak-gpt)<!--en-->
<!--en-->
    A feature-rich Android ChatGPT client with Material Design 3, supporting GPT-4 Vision, DALL·E image generation, assistant mode, and a community prompts store. Allows users to configure their own API key.<!--en-->
<!--en-->
### Special-purpose<!--en-->
<!--en-->
- [ChatGPT Translator](https://github.com/simpleapples/chatgpt-translator)<!--en-->
<!--en-->
    ChatGPT Translator is an open-source desktop app that allows you to translate text using GPT language model.<!--en-->
<!--en-->
- [OpenAI Translator](https://github.com/yetone/openai-translator)<!--en-->
<!--en-->
    Browser extension and cross-platform desktop application for translation based on ChatGPT API.<!--en-->
    <!--en-->
- [Polyglot](https://github.com/liou666/polyglot) <!--en-->
<!--en-->
    Desktop AI language practice application based on ChatGPT API and Azure TTS<!--en-->
<!--en-->
- [NITM GPT](https://github.com/deskbtm/nitmgpt)<!--en-->
<!--en-->
    An Android application that filters ads, spam, notifications using GPT AI.<!--en-->
<!--en-->
- [CommuniqAI](https://play.google.com/store/apps/details?id=dev.mtc.ga)<!--en-->
<!--en-->
    An Android application that helps you stay in touch by scheduling and automating SMS text messages (and calls and email) while leveraging ChatGPT for message generation.<!--en-->
<!--en-->
- [RewriteBar](https://rewritebar.com/)<!--en-->
<!--en-->
    A MacOS app that allows you to rewrite text using the ChatGPT API. Select text in any app and choose one of the options in the RewriteBar to rewrite the selected text. You can create your own presets for specific workflows.<!--en-->
<!--en-->
<!--en-->
## CLI<!--en-->
<!--en-->
- [ShellGPT](https://github.com/TheR1D/shell_gpt)<!--en-->
<!--en-->
    A command-line productivity tool powered by ChatGPT. Features include generate shell commands, code snippets, comments, and documentation.<!--en-->
<!--en-->
- [bilingual\_book\_maker](https://github.com/yihong0618/bilingual_book_maker)<!--en-->
<!--en-->
    Make bilingual epub books Using AI translate. Original tweet [@yihong0618](https://twitter.com/yihong0618/status/1630948132564631552)<!--en-->
<!--en-->
    There's a web UI at [streamlit](https://goldengrape-bilingual-book-maker-streamlit-app-x7nhof.streamlit.app/), made by the author of this [tweet](https://twitter.com/goldengrape/status/1631549869306572800).<!--en-->
<!--en-->
- [AI Commits](https://github.com/Nutlope/aicommits)<!--en-->
<!--en-->
    A CLI that writes your git commit messages for you with AI.<!--en-->
<!--en-->
- [cz-git](https://github.com/Zhengqbbb/cz-git)<!--en-->
<!--en-->
    A Commitizen CLI and Commitizen adapter generate standardized commit messages with AI. [Recipes/OpenAI](https://cz-git.qbb.sh/recipes/openai)<!--en-->
<!--en-->
- [turbocommit](https://github.com/Sett17/turboCommit)<!--en-->
<!--en-->
    CLI that uses the staged diff and optional message to create Conventional commits.<!--en-->
<!--en-->
- [xiaogpt](https://github.com/yihong0618/xiaogpt)<!--en-->
<!--en-->
    Play ChatGPT with Xiaomi AI Speaker.<!--en-->
<!--en-->
- [AI Vocabulary Builder](https://github.com/piglei/ai-vocabulary-builder)<!--en-->
<!--en-->
    A CLI that helps you build your vocabulary with AI.<!--en-->
<!--en-->
- [verdverm/chatgpt](https://github.com/verdverm/chatgpt)<!--en-->
<!--en-->
    CLI application for working with ChatGPT API interactively or in file based sessions. Supports promt engineering and most configurations.<!--en-->
<!--en-->
- [ai-cli](https://github.com/yufeikang/ai-cli)<!--en-->
<!--en-->
    This CLI tool allows you to easily use chatGPT in the command line. You can chat with it, ask it questions, and get text translations. It also supports rendering Markdown in the terminal.<!--en-->
<!--en-->
- [chatgpt-cli](https://github.com/efJerryYang/chatgpt-cli/)<!--en-->
<!--en-->
    A markdown-supported command-line interface tool that connects to ChatGPT using OpenAI's API key. Commands provided enable you to use this tool much like you would use the official web client. Conversations are saved as JSON format in your machine.<!--en-->
<!--en-->
- [chatGPT-shell-cli](https://github.com/0xacx/chatGPT-shell-cli)<!--en-->
<!--en-->
    A simple, lightweight shell script to use OpenAI's chatGPT and DALL-E from the terminal.<!--en-->
<!--en-->
- [i18n-cli](https://github.com/pandodao/i18n-cli)<!--en-->
<!--en-->
    A command-line interface (CLI) tool that utilizes the OpenAI API to translate locale files based on JSON format.<!--en-->
<!--en-->
- [ChatGPT-for-Translation](https://github.com/Raychanan/ChatGPT-for-Translation)<!--en-->
<!--en-->
    Python tool for translating text files. It provides bilingual translation, multithreading, and automatic handling of excessive request frequency.<!--en-->
<!--en-->
- [subtitle-translator](https://github.com/gnehs/subtitle-translator)<!--en-->
<!--en-->
    A subtitle translation CLI tool based on ChatGPT developed using NodeJS. It also has a Electron GUI version [subtitle-translator-electron](https://github.com/gnehs/subtitle-translator-electron)<!--en-->
<!--en-->
- [Multimedia GPT](https://github.com/fengyuli2002/multimedia-gpt)<!--en-->
<!--en-->
    Multimedia GPT connects OpenAI GPT with vision and audio. Users can now send images, videos, and audio recordings and get a response in both text and image formats.<!--en-->
<!--en-->
- [README-AI](https://github.com/eli64s/README-AI)<!--en-->
<!--en-->
    Command-line tool for crafting aesthetic, structured, and informative README.md files. Powered by OpenAI's language model API.<!--en-->
<!--en-->
- [GPTerminator](https://github.com/AineeJames/ChatGPTerminator)<!--en-->
<!--en-->
    GPTerminator is a python package that provides a convenient way to interact with OpenAI's chat completion and image generation API's using your command line interface.<!--en-->
<!--en-->
- [naming](https://github.com/davidleitw/naming)<!--en-->
<!--en-->
    naming is a command line tool that suggests intuitive and descriptive names for your functions and variables, improving the readability of your code. It uses ChatGPT API to generate program naming suggestions tailored to your code.<!--en-->
    <!--en-->
- [AI Shell](https://github.com/BuilderIO/ai-shell)<!--en-->
<!--en-->
    A CLI that converts natural language to shell commands. Inspired by the Github Copilot X CLI, but open source for everyone.<!--en-->
<!--en-->
- [DoctorGPT](https://github.com/ingyamilmolinar/doctorgpt)<!--en-->
<!--en-->
    DoctorGPT brings GPT into production for application log error diagnosing.<!--en-->
<!--en-->
- [aider](https://github.com/paul-gauthier/aider)<!--en-->
<!--en-->
    aider is a command-line chat tool that allows you to code with GPT-4 in the terminal. Ask GPT for features, improvements, or bug fixes and aider will apply the suggested changes to your source files. Each change is automatically committed to git with a descriptive commit message.<!--en-->
<!--en-->
- [Autohand Code CLI](https://github.com/autohandai/code-cli)<!--en-->
<!--en-->
    A self-evolving autonomous coding agent for the terminal that supports multiple LLM API providers including OpenRouter, Anthropic, OpenAI, and Ollama. It uses a ReAct reasoning pattern, ships with 40+ built-in tools, and integrates with VS Code and Zed editors.<!--en-->
<!--en-->
- [mods](https://github.com/charmbracelet/mods)<!--en-->
<!--en-->
    mods works by reading standard in and prefacing it with a prompt supplied in the mods arguments. Optionally it formats output as Markdown, which you can pipe to markdown rendering CLIs. Example: `mods -f "what are your thoughts on improving this code?" < main.go | glow`<!--en-->
<!--en-->
- [dna-claude-analysis](https://github.com/shmlkv/dna-claude-analysis)<!--en-->
<!--en-->
    Personal genome analysis toolkit that uses LLM APIs to analyze raw DNA data across 17 categories (ancestry, health risks, nutrition, fitness, pharmacogenomics, and more) and generates a terminal-style single-page HTML visualization.<!--en-->
<!--en-->
- [fellow](https://github.com/ManuelZierl/fellow)<!--en-->
<!--en-->
    Fellow is an open-source command-line AI assistant built by developers, for developers. Unlike most AI tools that stop at suggesting code, Fellow goes a step further: It executes tasks on your behalf. It reasons step-by-step, chooses commands from a plugin system, and edits files, generates content, or writes tests — autonomously.<!--en-->
<!--en-->
- [Shep](https://github.com/shep-ai/cli)<!--en-->
<!--en-->
    A multi-session SDLC control center for AI coding agents that orchestrates the complete feature lifecycle — from requirements through testing to merged pull requests — using Claude Code, Cursor CLI, or Gemini, with configurable approval gates and a live web dashboard.<!--en-->
<!--en-->
- [onWatch](https://github.com/onllm-dev/onwatch)<!--en-->
<!--en-->
    Open-source Go CLI that tracks AI API quota usage across 6 providers: OpenAI, Anthropic, GitHub Copilot, Synthetic, Z.ai, and Antigravity. Runs as a background daemon with <50MB RAM, stores data locally in SQLite with zero telemetry, and includes a Material Design 3 web dashboard.<!--en-->
<!--en-->
## Chatbots<!--en-->
<!--en-->
- Telegram<!--en-->
    - [karfly/chatgpt\_telegram\_bot](https://github.com/karfly/chatgpt_telegram_bot): Written in **Python**.<!--en-->
    - [n3d1117/chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot): Written in **Python**.<!--en-->
    - [RainEggplant/chatgpt-telegram-bot](https://github.com/RainEggplant/chatgpt-telegram-bot): Written in **JavaScript**.<!--en-->
    - [leafduo/chatgpt-telegram-bot](https://github.com/leafduo/chatgpt-telegram-bot): Written in **Go**.<!--en-->
    - [TBXark/ChatGPT-Telegram-Workers](https://github.com/TBXark/ChatGPT-Telegram-Workers): This one has been specifically made for **Cloudflare Workers**.<!--en-->
    - [franalgaba/chatgpt-telegram-bot-serverless](https://github.com/franalgaba/chatgpt-telegram-bot-serverless): Free and in AWS serverless bot in **Python**.<!--en-->
    - [iamwavecut/telegram-chatgpt-bot](https://github.com/iamwavecut/telegram-chatgpt-bot): Written in **Go** and comes with the **Dockerfile** for easy setup.<!--en-->
- Slack<!--en-->
    - [myGPTReader](https://github.com/madawei2699/myGPTReader)<!--en-->
<!--en-->
        myGPTReader is a slack bot that can read any webpage, ebook, video(YouTube) or document and summarize it with chatGPT. It can also talk to you via voice using the content in the channel.<!--en-->
- WeChat<!--en-->
    - [zhayujie/chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)<!--en-->
    - [ChatGPT for Wechat](https://chatgpt4wechat.aow.me/)<!--en-->
- Feishu<!--en-->
    - [bestony/ChatGPT-Feishu](https://github.com/bestony/ChatGPT-Feishu)<!--en-->
    - [Leizhenpeng feishu-chatGpt](https://github.com/Leizhenpeng/feishu-chatGpt)<!--en-->
    - [go-zoox/chatgpt-for-chatbot-feishu](https://github.com/go-zoox/chatgpt-for-chatbot-feishu)<!--en-->
    - [key7men/openai-feishu-bot](https://github.com/key7men/openai-feishu-bot)<!--en-->
- DingTalk<!--en-->
    - [eryajf/chatgpt-dingtalk](https://github.com/eryajf/chatgpt-dingtalk): Written in **Go**.<!--en-->
- Teams<!--en-->
    - [formulahendry/chatgpt-teams-bot](https://github.com/formulahendry/chatgpt-teams-bot)<!--en-->
<!--en-->
<!--en-->
## Development<!--en-->
<!--en-->
### Projects<!--en-->
<!--en-->
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)<!--en-->
<!--en-->
    Official examples and guides for using the OpenAI API, including how to embedding long inputs, stream completions, format better inputs and much more.<!--en-->
<!--en-->
- [DocsGPT](https://github.com/arc53/docsgpt)<!--en-->
<!--en-->
    An open-source solution that streamlines the process of finding information in project documentation. With its integration of the powerful GPT models, developers can easily ask questions about a project and receive accurate answers.<!--en-->
<!--en-->
- [Paul Graham GPT](https://github.com/mckaywrigley/paul-graham-gpt)<!--en-->
<!--en-->
    AI-powered search and chat for Paul Graham's essays. This is a excellent demo<!--en-->
    on how to use [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)<!--en-->
    to compress large text data into prompts within the limit of ChatGPT API's 4096 tokens limit.<!--en-->
<!--en-->
    Some insightful tweets about this project and token limitation: [@chuangbo](https://twitter.com/chuangbo/status/1631461656151887873), [@dotey](https://twitter.com/dotey/status/1631779232455053313)<!--en-->
<!--en-->
- [Elasticsearch + GPT3 Answerer](https://github.com/hunkim/es-gpt)<!--en-->
<!--en-->
    Intercepts Elasticsearch results and sends them to GPT3 to provide accurate and relevant answers to your queries.<!--en-->
<!--en-->
<!--en-->
### Tools<!--en-->
<!--en-->
- [LlamaIndex 🦙 \(GPT Index\)](https://github.com/jerryjliu/gpt_index)<!--en-->
<!--en-->
    LlamaIndex (GPT Index) is a project that provides a central interface to connect your LLM's with external data. It has a set of data structures that allow you to index your data for various LLM tasks, and remove concerns over prompt size limitations.<!--en-->
<!--en-->
- [gptcache](https://github.com/zilliztech/gptcache) ⭐️<!--en-->
<!--en-->
    a powerful caching library that can be used to speed up and lower the cost of chat applications that rely on the LLM service. GPT Cache works as a memcache for AIGC applications, similar to how Redis works for traditional applications.<!--en-->
<!--en-->
- [Embedchain](https://github.com/embedchain/embedchain) <!--en-->
<!--en-->
    Framework to create LLM-powered ChatGPT like bots over your dataset<!--en-->
<!--en-->
- [Tiktokenizer](https://tiktokenizer.vercel.app/)<!--en-->
<!--en-->
    Online playground for openai's tiktoken library, calculating the correct number of tokens for a given prompt. Source code: [dqbd/tiktokenizer](https://github.com/dqbd/tiktokenizer)<!--en-->
<!--en-->
- [ChatGPT Wrapper](https://github.com/mmabrouk/chatgpt-wrapper)<!--en-->
<!--en-->
    ChatGPT Wrapper is an open-source unofficial Power CLI, Python API and Flask API that lets you interact programmatically with ChatGPT/GPT4. Several different backends are supported to connect to the ChatGPT models, including browser-based and REST-based options.<!--en-->
<!--en-->
- [OpenAI GPT-3.5 Price Calculator](https://openai.deepakness.com/)<!--en-->
<!--en-->
    Calculate how much it will cost to generate certain number of words by using OpenAI GPT-3.5 API.<!--en-->
<!--en-->
- [OpenAI proxy](https://github.com/egoist/openai-proxy)<!--en-->
<!--en-->
    An OpenAI API reverse proxy that can be deployed on Cloudflare Workers and Vercel Edge.<!--en-->
    Helpful for bypassing network restrictions or IP rate limits.<!--en-->
<!--en-->
<!--en-->
### Articles<!--en-->
<!--en-->
- [I got early access to ChatGPT API and then pushed it to it’s limits. Here’s what you need to know. — Buildt](https://www.buildt.ai/blog/vm3qozd4qfrbbyzukqhynrwm9vb9tq)<!--en-->
- [Thread: Advantages of ChatGPT API compared to ChatGPT](https://twitter.com/novoreorx/status/1631250035852861440)<!--en-->
# Awesome ChatGPT API<!--cn-->
<!--cn-->
精心策划的应用程序和工具列表，不仅使用新的 [ChatGPT API](https://platform.openai.com/docs/api-reference/chat), 还允许用户自行配置 [API keys](https://platform.openai.com/account/api-keys), 允许免费和按需使用自己的配额。<!--cn-->
<!--cn-->
还有一个[开发](#开发)部分，该部分为开发人员提供了一系列项目和文章，以帮助他们更好地进行构建.<!--cn-->
<!--cn-->
请访问网站获取最新消息: [awesome-chatgpt-api.top](https://awesome-chatgpt-api.top/)<!--cn-->
<!--cn-->
> 由 [Reorx](https://reorx.com) 收集整理，欢迎在 Twitter 或通过 PR 向我提交新的作品，但请确保您已经阅读了[提交须知](https://github.com/reorx/awesome-chatgpt-api/issues/21)。<!--cn-->
<!--cn-->
<!--cn-->
**目录表**<!--cn-->
<!--cn-->
- [插件和扩展](#插件和扩展)<!--cn-->
- [Web应用](#web应用)<!--cn-->
  - [类似chatgpt的Web-UI](#类似chatgpt的web-ui)<!--cn-->
  - [特殊用途](#特殊用途)<!--cn-->
- [桌面和移动应用程序](#桌面和移动应用程序)<!--cn-->
  - [类似chatgpt的Web-UI](#类似chatgpt的web-ui)<!--cn-->
  - [特殊用途](#特殊用途)<!--cn-->
- [CLI](#cli)<!--cn-->
- [聊天机器人](#聊天机器人)<!--cn-->
- [开发](#开发)<!--cn-->
  - [项目](#项目)<!--cn-->
  - [工具](#工具)<!--cn-->
  - [文章](#文章)<!--cn-->
<!--cn-->
<!--cn-->
## 插件和扩展<!--cn-->
<!--cn-->
- Chrome扩展<!--cn-->
<!--cn-->
    - [ChatGPT Box](https://github.com/josStorer/chatGPTBox)<!--cn-->
<!--cn-->
        深度ChatGPT集成在您的浏览器。支持在任何页面上随时调用聊天对话框，用右键菜单总结任何页面，独立对话页面，多个API等等。此扩展可在Chrome, Edge, Safari和Firefox上使用。<!--cn-->
<!--cn-->
    - [Glarity](https://glarity.app/)<!--cn-->
<!--cn-->
         总结谷歌搜索结果或YouTube视频与ChatGPT API，也支持雅虎!PubMed, PMC, NewsPicks, Github，日经，必应，谷歌专利。这个扩展还支持ChatGPT Webapp的API，不需要配置。<!--cn-->
<!--cn-->
    - [ChatGPT Sidebar](https://chatgpt-sidebar.com/)<!--cn-->
<!--cn-->
        在任何网页中打开侧边栏，向ChatGPT询问有关页面内容的任何信息。比如解释、翻译、总结或重写。您可以自定义提示以方便访问。这个扩展还支持ChatGPT Webapp的API，不需要配置。<!--cn-->
<!--cn-->
    - [ChatHub](https://chrome.google.com/webstore/detail/chathub-all-in-one-chatbo/iaakpnchhognanibcahlpcplchdfmgma)<!--cn-->
<!--cn-->
        ChatHub是一个一体化聊天机器人客户端，目前支持ChatGPT和新的必应聊天。它允许同时与多个聊天机器人聊天，便于比较它们的答案。源代码:[chathub-dev/chathub](https://github.com/chathub-dev/chathub)<!--cn-->
<!--cn-->
    - [TeamSmart AI](https://www.teamsmart.ai/)<!--cn-->
<!--cn-->
        TeamSmart AI是一款Chrome浏览器扩展，旨在提高您的生产力并增强您的ChatGPT体验。它允许你组建一个人工智能助手团队来帮助你完成日常任务。它可以与您自己的OpenAI API密钥一起使用。<!--cn-->
<!--cn-->
    - [OpenAI Translator](https://github.com/yetone/openai-translator)<!--cn-->
<!--cn-->
        一个Chrome扩展，使用OpenAI API翻译文本，附加功能，如抛光和总结。<!--cn-->
<!--cn-->
    - [ChatGPT » summarize everything!](https://chrome.google.com/webstore/detail/chatgpt-%C2%BB-summarize-every/cbgecfllfhmmnknmamkejadjmnmpfjmp)<!--cn-->
<!--cn-->
        一个Chrome扩展，总结任何网站与ChatGPT。<!--cn-->
        其他功能包括总结任何Youtube视频的成绩单和自定义模板。这个扩展还支持ChatGPT Webapp的API，不需要配置。<!--cn-->
<!--cn-->
- [Emacs](https://www.gnu.org/software/emacs/) Packages<!--cn-->
<!--cn-->
    - [GPTel](https://github.com/karthink/gptel)<!--cn-->
    <!--cn-->
        在Emacs中添加一个主模式，其作用类似于ChatGPT网页。它支持多个聊天会话，可以将任何文本选择发送到ChatGPT API，以获得答案，校对，代码建议等。<!--cn-->
        <!--cn-->
    - [org-ai](https://github.com/rksm/org-ai) <!--cn-->
    <!--cn-->
        在Emacs笔记包org模式中添加一个块，该块可以与ChatGPT聊天并使用dll - e生成图像。它支持语音到文本的输入和文本到语音的读出。<!--cn-->
<!--cn-->
- [Obsidian](https://obsidian.md/) Plugins<!--cn-->
<!--cn-->
    - [Obsidian Text Generator Plugin](https://github.com/nhaouari/obsidian-textgenerator-plugin)<!--cn-->
<!--cn-->
        根据你的黑曜石笔记产生想法、吸引人的标题、摘要、大纲和整个段落。<!--cn-->
<!--cn-->
- [Logseq](https://logseq.com/) Plugins<!--cn-->
<!--cn-->
    - [Logseq Plugin GPT3 OpenAI](https://github.com/briansunter/logseq-plugin-gpt3-openai)<!--cn-->
<!--cn-->
        一个插件使用GPT-3 AI辅助笔记在Logseq。<!--cn-->
<!--cn-->
- [Roam Research](https://roamresearch.com/) Plugins<!--cn-->
<!--cn-->
    - [roam-ai](https://github.com/LayBacc/roam-ai)<!--cn-->
<!--cn-->
        基于当前块生成文本;使用dall-e2生成图像;改述<!--cn-->
<!--cn-->
- [Popclip](https://pilotmoon.com/popclip/) Extensions<!--cn-->
<!--cn-->
    - [ChatGPT — PopClip Extensions](https://pilotmoon.com/popclip/extensions/page/ChatGPT)<!--cn-->
<!--cn-->
        将选定的文本发送到ChatGPT并附加响应。<!--cn-->
<!--cn-->
    - [ChatGPT Proofreader extension for Popclip](https://reorx.com/makers-daily/003-chatgpt-proofreader-extension-popclip/)<!--cn-->
<!--cn-->
        校对选定的文本，并附上增强的结果。<!--cn-->
<!--cn-->
    - [ChatGPT Grammar Check PopClip Extension](https://github.com/hirakujira/ChatGPT-Grammar-Check-PopClip-Extension)<!--cn-->
<!--cn-->
        类似于ChatGPT校对扩展，具有不同的提示符和可下载的包。<!--cn-->
<!--cn-->
- [Drafts](https://getdrafts.com/) Actions<!--cn-->
<!--cn-->
    - [ChatGPT Conversation | Drafts Directory](https://directory.getdrafts.com/a/2HJ)<!--cn-->
<!--cn-->
        在草稿笔记中与ChatGPT进行对话，新的回复将在最后添加。支持声明和修改系统、助手和用户角色消息块。<!--cn-->
<!--cn-->
- [Bob](https://bobtranslate.com/) Plugins<!--cn-->
<!--cn-->
    - [OpenAI Translator Bob Plugin](https://github.com/yetone/bob-plugin-openai-translator)<!--cn-->
<!--cn-->
        基于ChatGPT API的Bob插件，用于文本翻译、文本细化和语法纠正。它有一个派生版本，特别强调校对的任务： [OpenAI Polisher Bob Plugin](https://github.com/yetone/bob-plugin-openai-polisher).<!--cn-->
<!--cn-->
- 苹果快捷键<!--cn-->
<!--cn-->
    - [ChatGPT Siri](https://github.com/Yue-Yang/ChatGPT-Siri)<!--cn-->
<!--cn-->
        快捷键Siri连接ChatGPT 3.5涡轮模型，支持连续对话<!--cn-->
<!--cn-->
    - [Siri Pro](https://www.icloud.com/shortcuts/6889d862918e479693be11fd9a0293b2)<!--cn-->
<!--cn-->
      一个增强的快捷方式基于 **ChatGPT Siri**. 原文: [@DottChen](https://twitter.com/DottChen/status/1631309329684123650)<!--cn-->
<!--cn-->
    - [Share to ChatGPT](https://github.com/reorx/Share-to-ChatGPT-Shortcut)<!--cn-->
<!--cn-->
       分享到ChatGPT是一个苹果快捷方式，允许用户分享突出显示的文本到ChatGPT，同时还包括个性化的提示，响应消息将自动复制到用户的剪贴板。<!--cn-->
<!--cn-->
- [Keyboard Maestro](https://www.keyboardmaestro.com/) Macros<!--cn-->
<!--cn-->
    - [Copy to Ask ChatGPT](https://blog.retompi.com/post/use-chatgpt-api/#keyboard-maestro)<!--cn-->
<!--cn-->
        选择并复制文本以使用键盘快捷键询问ChatGPT. [下载链接](https://p15.p3.n0.cdn.getcloudapp.com/items/geuEZvwA/aeed10cb-a35d-404f-a17f-da1d46c9c9c7.kmmacros)<!--cn-->
<!--cn-->
    - [我的六個專屬 ChatGPT 助手](https://pinchlime.com/newsletters/my-six-chatgpt-assistants/)<!--cn-->
<!--cn-->
- GitHub App<!--cn-->
<!--cn-->
    - [CR.GPT](https://github.com/apps/cr-gpt)<!--cn-->
<!--cn-->
        由ChatGPT驱动的代码审查机器人<!--cn-->
<!--cn-->
- [LaunchBar](https://www.obdev.at/products/launchbar/) Actions<!--cn-->
<!--cn-->
    - [ChipiChat](https://github.com/quinncomendant/ChipiChat.lbaction)<!--cn-->
<!--cn-->
        与ChatGPT API交互的LaunchBar操作。响应直接在LaunchBar中接收，可以通过Quick Look浏览、打开、预览、插入或发送到另一个操作。保存会话历史记录以供参考。ChatGPT系统消息可以通过角色进行配置。<!--cn-->
<!--cn-->
<!--cn-->
## web应用<!--cn-->
<!--cn-->
<!--cn-->
### 类似chatgpt的web-ui<!--cn-->
<!--cn-->
- [ChatKit](https://chatkit.app/)<!--cn-->
<!--cn-->
    一个轻量级的ChatGPT Web UI，允许设置url作为对话的上下文。<!--cn-->
<!--cn-->
- [TypingMind](https://www.typingmind.com/)<!--cn-->
<!--cn-->
    一个更好的用户界面ChatGPT，与增强的功能，如快速响应，聊天搜索，集成，提示库等。<!--cn-->
<!--cn-->
- [ChatGPT Next Web](https://github.com/Yidadaa/ChatGPT-Next-Web)<img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--cn-->
<!--cn-->
    一键部署设计良好的ChatGPT web UI在Vercel。界面经过抛光，支持响应式设计、暗模式和PWA。具有内置提示库，对话压缩和将聊天记录导出为Markdown文件等功能。<!--cn-->
<!--cn-->
- [Chatbot UI](https://github.com/mckaywrigley/chatbot-ui) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--cn-->
<!--cn-->
    Chatbot UI是OpenAI聊天模型的高级聊天机器人套件，基于Chatbot UI Lite，使用Next.js、TypeScript和顺风CSS。<!--cn-->
<!--cn-->
- [Chat with GPT](https://chatwithgpt.netlify.app) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--cn-->
<!--cn-->
    一个开源的ChatGPT web UI与附加功能，如TTS。源代码: [cogentapps/chat-with-gpt](https://github.com/cogentapps/chat-with-gpt)<!--cn-->
<!--cn-->
- [ChatGPT Web](https://github.com/Chanzhaoyu/chatgpt-web) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--cn-->
<!--cn-->
    一个使用ve3和Express构建的ChatGPT web应用程序演示。<!--cn-->
<!--cn-->
- [Next.js ChatGPT](https://github.com/enricoros/nextjs-chatgpt-app) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--cn-->
<!--cn-->
    这是一个使用Next.js和TypeScript构建的响应式聊天web应用程序，由OpenAI的GPT-4提供支持，具有聊天流，代码高亮显示，代码执行，开发预设等功能。<!--cn-->
<!--cn-->
- [ChatGPT-API Demo](https://github.com/ddiu8081/chatgpt-demo) <img src="https://img.shields.io/badge/-self--hosted-1adc61" /><!--cn-->
<!--cn-->
    一个用Astro和TypeScript构建的ChatGPT web应用演示。<!--cn-->
<!--cn-->
    相关项目: [ChatGPT-Vercel](https://github.com/ourongxing/chatgpt-vercel) is another ChatGPT web app based on ddiu8081/chatgpt-demo, specifically made for deploying on Vercel.<!--cn-->
<!--cn-->
<!--cn-->
### 特殊用途<!--cn-->
<!--cn-->
- [ChatFiles](https://github.com/guangzhengli/ChatFiles)<!--cn-->
<!--cn-->
    一个可以上传文件并与之对话的网络应用程序。<!--cn-->
    该存储库使用jerryjliu/llama_index拆分大文本，基于mckaywrigley/chatbot-ui，并受到madawei2699/myGPTReader的启发<!--cn-->
<!--cn-->
- [ChatPDF](https://www.chatpdf.com/)<!--cn-->
<!--cn-->
    ChatPDF是一种创新的工具，它允许用户与他们的PDF文件进行口头交流，从而更容易从手册、法律合同和研究论文等大型文档中提取信息。<!--cn-->
<!--cn-->
- [OpenAI Translator](https://translator.lance.moe/)<!--cn-->
<!--cn-->
    一款使用OpenAI GPT-3进行语言翻译的翻译应用程序。它是一个PWA，可以安装在您的手机或桌面上。源代码: [LanceMoe/openai-translator](https://github.com/LanceMoe/openai-translator)<!--cn-->
<!--cn-->
- [BiliGPT](https://b.jimmylv.cn/)<!--cn-->
<!--cn-->
    哔哩哔哩字幕视频一键汇总。源代码: [JimmyLv/BiliGPT](https://github.com/JimmyLv/BiliGPT)<!--cn-->
<!--cn-->
- [ResearchGPT](https://researchgpt.ue.r.appspot.com/)<!--cn-->
<!--cn-->
    这是一个flask应用程序，提供了一个界面，可以与研究论文进行对话。<!--cn-->
    源代码: [mukulpatnaik/ResearchGPT](https://github.com/mukulpatnaik/researchgpt).<!--cn-->
<!--cn-->
    作者探索了从与原始tweet中的提示密切匹配的文本中派生的向量嵌入的利用： [@mukul0x](https://twitter.com/mukul0x/status/1625673579399446529)<!--cn-->
<!--cn-->
- [ChatGPT Academic](https://github.com/binary-husky/chatgpt_academic)<!--cn-->
<!--cn-->
    专门针对科研工作的ChatGPT应用，针对学术论文校对体验进行优化，支持自定义快捷按钮，支持降价表显示，Tex公式双显示，改进代码显示功能，增加本地Python项目分析/自分析功能。<!--cn-->
<!--cn-->
- [AI Subtitle Translator](https://ai.cgsv.top/)<!--cn-->
<!--cn-->
    使用GPT-3.5 API翻译本地或Youtube/Bilibili字幕。源代码: [AI Subtitle](https://github.com/cgsvv/AISubtitle)<!--cn-->
<!--cn-->
- [Visual ChatGPT](https://github.com/microsoft/visual-chatgpt)<!--cn-->
    <!--cn-->
    Visual ChatGPT是一个web应用程序，它将ChatGPT和一系列Visual Foundation Models连接起来，以便在聊天过程中发送和接收图像。<!--cn-->
<!--cn-->
<!--cn-->
## 桌面和移动应用程序<!--cn-->
<!--cn-->
<!--cn-->
### 类似chatgpt的web-ui<!--cn-->
<!--cn-->
- [ChatBox](https://github.com/Bin-Huang/chatbox)<!--cn-->
<!--cn-->
    ChatBox是OpenAI API的跨平台桌面客户端，也是一个即时调试和管理工具。<!--cn-->
<!--cn-->
- [OpenCat](https://opencat.app/)<!--cn-->
<!--cn-->
    本机桌面ChatGPT客户端，利用您自己的API密钥，提供更快和增强的聊天体验。<!--cn-->
<!--cn-->
- [MacGPT](https://www.macgpt.com/)<!--cn-->
<!--cn-->
    一个本地桌面ChatGPT应用程序，与功能，如访问ChatGPT从任何地方在您的Mac与全局，把ChatGPT直接到您的文本字段与MacGPT内联，并快速访问ChatGPT从您的菜单栏。<!--cn-->
<!--cn-->
- [AssisChat](https://assischat.com)<!--cn-->
<!--cn-->
    一个在iOS上运行的ChatGPT API客户端。它可以用来翻译和润色文本，而无需离开其他应用程序，利用系统的共享功能。<!--cn-->
<!--cn-->
- [OpenChit](https://apps.apple.com/cn/app/openchit/id6446192123)<!--cn-->
<!--cn-->
    一个在iOS上运行的ChatGPT API客户端。有语音输入和TTS等功能。<!--cn-->
<!--cn-->
- [MindMac](https://mindmac.app)<!--cn-->
<!--cn-->
    毫不费力地管理您的聊天和文件夹，同时监控成本与直观的macOS应用程序，由ChatGPT API供电，并设计为最大的生产力。内置提示模板，支持GPT-3.5和GPT-4。<!--cn-->
<!--cn-->
### Special-purpose<!--cn-->
<!--cn-->
- [ChatGPT Translator](https://github.com/simpleapples/chatgpt-translator)<!--cn-->
<!--cn-->
    ChatGPT Translator是一个开源的桌面应用程序，允许您使用GPT语言模型翻译文本。<!--cn-->
<!--cn-->
- [OpenAI Translator](https://github.com/yetone/openai-translator)<!--cn-->
<!--cn-->
    基于ChatGPT API的浏览器扩展和跨平台桌面翻译应用程序。<!--cn-->
    <!--cn-->
- [Polyglot](https://github.com/liou666/polyglot) <!--cn-->
<!--cn-->
    基于ChatGPT API和Azure TTS的桌面AI语言实践应用<!--cn-->
<!--cn-->
- [NITM GPT](https://github.com/deskbtm/nitmgpt)<!--cn-->
<!--cn-->
    一个Android应用程序，过滤广告，垃圾邮件，通知使用GPT AI。<!--cn-->
<!--cn-->
- [CommuniqAI](https://play.google.com/store/apps/details?id=dev.mtc.ga)<!--cn-->
<!--cn-->
    这是一个Android应用程序，通过调度和自动发送SMS文本消息(以及电话和电子邮件)来帮助您保持联系，同时利用ChatGPT生成消息。<!--cn-->
<!--cn-->
<!--cn-->
## CLI<!--cn-->
<!--cn-->
- [ShellGPT](https://github.com/TheR1D/shell_gpt)<!--cn-->
<!--cn-->
    一个由ChatGPT提供支持的命令行生产力工具。功能包括生成shell命令、代码片段、注释和文档。<!--cn-->
<!--cn-->
- [bilingual\_book\_maker](https://github.com/yihong0618/bilingual_book_maker)<!--cn-->
<!--cn-->
    使用AI翻译制作双语电子书。原创推文 [@yihong0618](https://twitter.com/yihong0618/status/1630948132564631552)<!--cn-->
<!--cn-->
    在[streamlit](https://goldengrape-bilingual-book-maker-streamlit-app-x7nhof.streamlit.app/)上有一个web UI，由[tweet](https://twitter.com/goldengrape/status/1631549869306572800)的作者制作。<!--cn-->
<!--cn-->
- [AI Commits](https://github.com/Nutlope/aicommits)<!--cn-->
<!--cn-->
    一个用AI为你写git提交消息的CLI。<!--cn-->
<!--cn-->
- [cz-git](https://github.com/Zhengqbbb/cz-git)<!--cn-->
<!--cn-->
    commizen CLI和commizen适配器使用AI生成标准化的提交消息。 [Recipes/OpenAI](https://cz-git.qbb.sh/recipes/openai)<!--cn-->
<!--cn-->
- [turbocommit](https://github.com/Sett17/turboCommit)<!--cn-->
<!--cn-->
    使用阶段性diff和可选消息创建常规提交的CLI。<!--cn-->
<!--cn-->
- [xiaogpt](https://github.com/yihong0618/xiaogpt)<!--cn-->
<!--cn-->
    与小米AI扬声器一起玩ChatGPT。<!--cn-->
<!--cn-->
- [AI Vocabulary Builder](https://github.com/piglei/ai-vocabulary-builder)<!--cn-->
<!--cn-->
   帮助您使用AI构建词汇表的CLI。<!--cn-->
<!--cn-->
- [verdverm/chatgpt](https://github.com/verdverm/chatgpt)<!--cn-->
<!--cn-->
    用于与ChatGPT API交互或在基于文件的会话中工作的CLI应用程序。支持提示工程和大多数配置。<!--cn-->
<!--cn-->
- [ai-cli](https://github.com/yufeikang/ai-cli)<!--cn-->
<!--cn-->
    该命令行工具允许您在命令行中轻松使用chatGPT。你可以和它聊天，向它提问，并获得文本翻译。它还支持在终端中呈现Markdown。<!--cn-->
<!--cn-->
- [chatgpt-cli](https://github.com/efJerryYang/chatgpt-cli/)<!--cn-->
<!--cn-->
    一个支持markdown的命令行接口工具，使用OpenAI的API密钥连接到ChatGPT。所提供的命令使您能够像使用官方web客户端一样使用此工具。对话以JSON格式保存在您的机器中。<!--cn-->
<!--cn-->
- [chatGPT-shell-cli](https://github.com/0xacx/chatGPT-shell-cli)<!--cn-->
<!--cn-->
    一个简单的，轻量级的shell脚本，从终端使用OpenAI的chatGPT和dll - e。<!--cn-->
<!--cn-->
- [i18n-cli](https://github.com/pandodao/i18n-cli)<!--cn-->
<!--cn-->
   一个命令行接口(CLI)工具，它利用OpenAI API来翻译基于JSON格式的语言环境文件。<!--cn-->
<!--cn-->
- [ChatGPT-for-Translation](https://github.com/Raychanan/ChatGPT-for-Translation)<!--cn-->
<!--cn-->
    翻译文本文件的Python工具。它提供双语翻译、多线程和自动处理过多的请求频率。<!--cn-->
<!--cn-->
- [subtitle-translator](https://github.com/gnehs/subtitle-translator)<!--cn-->
<!--cn-->
    基于ChatGPT的字幕翻译CLI工具，使用NodeJS开发。它也有一个GUI版本 [subtitle-translator-electron](https://github.com/gnehs/subtitle-translator-electron)<!--cn-->
<!--cn-->
- [Multimedia GPT](https://github.com/fengyuli2002/multimedia-gpt)<!--cn-->
<!--cn-->
    多媒体GPT连接OpenAI GPT与视觉和音频。用户现在可以发送图像、视频和录音，并获得文本和图像格式的回复。<!--cn-->
<!--cn-->
- [README-AI](https://github.com/eli64s/README-AI)<!--cn-->
<!--cn-->
   用于制作美观、结构化和信息丰富的README的命令行工具。md文件。由OpenAI语言模型API提供支持。<!--cn-->
<!--cn-->
- [GPTerminator](https://github.com/AineeJames/ChatGPTerminator)<!--cn-->
<!--cn-->
   GPTerminator是一个python包，它提供了一种使用命令行接口与OpenAI的聊天完成和图像生成API进行交互的方便方法。<!--cn-->
<!--cn-->
- [naming](https://github.com/davidleitw/naming)<!--cn-->
<!--cn-->
    naming 是一个命令行工具，它为函数和变量建议直观和描述性的名称，从而提高代码的可读性。它使用ChatGPT API生成适合您代码的程序命名建议。<!--cn-->
    <!--cn-->
- [AI Shell](https://github.com/BuilderIO/ai-shell)<!--cn-->
<!--cn-->
    将自然语言转换为shell命令的CLI。受Github Copilot X CLI的启发，对所有人开放源代码。<!--cn-->
<!--cn-->
- [DoctorGPT](https://github.com/ingyamilmolinar/doctorgpt)<!--cn-->
<!--cn-->
    DoctorGPT将GPT引入生产环境，用于应用程序日志错误诊断。<!--cn-->
<!--cn-->
- [aider](https://github.com/paul-gauthier/aider)<!--cn-->
<!--cn-->
    aider是一个命令行聊天工具，允许您在终端中使用GPT-4进行编码。向GPT询问特性、改进或错误修复，aider将把建议的更改应用到源文件中。每个更改都会自动提交到git，并附带一个描述性的提交消息。<!--cn-->
    <!--cn-->
- [mods](https://github.com/charmbracelet/mods)<!--cn-->
<!--cn-->
   Mods的工作原理是通过读取标准，并在Mods参数中提供提示符。可选地，它将输出格式化为Markdown，您可以通过管道将其传输到Markdown呈现cli。例如: `mods -f "what are your thoughts on improving this code?" < main.go | glow`<!--cn-->
<!--cn-->
## 聊天机器人<!--cn-->
<!--cn-->
- 电报<!--cn-->
    - [karfly/chatgpt\_telegram\_bot](https://github.com/karfly/chatgpt_telegram_bot): Written in **Python**.<!--cn-->
    - [n3d1117/chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot): Written in **Python**.<!--cn-->
    - [RainEggplant/chatgpt-telegram-bot](https://github.com/RainEggplant/chatgpt-telegram-bot): Written in **JavaScript**.<!--cn-->
    - [leafduo/chatgpt-telegram-bot](https://github.com/leafduo/chatgpt-telegram-bot): Written in **Go**.<!--cn-->
    - [TBXark/ChatGPT-Telegram-Workers](https://github.com/TBXark/ChatGPT-Telegram-Workers): This one has been specifically made for **Cloudflare Workers**.<!--cn-->
    - [franalgaba/chatgpt-telegram-bot-serverless](https://github.com/franalgaba/chatgpt-telegram-bot-serverless): Free and in AWS serverless bot in **Python**.<!--cn-->
    - [iamwavecut/telegram-chatgpt-bot](https://github.com/iamwavecut/telegram-chatgpt-bot): Written in **Go** and comes with the **Dockerfile** for easy setup.<!--cn-->
- Slack<!--cn-->
    - [myGPTReader](https://github.com/madawei2699/myGPTReader)<!--cn-->
<!--cn-->
        myGPTReader是一个slack机器人，可以阅读任何网页，电子书，视频(YouTube)或文档，并与chatGPT总结。它还可以使用频道中的内容通过语音与您交谈。<!--cn-->
- 微信<!--cn-->
    - [zhayujie/chatgpt-on-wechat](https://github.com/zhayujie/chatgpt-on-wechat)<!--cn-->
    - [ChatGPT for Wechat](https://chatgpt4wechat.aow.me/)<!--cn-->
- 飞书<!--cn-->
    - [bestony/ChatGPT-Feishu](https://github.com/bestony/ChatGPT-Feishu)<!--cn-->
    - [Leizhenpeng feishu-chatGpt](https://github.com/Leizhenpeng/feishu-chatGpt)<!--cn-->
    - [go-zoox/chatgpt-for-chatbot-feishu](https://github.com/go-zoox/chatgpt-for-chatbot-feishu)<!--cn-->
    - [key7men/openai-feishu-bot](https://github.com/key7men/openai-feishu-bot)<!--cn-->
- 钉钉<!--cn-->
    - [eryajf/chatgpt-dingtalk](https://github.com/eryajf/chatgpt-dingtalk): Written in **Go**.<!--cn-->
- Teams<!--cn-->
    - [formulahendry/chatgpt-teams-bot](https://github.com/formulahendry/chatgpt-teams-bot)<!--cn-->
<!--cn-->
<!--cn-->
## 开发<!--cn-->
<!--cn-->
### 项目<!--cn-->
<!--cn-->
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)<!--cn-->
<!--cn-->
    官方示例和指南使用OpenAI API，包括如何嵌入长输入，流完成，格式更好的输入和更多。<!--cn-->
    <!--cn-->
- [DocsGPT](https://github.com/arc53/docsgpt)<!--cn-->
<!--cn-->
     一个开源解决方案，简化了在项目文档中查找信息的过程。通过集成强大的GPT模型，开发人员可以轻松地提出有关项目的问题并获得准确的答案。<!--cn-->
<!--cn-->
- [Paul Graham GPT](https://github.com/mckaywrigley/paul-graham-gpt)<!--cn-->
<!--cn-->
    人工智能搜索和聊天Paul Graham的文章。这是一个很好的演示，关于如何使用[OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)<!--cn-->
    在ChatGPT API的4096个令牌限制范围内将大型文本数据压缩为提示<!--cn-->
<!--cn-->
    关于这个项目和令牌限制的一些有见地的推文: [@chuangbo](https://twitter.com/chuangbo/status/1631461656151887873), [@dotey](https://twitter.com/dotey/status/1631779232455053313)<!--cn-->
<!--cn-->
- [Elasticsearch + GPT3 Answerer](https://github.com/hunkim/es-gpt)<!--cn-->
<!--cn-->
    拦截Elasticsearch结果并将其发送到GPT3，为您的查询提供准确和相关的答案。<!--cn-->
<!--cn-->
<!--cn-->
### 工具<!--cn-->
<!--cn-->
- [LlamaIndex 🦙 \(GPT Index\)](https://github.com/jerryjliu/gpt_index)<!--cn-->
<!--cn-->
    LlamaIndex (GPT Index)是一个项目，它提供了一个中央接口来连接您的LLM与外部数据。它有一组数据结构，允许您为各种LLM任务索引数据，并消除对提示大小限制的担忧。<!--cn-->
<!--cn-->
- [gptcache](https://github.com/zilliztech/gptcache) ⭐️<!--cn-->
<!--cn-->
    一个强大的缓存库，可以用来加速和降低依赖LLM服务的聊天应用程序的成本。GPT Cache作为AIGC应用程序的memcache，类似于Redis为传统应用程序工作的方式。<!--cn-->
<!--cn-->
- [Embedchain](https://github.com/embedchain/embedchain) <!--cn-->
<!--cn-->
    用于在数据集上创建类似机器人的由 LLM 支持的 ChatGPT 的框架<!--cn-->
<!--cn-->
- [Tiktokenizer](https://tiktokenizer.vercel.app/)<!--cn-->
<!--cn-->
    openai的tiktoken库的在线游乐场，为给定的提示计算正确的令牌数量。源代码: [dqbd/tiktokenizer](https://github.com/dqbd/tiktokenizer)<!--cn-->
<!--cn-->
- [ChatGPT Wrapper](https://github.com/mmabrouk/chatgpt-wrapper)<!--cn-->
<!--cn-->
    ChatGPT Wrapper是一个开源的非官方的Power CLI, Python API和Flask API，允许您以编程方式与ChatGPT/GPT4进行交互。支持几种不同的后端连接到ChatGPT模型，包括基于浏览器和基于rest的选项。<!--cn-->
<!--cn-->
- [OpenAI GPT-3.5 Price Calculator](https://openai.deepakness.com/)<!--cn-->
<!--cn-->
    计算使用OpenAI GPT-3.5 API生成一定数量的单词需要花费多少。<!--cn-->
<!--cn-->
- [OpenAI proxy](https://github.com/egoist/openai-proxy)<!--cn-->
<!--cn-->
    OpenAI API反向代理，可以部署在Cloudflare Workers和Vercel Edge上。有助于绕过网络限制或IP速率限制。.<!--cn-->
<!--cn-->
<!--cn-->
### 文章<!--cn-->
<!--cn-->
- [I got early access to ChatGPT API and then pushed it to it’s limits. Here’s what you need to know. — Buildt](https://www.buildt.ai/blog/vm3qozd4qfrbbyzukqhynrwm9vb9tq)<!--cn-->
- [Thread: Advantages of ChatGPT API compared to ChatGPT](https://twitter.com/novoreorx/status/1631250035852861440)<!--cn-->

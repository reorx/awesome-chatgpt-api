---
title: "Updates for 2023-05-24"
date: 2023-05-24
summary: "The mods project has been updated to allow for formatted output in Markdown. It prompts users for input and can be piped to other CLIs for rendering."
---
Here's the projects added or updated today:

- [mods](https://github.com/charmbracelet/mods)
    
    mods works by reading standard in and prefacing it with a prompt supplied in the mods arguments. Optionally it formats output as Markdown, which you can pipe to markdown rendering CLIs. Example: `mods -f "what are your thoughts on improving this code?" < main.go | glow`

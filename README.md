# Opinionated Markdown to PDF converter using Pandoc

It uses slightly modified formatting and styling, and includes a python parser in the workflow for adapting Obsidian markdown wikilink format to standard markdown format.

TODO:
- [ ] Add support for merging multiple markdown files into a single PDF.

## Installing on Windows

[Download pandoc](https://pandoc.org/installing.html)

[Download Miktex (latex engine I use with pandoc)](https://miktex.org/download)

[Download pandoc-crossref](https://github.com/lierdakil/pandoc-crossref)

Add pandoc and pandoc-crossref to your PATH.

The command that generates latex-formatted PDF from a Obsidian markdown file is in `launch.json`.

If editing with Obsidian, the support for images embedded directly via Obsidian is given by my custom `parse.py`, which processes each Markdown file before being fed to `pandoc`, and it adapts the custom Obsidian wikilink format to standard Markdown format. **Make sure that you configured Obsidian to save all images into the same folder**, and specify that folder in the `parse.py` script.

If using VSCode, you can use the run configuration inside `launch.json` to run the whole workflow on the currently opened Markdown file.
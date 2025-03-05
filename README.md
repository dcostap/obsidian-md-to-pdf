# Opinionated Markdown to PDF converter using Pandoc

It uses slightly modified formatting and styling.

## Usage

Run the .bat file providing the input markdown file path. 

If using VSCode, you can use the run configuration inside `launch.json` to quickly run the .bat on the currently opened Markdown file.

If editing markdown with Obsidian, change the setting to not use wiki-links.

TODO:
- [ ] Add support for merging multiple markdown files into a single PDF.

## Installing on Windows

[Download pandoc](https://pandoc.org/installing.html)

[Download Miktex (LaTeX engine I use with pandoc)](https://miktex.org/download)

[Download pandoc-crossref (for automatic image references links and index counting)](https://github.com/lierdakil/pandoc-crossref)

Add pandoc and pandoc-crossref executables to your PATH.

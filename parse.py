#!/usr/bin/env python3
import os
import re
import sys

OBSIDIAN_APPENDED_FILES_FOLDER = "imgs"

def parse_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_code_block = False
    parsed_lines = []

    codeblock_pattern = re.compile(r'^\s*```')
    italic_pattern = re.compile(r'_([^_]+)_')  # captures text between single underscores

    for line in lines:
        # Toggle code block tracking
        if codeblock_pattern.match(line):
            in_code_block = not in_code_block
            parsed_lines.append(line)
            continue

        if not in_code_block:
            # Insert a blank line before an Obsidian image link if the previous line isn't blank
            if re.search(r'!\[\[.*?\]\]', line) and parsed_lines and parsed_lines[-1].strip() != "":
                parsed_lines.append('\n')

            # 1) Obsidian image links: ![[img.png]] -> ![img.png](imgs/img.png)
            line = re.sub(r'!\[\[(.*?)\]\]', r'![\1](imgs/\1)', line)

            # 2) Wiki links: [[link]] -> [link](imgs/link)
            line = re.sub(r'\[\[(.*?)\]\]', r'[\1](imgs/\1)', line)

            # 3) Remove empty links
            line = re.sub(r'\[\]\(\)', '', line)

            # 4) Escape backslashes
            line = line.replace('\\', '\\\\')

            # 5) Convert italics `_text_` -> `*text*`
            line = italic_pattern.sub(r'*\1*', line)

            # 6) Escape leftover underscores
            line = line.replace('_', r'\_')

        parsed_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(parsed_lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse.py <input_markdown_file>")
        sys.exit(1)

    input_md = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(input_md))[0]

    if os.path.splitext(os.path.basename(input_md))[1] != ".md":
        print("ERROR: Input file must be a .md file.")
        sys.exit(1)

    os.makedirs('build', exist_ok=True)
    output_md = f"build/{base_name}_parsed.md"
    parse_markdown(input_md, output_md)
    print(f"Parsed Markdown generated: {output_md}")

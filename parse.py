#!/usr/bin/env python3
import os
import re
import sys

OBSIDIAN_APPENDED_FILES_FOLDER = "imgs"

def parse_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    parsed_lines = []

    for line in lines:
        # 1) Obsidian image links with aliases: ![[img.png|Alias]] -> ![Alias](imgs/img.png)
        line = re.sub(r'!\[\[(.*?)\|(.*?)\]\]', r'![\2](imgs/\1)', line)
        
        # 2) Regular Obsidian image links: ![[img.png]] -> ![img.png](imgs/img.png)
        line = re.sub(r'!\[\[(.*?)\]\]', r'![\1](imgs/\1)', line)

        # 3) Wiki links with aliases: [[link|Alias]] -> [Alias](imgs/link)
        line = re.sub(r'\[\[(.*?)\|(.*?)\]\]', r'[\2](imgs/\1)', line)
        
        # 4) Regular Wiki links: [[link]] -> [link](imgs/link)
        line = re.sub(r'\[\[(.*?)\]\]', r'[\1](imgs/\1)', line)

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

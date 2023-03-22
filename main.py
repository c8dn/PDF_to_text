import PyPDF2
import re

watermark_regex = re.compile(r'^\[\d+\]$')

with open('input.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page].extract_text()
        if watermark_regex.match(page_text.strip()):
            continue
        text += page_text

lines = [line.strip() for line in text.split('\n')]
lines = [line for line in lines if line and not watermark_regex.match(line)]
lines.sort()

sections = {}
for line in lines:
    first_char = line[0].upper()
    if first_char not in sections:
        sections[first_char] = []
    sections[first_char].append(line)

with open('output.txt', 'w') as file:
    for header, lines in sorted(sections.items()):
        file.write(f"{header}:\n")
        for line in lines:
            file.write(f"  {line}\n")

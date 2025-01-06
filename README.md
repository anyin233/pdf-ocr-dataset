# Script to Generate Dataset for PDF OCR

## Lorem Markdown
Get random Markdown file from [Lorem Markdown](https://jaspervdj.be/lorem-markdownum/), and render it to PDF and HTML.

### How to use

1. Install Dependences

```bash
pip install xhtml2pdf tqdm mistune
```

2. Run the script

```bash
python lorem_markdown/main.py -o <output_dir> -n <num of markdown>
```

Optional Arguments:
- max_b: max number of blocks of markdown file
- min_b: min number of blocks of markdown file

3. Got your file

Structure:
```
<output_dir>
|--0
   |--0.md
   |--0.pdf
   |--0.html
|--1
   |--1.md
   |--1.pdf
   |--1.html
|-- ....
```

## Mathgen Latex
Generate random fake mathematics papers with [Mathgen](https://github.com/neldredge/mathgen) and render it to Markdown and PDF.

### Prerequisites

- pandoc
- pandoc-crossref
- mathgen

### How to use

TODO

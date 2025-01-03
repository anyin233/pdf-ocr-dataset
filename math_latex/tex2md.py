import subprocess
import os
import argparse
import shutil

def parse_arg():
  parser = argparse.ArgumentParser(description="Generate a new file")
  parser.add_argument("-i", "--input", help="Input file path", required=True)
  parser.add_argument("-o", "--output", help="Output file path", required=True)
  return parser.parse_args()


def main(args):
  ipath = args.input
  opath = args.output
  if not os.path.exists(ipath):
    print(f"Input file {ipath} does not exist")
    return
  
  if os.path.exists(opath):
    print(f"Output file {opath} already exists")
    shutil.rmtree(opath, ignore_errors=True)
  
  os.makedirs(opath)
  

  # find all tex file under ipath
  tex_files = []
  for root, _, files in os.walk(ipath):
    for f in files:
      if f.endswith(".tex"):
        tex_files.append(os.path.join(root, f))
  
  # use pandoc convert tex to md
  for tex_file in tex_files:
    # Generate md files into output directory preserving relative paths
    rel_path = os.path.relpath(tex_file, ipath)
    md_file = os.path.join(opath, os.path.splitext(rel_path)[0] + ".md")
    temp_docx_file = os.path.join(opath, os.path.splitext(rel_path)[0] + ".docx")
    bib_path = os.path.join(os.path.dirname(tex_file), "scigenbibfile.bib")
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(md_file), exist_ok=True)
    
    print(f"Converting {tex_file} to {md_file}")
    subprocess.run(["pandoc", tex_file, "--filter", "pandoc-crossref", "--biblatex", "--citeproc", "--bibliography", bib_path, "-M reference-section-title=Reference", "-V biblio-title=Reference", "-f", "latex", "-t", "docx", "-o", temp_docx_file])
    subprocess.run(["pandoc", temp_docx_file, "--filter", "pandoc-crossref", "-f", "docx", "-t", "markdown", "-o", md_file])
    # Remove temporary docx file
    # os.remove(temp_docx_file)
  
    # Add newline before $$ while preserving the content
    with open(md_file, "r") as f:
      content = f.read()
    
    modified_content = content.replace("$$", "\n$$")
    # print(modified_content)
    # return
    
    with open(md_file, "w") as f:
      f.write(modified_content)
    
    # Copy tex source and pdf file to output directory
    shutil.copy(tex_file, os.path.join(opath, os.path.relpath(tex_file, ipath)))
    pdf_file = os.path.splitext(tex_file)[0] + ".pdf"
    if os.path.exists(pdf_file):
      shutil.copy(pdf_file, os.path.join(opath, os.path.relpath(pdf_file, ipath)))

if __name__ == "__main__":
  args = parse_arg()
  main(args)
import requests
import mistune
from xhtml2pdf import pisa
import argparse
import os
import shutil
import random
from tqdm import tqdm

ENDPOINT_URL = "https://jaspervdj.be/lorem-markdownum/markdown.txt?num-blocks={nblocks}"

pisa.showLogging()

parser = argparse.ArgumentParser()
parser.add_argument("-o", help="Output directory", default="output")
parser.add_argument("-n", help="Count of files to generate", default=1, type=int)
parser.add_argument("--max_b", help="Number of blocks (max)", default=50, type=int)
parser.add_argument("--min_b", help="Number of blocks (min)", default=10, type=int)
args = parser.parse_args()

print("Output directory: ", args.o)
checkpoint = 0
if os.path.exists(args.o):
    # find the last index
    for root, dirs, files in os.walk(args.o):
        for name in dirs:
            try:
                index = int(name)
                if index > checkpoint:
                    checkpoint = index
            except:
                pass
  
# os.makedirs(args.o)
    
for index in tqdm(range(args.n)):
  if index < checkpoint:
        continue
  n_blocks = random.randint(args.min_b, args.max_b) 
  markdown_text = requests.get(ENDPOINT_URL.format(nblocks=n_blocks)).text
  markdown_html = mistune.markdown(markdown_text)
  
  output_path = os.path.join(args.o, str(index))
  os.makedirs(output_path, exist_ok=True)
  with open(os.path.join(output_path, "{}.md".format(index)), "w") as output_file:
      output_file.write(markdown_text)
      
  with open(os.path.join(output_path, "{}.html".format(index)), "w") as output_file:
      output_file.write(markdown_html)

  with open(os.path.join(output_path, "{}.pdf".format(index)), "w+b") as output_file:
      stat = pisa.CreatePDF(markdown_html, dest=output_file)
      
      if stat.err:
          print(stat.err)
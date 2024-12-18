import subprocess
import random
import argparse
from tqdm import tqdm
import os
from names_generator import generate_name

MATHGEN_PATH="../mathgen"
print(generate_name(style="capital"))

parser = argparse.ArgumentParser(description='Generate random data')
parser.add_argument("--count", type=int, default=1000, help="Number of records to generate")
parser.add_argument("--output", type=str, default="output", help="Output Directory")
args = parser.parse_args()

output_dir = args.output
count = args.count

if not os.path.exists(output_dir):
  os.makedirs(output_dir)

for index in tqdm(range(count)):
  full_output_path = os.path.join(output_dir, f"{index}")
  if not os.path.exists(full_output_path):
    os.makedirs(full_output_path)
  author_count = random.choice(range(1, 5))
  authors = [generate_name(style="capital") for _ in range(author_count)]

  full_command = [os.path.join(MATHGEN_PATH, "mathgen.pl"), "--mode", "dir", "--dir", full_output_path]
  
  for author in authors:
    full_command.append("--author")
    full_command.append(author)
  
  subprocess.run(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  
  
  




import os
from tqdm import tqdm
import lzma

def xz_files_in_dir(dir):
    files = []
    for filename in os.listdir(dir):
        if filename.endswith('.xz') and os.path.isfile(os.path.join(dir, filename)):
            files.append(filename)
    return files

folder_path = "/Users/clementmarie/Desktop/ML/datasets/OpenWebCorpus/openwebtext"
output_file_train = "output_train.txt"
output_file_val = "output_val.txt"
vocab_file = "vocab.txt"

files = xz_files_in_dir(folder_path)
total_files = len(files)

# calculating split indices
split_index = int(total_files*0.9)
files_train = files[:split_index]
files_val = files[split_index:]

vocab = set()

# processing training files
with open(output_file_train, "w", encoding = 'utf-8') as outfile:
    for filename in tqdm(files_train, total = len(files_train)):
        file_path = os.path.join(folder_path, filename)
         # rt stands for read text
        with lzma.open(file_path, "rt", encoding = 'utf-8') as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            # add characters dict content to vocab dict
            vocab.update(characters)
            
            
# processing val files
with open(output_file_val, "w", encoding = 'utf-8') as outfile:
    for filename in tqdm(files_val, total = len(files_val)):
        file_path = os.path.join(folder_path, filename)
         # rt stands for read text
        with lzma.open(file_path, "rt", encoding = 'utf-8') as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            # add characters dict content to vocab dict
            vocab.update(characters)

# write vocab to vocab.txt
with open(vocab_file, "w", encoding = 'utf-8') as vfile:
    for char in vocab:
        vfile.write(char + '\n')
           
'''
Patricia Zito 
Feb 5, 2022
'''

import xmltodict
import Bio 
from Bio import Entrez 
Entrez.email = "pzito@wisc.edu"

acc = "TRY75264.1" # for testing 

# getting info from accession number 

# acquiring information 
handle = Entrez.efetch(db = "protein", id = acc, rettype = "gb", retmode = "text")
readable = handle.read()
handle.close()

# parsing and putting info into dict 
read_split = readable.split()
read_split
keys = ['LOCUS', 'DEFINITION', 'ACCESSION', 'VERSION', 'DBLINK', 'KEYWORDS', 'SOURCE',
    'ORGANISM', 'REFERENCE', 'AUTHORS', 'TITLE', 'JOURNAL', 'PUBMED', 'REFERENCE', 'AUTHORS'
    'TITLE', 'JOURNAL', 'COMMENT', 'FEATURES', 'ORIGIN']
copy_keys = keys
index_keys = [] # this contains index for where each key is in read_split
values = []
my_dict = {}

for i in range(len(read_split)):
    if read_split[i] == keys[0]:
        index_keys.append(i)
        keys.remove(keys[0])

for i in range(len(index_keys)): 
    print(index_keys[i])
    print(read_split[index_keys[i+1]:index_keys[i+1]-1])
    my_dict[index_keys[i]] = read_split[index_keys[i+1]:index_keys[i+1]-1]
        
for i in range(len(read_split)):
    if read_split[i] == keys[0]: # if this is the right word
        my_dict[keys[0]] = "empty" # make it a dict key
        keys.remove(keys[0]) # remove from options
    else: # if not, it is a value 
        values.append(read_split[i]) # add it to temp value 
        my_dict[copy_keys]



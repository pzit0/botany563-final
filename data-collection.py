'''
Patricia Zito 
Feb 5, 2022
'''
import Bio 
from Bio import Entrez 
Entrez.email = "pzito@wisc.edu"

acc = "TRY75264.1" # for testing 

# getting info from accession number 

# acquiring handle  
handle = Entrez.efetch(db = "protein", id = acc, rettype = "gb", retmode = "text")
readable = handle.read()
handle.close()

# parsing and putting info into dict 
# I've tried through xmltodict and it didn't work
# have to do it manually 
read_split = readable.split()

keys = ['LOCUS', 'DEFINITION', 'ACCESSION', 'VERSION', 'DBLINK', 'KEYWORDS', 'SOURCE',
    'ORGANISM', 'REFERENCE', 'AUTHORS', 'TITLE', 'JOURNAL', 'PUBMED', 'REFERENCE', 'AUTHORS',
    'TITLE', 'JOURNAL', 'COMMENT', 'FEATURES', 'ORIGIN'] # got these from looking at original file

my_dict = {}
key = keys[0] # temp
values = [] # temp 

for i in range(len(read_split)):
    if read_split[i] != keys[0]: # if it's a value 
        values.append(read_split[i]) # accumulate 
    else: # it's a key 
        if len(values): # if value is full 
            my_dict[key] = values # match key and value 
            key = keys[0] # current key 
            keys.remove(keys[0]) # start looking for next boundary
            values = [] # restart values 
        else: 
            keys.remove(keys[0])







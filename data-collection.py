'''
Patricia Zito 
Feb 5, 2022
'''

import xmltodict
import Bio 
from Bio import Entrez 
Entrez.email = "pzito@wisc.edu"

acc = "TRY75264.1"
# getting info from accession number 
handle = Entrez.efetch(db = "protein", id = acc, rettype = "gb", retmode = "xml")
info = handle.read()
handle.close()
dic = xmltodict.parse(info)

hand = Entrez.efetch(db = "protein", id = acc, rettype = "gb", retmode = "text")
readable = hand.read()
read_split = readable.split()
keys = []
values = []
for i in range(len(read_split)):
    print(read_split[i])
    if (i%2) == 0:
        keys += read_split[i]
    else:
        values += read_split[i]


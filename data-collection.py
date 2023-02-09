'''
Patricia Zito 
Feb 5, 2023
'''

# Importing libraries
import Bio 
from Bio import Entrez 
Entrez.email = "pzito@wisc.edu"

# Settings
# KEYS FOR DICTIONARY 
protein_keys = ['LOCUS', 'DEFINITION', 'ACCESSION', 'VERSION', 'DBLINK', 'KEYWORDS', 'SOURCE',
        'ORGANISM', 'REFERENCE', 'AUTHORS', 'TITLE', 'JOURNAL', 'PUBMED', 'REFERENCE', 'AUTHORS',
        'TITLE', 'JOURNAL', 'COMMENT', 'FEATURES', 'ORIGIN'] 
assembly_keys = []

acc = "TRY75264.1" # for testing 
acc1 = "PRJNA237968"

# Defining Functions
def get_dict(id, database):
    '''
    Function that creates a dictionary containing information from genbank 
        from an accession number 
    Inputs: 
        id: a string, an UID or accession number 
    Outputs:
        out: a dictionary containing this information 
    '''

    # protein or assembly 
    if database == "protein":
        keys = ['LOCUS', 'DEFINITION', 'ACCESSION', 'VERSION', 'DBLINK', 'KEYWORDS', 'SOURCE',
        'ORGANISM', 'REFERENCE', 'AUTHORS', 'TITLE', 'JOURNAL', 'PUBMED', 'REFERENCE', 'AUTHORS',
        'TITLE', 'JOURNAL', 'COMMENT', 'FEATURES', 'ORIGIN'] 
    if database == "assembly":
        assembly_keys = [] 

    # acquiring handle  
    handle = Entrez.efetch(db = database, id = acc, rettype = "gb", retmode = "text")
    readable = handle.read()
    handle.close()

    # parsing and putting info into dict 
    read_split = readable.split()
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
    
    return my_dict


# next function: assembly = Bioproject
# take dictionary and get_dict(assembly) 
assembly_accession = my_dict['DBLINK'][1]
assembly_dict = get_dict(id = assembly_accession, database = 'assembly', in_keys = assembly_keys)

# next function: extract info from dict and build dataframe 

# next function: filter dataframe 

# next function: import list of accession numbers -> runs everything and exports data files 

##############TESTING################
handl = Entrez.efetch(db = "protein", id = "TRY75264.1", rettype = "gb", retmode = "xml")
readabl = Entrez.read(handl)
handl.close()

read_dict = readabl[0] # because dict is nested inside object
read_dict['GBSeq_sequence'] # sequence of the protein
read_dict['GBSeq_length'] # protein size 
read_dict['GBSeq_comment'] # assembly accession number 
read_dict['GBSeq_organism'] # organism 

# now testing efetch the assembly
hand = Entrez.efetch(db = "bioproject", id = read_dict['GBSeq_project'], rettype = 'gb', retmode = 'string')
read = hand.read()
import xml.etree.ElementTree as ET 
tree = ET.parse(hand)
root = tree.getroot()







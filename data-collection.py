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
read_dict['GBSeq_comment'] # assembly info, does not contain scaffold info, however
read_dict['GBSeq_organism'] # organism 

# now testing efetch the assembly through bioproject 
# absolutely no important info 
hand = Entrez.efetch(db = "bioproject", id = read_dict['GBSeq_project'], rettype = 'gb', retmode = 'string')
read = hand.read()
import xml.etree.ElementTree as ET 
tree = ET.parse(hand)
root = tree.getroot()

# through genome 
# omg this takes forever and it doesn't work 
hand1 = Entrez.efetch(db = "genome", id = "12192", rettype = "gb", retmode = "string")
read1 = hand1.read()

# assembly 
hand2 = Entrez.efetch(db = "assembly", id = "4120771", rettype = "gb", retmode = "xml")
read2 = hand2.read()

hand3 = Entrez.esummary(db = "assembly", id = "4120771", report = "full", retmode = "xml") # this worked for like a second? 
read3 = hand3.read()

hand4 = Entrez.esummary(db = 'assembly', id ='4120771', report = 'full') # now this kind of works, id has to be iud, NOT genbank 
read4 = hand4.read() # as it turns out, the dict is NOT nested inside, a bunch of random numbers literally what the fuck 

Entrez.esummary()




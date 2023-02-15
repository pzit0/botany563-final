'''
Patricia Zito 
Feb 5, 2023
'''

# Importing libraries
import Bio 
from Bio import Entrez 
Entrez.email = "pzito@wisc.edu"

acc1 = "TRY75264.1" # for testing, can get this from BLAST 
acc2 = "XP_047735583.1" # for testing
blast_res = []

# importing data 

# function for extracting acc numbers from blast result csv 
def get_acc(blast_res):
    '''
    This function takes in the Blast result csv file and returns a list 
        of protein accession numbers. 

    Input: blast-res (csv file)
    Output: list of accession numbers (python list)
    '''
    acc_lst = []
    return acc_lst 

# maybe write some logs here, like if not a match (protein and assembly)
def look_ncbi(acc):
    '''
    This function takes in a protein ncbi accession number (possibly from your BLAST result)
        and returns information about its protein and assembly as a dict. 
    
    Input: Accession Number (string)
    Output: Dict containing: species, protein accession number, protein size, protein length, 
        assembly name, genome coverage, sequencing level, biosample accession number, contig N50,
        scaffold N50, Busco comments. 
    '''
    info = dict()

    # extracting info from protein link
    prot_handle = Entrez.efetch(db = 'protein', id = acc, rettype = 'gb', retmode = 'xml')
    prot_record = Entrez.read(prot_handle)
    prot_handle.close()
    protein_dict = prot_record[0] # dict is nested inside parsing object

    info['species'] = protein_dict['GBSeq_organism'] # organism 
    info['protein-accession'] = acc # accession number 
    info['protein-sequence'] = protein_dict['GBSeq_sequence'] # protein sequence 
    info['protein-length'] = protein_dict['GBSeq_length'] # protein size 
    
    assembly = protein_dict['GBSeq_comment'] # assembly info available in protein link 
    a = assembly.split() # so it reads the words and not characters 
    for i in range(len(a)):
        if a[i] == "Assembly":
            if a[i+1] == "Name":
                assembly_term = a[i+3] # use this to search for assembly id
        elif a[i] == "Genome":
            if a[i+1] == "Coverage":
                info['genome-coverage'] = a[i+3] # genome coverage 
            

    # getting assembly id: 
    # cannot use genbank accession code for obtaining assembly info, has to be the unique uid 
    pre_assembly_handle = Entrez.esearch(db = "assembly", term = assembly_term) 
    pre_assembly_record = Entrez.read(pre_assembly_handle)
    pre_assembly_handle.close()
    assembly_id = pre_assembly_record['IdList'][0] # this is the uid for the assembly 

    # extracting info from assembly link: 
    assembly_handle = Entrez.esummary(db = 'assembly', id = assembly_id, report = 'full') 
    assembly_record = Entrez.read(assembly_handle) 
    assembly_handle.close()
    assembly_dict = assembly_record['DocumentSummarySet']['DocumentSummary'][0] # very nested 

    info['assembly-status'] = assembly_dict['AssemblyStatus'] # level (chromosome?)
    info['contig-N50'] = assembly_dict['ContigN50'] # contigN50
    info['scaffold-N50'] = assembly_dict['ScaffoldN50'] # scaffold n50 
    info['busco'] = assembly_dict['Busco']# busco 
    
    return info 

# function for filtering 
def filter(info):
    '''
    This function takes in a dictionary containing detailed information from a 
        blast result row, and it filters through it. 

    Input: info (python dictionary)
    Outputs: 
        detailed_filtered = dataframe containing usable results and their details  
        detailed_trash = dataframe containing discarded results and their details 
        log = list of logs for debugging
    '''

# writing and exporting

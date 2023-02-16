'''
Collect Data from NCBI 

Patricia Zito 
Feb 5, 2023
'''

# Importing libraries
import Bio 
from Bio import Entrez 
import pandas as pd
Entrez.email = "pzito@wisc.edu"

acc1 = "TRY75264.1" # for testing, can get this from BLAST 
acc2 = "XP_047735583.1" # for testing

# importing data and testing accession numbers 
blast_res = pd.read_csv('/Users/patriciazito/Desktop/botany563-final/2023-01-31-NHA7-HitTable.csv', )
acc_list = blast_res.iloc[:, 1] # selects only second column containing protein accession numbers

# maybe write some logs here, like if not a match (protein and assembly)
def prot_ncbi(acc):
    '''
    This function takes in a protein ncbi accession number (possibly from your BLAST result)
        and returns information about its protein and assembly as a dict. 
    
    Input: Accession Number (string)
    Output: Dict containing: species, protein accession number, protein size, protein length, 
        assembly-name, genome coverage, sequencing level, biosample accession number, contig N50, scaffold N50, 
        Busco comments. 
            Ass: a boolean value that tells whether the script was able to obtain a satisfying assembly match
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
    
    info['assembly-name'] = False # default is false 
    
    if 'GBSeq_comment' in protein_dict.keys(): # if they have this information 
        assembly = protein_dict['GBSeq_comment'] # assembly info available in protein link 
        a = assembly.split() # so it reads the words and not characters 
        for i in range(len(a)):
            if a[i] == "Assembly":
                if a[i+1] == "Name":
                    info['assembly-name'] = a[i+3] # use this to search for assembly id
            elif a[i] == "Genome":
                if a[i+1] == "Coverage":
                    info['genome-coverage'] = a[i+3] # genome coverage 
    
    return info

def ass_ncbi(info):
    '''
    obtain assembly info, if possible. 
    '''

    if info['assembly-name']:
        # getting assembly id: 
        # cannot use genbank accession code for obtaining assembly info, has to be the unique uid 
        pre_assembly_handle = Entrez.esearch(db = "assembly", term = info['assembly-name']) 
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
    
    return info 
    

# function for filtering 
def filter(acc_list):
    '''
    This function takes in a dictionary containing detailed information from a 
        blast result row, and it filters through it. 

    Input: info (python dictionary)
    Outputs: 
        filtered = dataframe containing usable results and their details  
        trash = dataframe containing discarded results and their details 
        log = list of logs for debugging
    '''
    # Setting minimum parameters 
    min_prot_size = 100
    min_genome_cov = 30
    min_contig_N50 = 100
    min_scaffold_N50 = 1000

    filtered = []    
    trash = []

    # start log information 
    log = []
    no_info = 0
    bad_coverage = 0
    small_protein = 0
    bad_cont_scaffold = 0
    
    for acc in acc_list: 
        row_prot = prot_ncbi(acc)
        print('NOW LOOKING AT', row_prot['species'], row_prot['protein-accession'])
        if row_prot['assembly-name']: 
            row = ass_ncbi(row_prot)
            if int(row['protein-length']) >= min_prot_size: # if at least this size 
                cov = row['genome-coverage'].replace('x', '')
                if float(cov) >= min_genome_cov: # if good coverage
                    if int(row['contig-N50']) >= min_contig_N50: # if good contig N50
                        if int(row['scaffold-N50']) >= min_scaffold_N50: # if good scaffold N50
                            filtered.append(row)
                            print(row['species'], row['protein-accession'], 'IS GOOD')
                            continue # go to the next item 
                        else:
                            m = str(row['species']) + str(row['protein-accession']) + 'was discarded due to low scaffold N50 score\n'
                            log.append(m)
                            bad_cont_scaffold += 1 
                    else: 
                        m = str(row['species']) + str(row['protein-accession']) + 'was discarded due to low contig N50 score\n'
                        log.append(m)
                        bad_cont_scaffold += 1 
                else: 
                    m = str(row['species']) + str(row['protein-accession']) + 'was discarded due to bad coverage\n'
                    log.append(m)
                    bad_coverage += 1 
            else: 
                m = str(row['species']) + str(row['protein-accession']) + 'was discarded due to small protein size\n'
                log.append(m)
                small_protein += 1 
        else: 
            m = str(row['species']) + str(row['protein-accession']) + 'had no assembly information\n'
            log.append()
            no_info += 1 
        trash.append(row_prot['species'])
        print(row_prot['species'], row_prot['protein-accession'], 'IS TRASH')

    # log comp. 
    log.append(print('\nA total of:', len(filtered), 'proteins were selected out of', len(acc_list)))
    log.append(print('this is equivalent to', len(filtered)/len(acc_list), 'of the data\n'))
    log.append(print(no_info, "or", no_info/len(trash), "were discarded because their relevant assemblly information was not found\n"))
    log.append(print(bad_coverage, "or", bad_coverage/len(trash), "were discarded due to bad genome coverage\n"))
    log.append(print(small_protein, "or", small_protein/len(trash), "were discarded due to small protein size\n"))
    log.append(bad_cont_scaffold, "or", bad_cont_scaffold/len(trash), "were discarded due to small contig or scaffold size\n")

    print(log[-5:])

    return filtered, trash, log



# writing and exporting

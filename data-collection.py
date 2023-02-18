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
    info['genome-coverage'] = '0x' # default is 0
    info['recover'] = False # any info that makes this entry worth recovering?  
    
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
            elif a[i] == "Pacbio" or a[i] == "Nanopore":
                info['recover'] = True 
    
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
    
    passed_size = 0
    passed_cov = 0
    passed_assembly = 0 
    passed_scaffold = 0

    filtered = []    
    maybes = []
    trashed = []
    
    for acc in acc_list: 
        row = prot_ncbi(acc)
        cov = row['genome-coverage'].replace('x', '')
        if int(row['protein-length']) >= min_prot_size: # if at least this size 
            passed_size += 1
            if float(cov) >= min_genome_cov: # if good coverage
                passed_cov += 1
                if row['assembly-name']: 
                    passed_assembly += 1 
                    ass_ncbi(row) # obtain assembly
                    if int(row['contig-N50']) >= min_contig_N50: # if good contig N50
                        if int(row['scaffold-N50']) >= min_scaffold_N50: # if good scaffold N50
                            filtered.append(row)
                            passed_scaffold += 1
                            print(row['species'], row['protein-accession'], 'IS GOOD')
                            continue # go to the next item 
                print('could not find assembly info but', row['species'], row['protein-accession'], 'has good coverage')
                maybes.append(row)
            if row['recover'] and row not in maybes: # was either sequenced w Pacbio or nanopore
                print('could not find assembly info but', row['species'], row['protein-accession'], 'had good sequencing tech')
                maybes.append(row)            
        trashed.append(row['species'])

    # log stuff 
    print('\nA total of ', len(acc_list), 'proteins were assessed')
    print('Out of those', len(filtered), '(', len(filtered)/ len(acc_list), ') were successfully curated and obtained')
    print(len(acc_list)-passed_size, 'were discarded due to small protein size')
    print(passed_size-passed_cov, 'were discarded due to not having good coverage or not having any coverage information')
    print(passed_cov-passed_assembly, 'were discarded due to me not finding its assembly information')
    print(len(filtered)-passed_scaffold, 'were discarded due to bad scaffold or contig N50 scores')


    return filtered, trashed, maybes


filtered, trashed, maybes = filter(acc_list)


# check species 
for i in filtered: 
    print(i['species'])

for i in maybes: 
    print(i['species'])

script_curated = [i['protein-accession'] for i in filtered]
script_curated.extend([i['protein-accession'] for i in maybes])

# check which ones didn't show up on my manual thingy 
curated = pd.read_excel('/Users/patriciazito/Desktop/botany563-final/curated-orthologs.xlsx', header=0)
curated_acc_list = curated['protein-accession']
curated_acc_list = curated_acc_list.dropna()

# check their entries
missing = []
for i in curated_acc_list: 
    if i not in script_curated: 
        prot_handle = Entrez.efetch(db = 'protein', id = i, rettype = 'gb', retmode = 'xml')
        prot_record = Entrez.read(prot_handle)
        prot_handle.close()
        protein_dict = prot_record[0] 
        missing.append(protein_dict)
        
# check the first one 
for key in missing[0]:
    print(key, ":", missing[0][key])
# might have to get information from bioproject instead 
# also interesting, missing[0]['GBSeq_feature-table'] has GeneID

# get gene id: 
gb_feat = missing[0]['GBSeq_feature-table'][-1]['GBFeature_quals'][-1]['GBQualifier_value']
id = str()
for i in gb_feat:
    if i.isdigit():
        id += i 

# second one:
for key in missing[1]:
    print(key, ":", missing[1][key])
# can also get gene sequence from GBSeq_locus (it goes to nucleotide)

# writing and exporting

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

acc = "TRY75264.1" # for testing, can get this from BLAST 
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
        assembly-name, genome coverage, sequencing level, biosample accession number, contig N50, scaffold N50.
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
    
    keys = [str(i) for i in protein_dict.keys()] # keys available in Entrez entry
    if 'GBSeq_project' in keys:
        info['project-accession'] = protein_dict['GBSeq_project'] # project id 
    else: 
        info['project-accession'] = False 
    
    info['assembly-name'] = False # default is false     
    if 'GBSeq_comment' in keys: # if they have this information 
        assembly = protein_dict['GBSeq_comment'] # assembly info available in protein link 
        a = assembly.split() # so it reads the words and not characters 
        for i in range(len(a)):
            if a[i] == "Assembly":
                if a[i+1] == "Name":
                    info['assembly-name'] = a[i+3] # use this to search for assembly id
    
    return info 

def ass_ncbi(info):
    '''
    obtain assembly info, if possible. 
    '''

    if info['assembly-name']: # already have an assembly name 
        # getting assembly id: 
        # cannot use genbank accession code for obtaining assembly info, has to be the unique uid 
        pre_assembly_handle = Entrez.esearch(db = "assembly", term = info['assembly-name']) 
        pre_assembly_record = Entrez.read(pre_assembly_handle)
        pre_assembly_handle.close()
        assembly_id = pre_assembly_record['IdList'][0] # this is the uid for the assembly

        assembly_handle = Entrez.esummary(db = 'assembly', id = assembly_id, report = 'full') 
        assembly_record = Entrez.read(assembly_handle) 
        assembly_handle.close()
        assembly_dict = assembly_record['DocumentSummarySet']['DocumentSummary'][0] # very nested 
        info['assembly-status'] = assembly_dict['AssemblyStatus'] # level (chromosome?)
        info['contig-N50'] = assembly_dict['ContigN50'] # contigN50
        info['scaffold-N50'] = assembly_dict['ScaffoldN50'] # scaffold n50 
        #info['coverage'] = assembly_dict['Coverage']
    
    else: # did not have a name associated, have to look it up by species
        if info['project-accession']: # if they have an accession
            search_organism = info['species']
            pre_assembly_handle = Entrez.esearch(db = "assembly", term = search_organism) 
            pre_assembly_record = Entrez.read(pre_assembly_handle)
            pre_assembly_handle.close() 

            for assembly_id in pre_assembly_record['IdList']: 
                assembly_handle = Entrez.esummary(db = 'assembly', id = assembly_id, report = 'full')
                assembly_record = Entrez.read(assembly_handle)
                assembly_handle.close()
                assembly_dict = assembly_record['DocumentSummarySet']['DocumentSummary'][0]
                if assembly_dict['GB_BioProjects']: # if info's stored here 
                    bioproject_accn = assembly_dict['GB_BioProjects'][0]['BioprojectAccn']
                elif assembly_dict['RS_BioProjects']: # or here 
                    bioproject_accn = assembly_dict[0]['BioprojectAccn']
                if bioproject_accn == info['project-accession']: # if the search's bioproj acc matches the protein bioproj
                    assembly_handle = Entrez.esummary(db = 'assembly', id = assembly_id, report = 'full') 
                    assembly_record = Entrez.read(assembly_handle) 
                    assembly_handle.close()
                    assembly_dict = assembly_record['DocumentSummarySet']['DocumentSummary'][0] # very nested 
                    info['assembly-name'] = assembly_record['DocumentSummarySet']['DocumentSummary'][0]['AssemblyName']
                    info['assembly-status'] = assembly_dict['AssemblyStatus'] # level (chromosome?)
                    info['contig-N50'] = assembly_dict['ContigN50'] # contigN50
                    info['scaffold-N50'] = assembly_dict['ScaffoldN50'] # scaffold n50
                    #info['coverage'] = assembly_dict['Coverage'] # coverage
                    break 
        
    
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
    min_prot_size = 200
    min_genome_cov = 30
    min_contig_N50 = 1000
    min_scaffold_N50 = 10000
    
    # starting counts for log
    passed_size = 0
    #passed_cov = 0
    passed_assembly = 0 
    passed_scaffold = 0

    # starting local vars 
    filtered = []    
    trashed = []
    trashed_bioproject = []
    
    for acc in acc_list: 
        row = prot_ncbi(acc)
        print('ASSESSING:', row['species'], row['protein-accession'])
        #cov = row['genome-coverage'].replace('x', '')
        if row['project-accession'] not in trashed_bioproject: 
            if int(row['protein-length']) >= min_prot_size: # if at least this size 
                passed_size += 1
                ass_ncbi(row) # get assembly info
                if row['assembly-name']: # if assembly was successfully acquired
                    passed_assembly += 1
                    if int(row['contig-N50']) >= min_contig_N50: # if good contig N50
                        if int(row['scaffold-N50']) >= min_scaffold_N50: # if good scaffold N50
                            filtered.append(row)
                            passed_scaffold += 1
                            print(row['species'], row['protein-accession'], 'WAS ADDED TO FILTERED')
                            continue # go to the next item 
        trashed.append(row)
        if row['project-accession'] not in trashed_bioproject: 
            trashed_bioproject.append(row['project-accession'])

    # log stuff 
    print('\nA total of ', len(acc_list), 'proteins were assessed')
    print('Out of those,', len(filtered), '(', len(filtered)/ len(acc_list), ') were successfully curated and obtained')
    print(len(acc_list)-passed_size, 'were discarded due to small protein size')
    print(passed_size-passed_assembly, 'were discarded due to me not finding its assembly information')
    #print(passed_assembly-passed_cov, 'were discarded due to not having good coverage or not having any coverage information')
    #print(passed_cov-passed_assembly, 'were discarded due to me not finding its assembly information')
    print(len(filtered)-passed_scaffold, 'were discarded due to bad scaffold or contig N50 scores')


    return filtered, trashed


filtered, trashed = filter(acc_list)

########## DOES IT WORK? ########
# check species 
for i in filtered:         
    print(i['species'])


script_curated = [i['protein-accession'] for i in filtered]

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

for i in missing: 
    print(i['GBSeq_definition'])

# check the first one 
for key in missing[0]:
    print(key, ":", missing[0][key])
# might have to get information from bioproject instead 
# also interesting, missing[0]['GBSeq_feature-table'] has GeneID

##### get gene id: 
gb_feat = missing[0]['GBSeq_feature-table'][-1]['GBFeature_quals'][-1]['GBQualifier_value']
gene_id = str()
for i in gb_feat:
    if i.isdigit():
        gene_id += i 

###### get gene info (e-fetch): 
gene_handle = Entrez.efetch(db = 'gene', id = gene_id, rettype = 'gb', retmode = 'xml')
gene_record = Entrez.read(gene_handle)
gene_handle.close()
gene_dict = gene_record[0]
for i in gene_dict:
    print(i, ':', gene_dict[i]) 
# does not contain sequence 
# can get scaffold and nucl positions though 

# gene info (e-summary):
gene_handle2 = Entrez.esummary(db = 'gene', id = gene_id, report = 'full')
gene_record2 = Entrez.read(gene_handle2)
gene_handle2.close()
gene_dict2 = gene_record2['DocumentSummarySet']['DocumentSummary'][0]
gene_dict2 # nope, not useful

# it the gene id the same as the nucl id? 

##### see what I can get from the bioproject handle (efetch)
project_id = missing[0]['GBSeq_project']
pr_handle = Entrez.efetch(db = 'bioproject', id = project_id, rettype = 'gb', retmode = 'text')
print(pr_handle.readline().strip()) # xml doesn't work for bioproject
pr_handle.close()

# bioproject handle (esummary)
pr_handle2 = Entrez.esummary(db = 'bioproject', id = project_id, report = 'full')
pr_record2 = Entrez.read(pr_handle2,  validate=False) # doesn't work anymore
pr_handle2.close()
pr_dict2 = pr_record2['DocumentSummarySet']['DocumentSummary'][0]
pr_dict2 # nope, not useful

######## trying to find assembly, other ways: 
search_organism = missing[0]['GBSeq_organism']
pre_assembly_handle = Entrez.esearch(db = "assembly", term = search_organism) 
pre_assembly_record = Entrez.read(pre_assembly_handle)
pre_assembly_handle.close()

res = []
for id in pre_assembly_record['IdList']: 
    assembly_handle = Entrez.esummary(db = 'assembly', id = id, report = 'full')
    assembly_record = Entrez.read(assembly_handle)
    assembly_handle.close()
    res.append(assembly_record)

for entry in res: 
    if entry['DocumentSummarySet']['DocumentSummary'][0]['GB_BioProjects']:
        bioproject_accn = entry['DocumentSummarySet']['DocumentSummary'][0]['GB_BioProjects'][0]['BioprojectAccn']
    elif entry['DocumentSummarySet']['DocumentSummary'][0]['RS_BioProjects']:
        bioproject_accn = entry['DocumentSummarySet']['DocumentSummary'][0]['RS_BioProjects'][0]['BioprojectAccn']
    print(bioproject_accn)
    if bioproject_accn == project_id: 
        print('eureka')
    else: 
        print('oop not this one')

# for res0: 
res[0]['DocumentSummarySet']['DocumentSummary'][0]['RS_BioProjects'][0]['BioprojectAccn']

# for res1: 
res[1]['DocumentSummarySet']['DocumentSummary'][0]['GB_BioProjects'][0]['BioprojectAccn']

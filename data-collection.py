'''
Collect Data from NCBI 

Patricia Zito 
Feb 5, 2023
'''

# Importing libraries
import Bio 
from Bio import Entrez 
import pandas as pd

acc = "TRY75264.1" # for testing, can get this from BLAST 
acc = "XP_047735583.1" # for testing

# importing data and testing accession numbers 
input1 = input("Name of your BLAST result csv file: ")
input2 = input("Your wisc email: ")

blast_res = pd.read_csv(input1)
acc_list = blast_res.iloc[:, 1] # selects only second column containing protein accession numbers
Entrez.email = input2

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
            elif a[i] == "Coverage":
                info['coverage'] = a[i+2]

    info['pubmed-accession'] = False # default is false 
    if 'GBSeq_references' in keys: # if info is avaialble 
        if 'GBSeq_references': # get it 
            info['pubmed-accession'] = protein_dict['GBSeq_references'][0]['GBReference_pubmed']
    
    return info 

def ass_ncbi(info):
    '''
    This function expands on an existing dictionary by extracting information from 
        an assembly entry. It first checks to see whether there was an assembly name 
        associated with the protein entry. If there is, it will search that name and 
        retrieve the the assembly status, contig N50, scaffold N50, coverage, and Busco
        comments. If there is NOT an assembly name associated with the protein, the 
        function will search the organism on the assembly database and compare the bioproject
        number from the protein with the results found. If it is the same, it retrieves the
        same information. Sometimes, NCBI is not updated, and newer assemblies might not 
        show as a potential search result. Other times, there might not have been a bioproject
        accession number associated with either protein or assembly entries. This means there
        is no way to check whether that assembly matches the protein. In both cases, this 
        function will fail to parse through the assembly page, and it will discard this protein
        from the filter process. 
    
    Input: info (dict) already containing information from the protein scraping process. 
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
        if info['project-accession']: # if they have a bioproject accession number
            search_organism = info['species']
            pre_assembly_handle = Entrez.esearch(db = "assembly", term = search_organism) 
            pre_assembly_record = Entrez.read(pre_assembly_handle) # contains search results 
            pre_assembly_handle.close() 

            for assembly_id in pre_assembly_record['IdList']: # for each result
                assembly_handle = Entrez.esummary(db = 'assembly', id = assembly_id, report = 'full')
                assembly_record = Entrez.read(assembly_handle) # get summary
                assembly_handle.close()
                assembly_dict = assembly_record['DocumentSummarySet']['DocumentSummary'][0]
                if assembly_dict['GB_BioProjects']: # get bioproject accession number from search result
                    bioproject_accn = assembly_dict['GB_BioProjects'][0]['BioprojectAccn']
                elif assembly_dict['RS_BioProjects']: # or here (sometimes info is placed in diff. places)
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



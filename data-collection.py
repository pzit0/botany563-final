'''
Collect Data from NCBI 

Patricia Zito 
Feb 5, 2023
'''

# IMPORTING LIBRARIES 
import Bio 
from Bio import Entrez 
import pandas as pd
import os

# DEFINING FUNCTIONS 
# extract information from protein entry
def prot_ncbi(acc):
    '''
    This function takes in a protein ncbi accession number (possibly from your BLAST result)
        and returns information about its protein and assembly as a dict. 
    
    Input: Accession Number (string)
    Output: Dict containing: species, protein accession number, protein sequence, protein size, 
        bioproject accession number, sequencing technology, assembly name, genome refseq accession
        number and sequence technology.
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
    
    # defaults 
    info['sequencing-technology'] = False 
    info['assembly-name'] = False     
    info['genome_refseq'] = False 

    if 'GBSeq_comment' in keys: # if they have this information 
        assembly = protein_dict['GBSeq_comment'] # assembly info available in protein link 
        a = assembly.split() # so it reads the words and not characters 
        tech = str()
        for i in range(len(a)):
            if a[i] == "Assembly":
                if a[i+1] == "Name":
                    info['assembly-name'] = a[i+3] # use this to search for assembly id
            if a[i] == "Technology": # this might fail, still testing 
                for j in a[i+2:len(a)]:
                    tech += j
                    if j == ";":
                        info['sequencing-technology'] = tech
                        break
            if a[i] == "genomic":
                if a[i+1] == "sequence":
                    genome_refseq = a[i+2]
                    info['genome-refseq'] = genome_refseq.replace('(', '').replace(')', '')

    info['pubmed-accession'] = False # default is false 
    if 'GBSeq_references' in keys: # if info is avaialble 
        if 'GBSeq_references': # get it 
            keys2 = [str(i) for i in protein_dict['GBSeq_references'][0].keys()]
            if 'GBReference_pubmed' in keys2: 
                info['pubmed-accession'] = protein_dict['GBSeq_references'][0]['GBReference_pubmed']
    
    return info 

# debugging function 
def show(info):
    '''
    Prints dictionary.
    '''
    for i in info: 
        print(i, ':', info[i])

# for the XP girlies 
def alt_ass_ncbi(info):
    '''
    Newer assemblies for proteins that have accession codes starting with "XP" don't show up 
        on the assembly searches. But sometimes, they contain refseq accession code for their 
        genome on the nucleotide database. 
        
    If we were unable to find its assembly, try the nucleotide database. This will 
        extract coverage, sequencing technology, and assembly method. 
    '''

    if info['genome-refseq']: 
        nucl_handle = Entrez.efetch(db = 'nucleotide', id = info['genome-refseq'], rettype = 'gb', retmode = 'xml')
        nucl_record = Entrez.read(nucl_handle)
        nucl_handle.close()
        nucl_dict = nucl_record[0]

        a = nucl_dict['GBSeq_comment'].split()
        tech = str()
        method = str() 
        for i in range(len(a)): 
            if a[i] == "Coverage": 
                print(a[i+2])
                #info['coverage'] = cov
            elif a[i] == "Technology": 
                print(a[i+2])
                for k in a[i+2:len(a)]: 
                        tech += k
                        if k == ";":
                            info['sequencing-technology'] = tech
                            print(tech)
                            break
            elif a[i] == "Assembly": 
                if a[i+1] == "Method":
                    for m in a[i+2:len(a)]:
                        method += m 
                        if m == ";":
                            info['assembly-method'] = method 
                            print(method)
                            break 

# extract information from assembly entry
def ass_ncbi(info):
    '''
    This function expands on an existing dictionary by extracting information from 
        an assembly entry. It first checks to see whether there was an assembly name 
        associated with the protein entry. If there is, it will search that name and 
        retrieve the the assembly status, scaffold N50, coverage.
        (number of scaffolds is hard, don't come for me). 
        
        If there is NOT an assembly name associated with the protein, the function will 
        search the organism on the assembly database and compare the bioproject
        number from the protein with the results found. If it is the same, it retrieves the
        same information. Sometimes, NCBI is not updated, and newer assemblies might not 
        show as a potential search result. Other times, there might not have been a bioproject
        accession number associated with either protein or assembly entries. This means there
        is no way to check whether that assembly matches the protein. In both cases, this 
        function will fail to parse through the assembly page, and it will discard this protein
        from the filter process. 
    
    Input: info (dict) already containing information from the protein scraping process. 
    '''
    # default is everything is false: 
    info['assembly-status'] = False
    info['scaffold-N50'] = False 

    if info['assembly-name']: # already have an assembly name 
        # getting assembly id: 
        # cannot use genbank accession code for obtaining assembly info, has to be the unique uid 
        pre_assembly_handle = Entrez.esearch(db = "assembly", term = info['assembly-name']) 
        pre_assembly_record = Entrez.read(pre_assembly_handle)
        pre_assembly_handle.close()
        if len(pre_assembly_record['IdList']): # if there are any results
            for assembly_id in pre_assembly_record['IdList']:
                assembly_handle = Entrez.esummary(db = 'assembly', id = assembly_id, report = 'full') 
                assembly_record = Entrez.read(assembly_handle) 
                assembly_handle.close()
                assembly_dict = assembly_record['DocumentSummarySet']['DocumentSummary'][0] # very nested 
                bioproject_accn = assembly_dict['GB_BioProjects'][0]['BioprojectAccn']
                if bioproject_accn == info['project-accession']: # if they match 
                    info['assembly-status'] = assembly_dict['AssemblyStatus'] # level (chromosome?)
                    info['scaffold-N50'] = assembly_dict['ScaffoldN50'] # scaffold n50 
                    info['coverage'] = assembly_dict['Coverage'] # coverage
                    break 
    
    else: # did not have a name associated, have to look it up by project number
        if info['project-accession']: # if they have a bioproject accession number
            pre_assembly_handle = Entrez.esearch(db = "assembly", term = info['project-accession']) 
            pre_assembly_record = Entrez.read(pre_assembly_handle) # contains search results 
            pre_assembly_handle.close() 
            if len(pre_assembly_record['IdList']): # if there are any results 
                for assembly_id in pre_assembly_record['IdList']: # for each result
                    print("ASSEMBLY ID",assembly_id)
                    assembly_handle = Entrez.esummary(db = 'assembly', id = assembly_id, report = 'full')
                    assembly_record = Entrez.read(assembly_handle) # get summary
                    assembly_handle.close()
                    assembly_dict = assembly_record['DocumentSummarySet']['DocumentSummary'][0] # nested 
                    if assembly_dict['GB_BioProjects']: # get bioproject accession number from search result
                        bioproject_accn = assembly_dict['GB_BioProjects'][0]['BioprojectAccn']
                        print("FOUND BIOPROJECT", bioproject_accn)
                        if bioproject_accn == info['project-accession']: # if assembly's matches the protein's
                            print("EUREKA")
                            info['assembly-name'] = assembly_record['DocumentSummarySet']['DocumentSummary'][0]['AssemblyName']
                            info['assembly-status'] = assembly_dict['AssemblyStatus'] # level (chromosome?)
                            info['scaffold-N50'] = assembly_dict['ScaffoldN50'] # scaffold n50
                            info['coverage'] = assembly_dict['Coverage'] # coverage
                            break # stop looking

# filter through 
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
    min_coverage = 30
    
    # starting counts for log
    failed_size = 0
    failed_assembly = 0
    failed_coverage = 0
    already_failed = 0

    # starting local vars 
    filtered = []    
    trashed = []
    trashed_bioproject = []
    
    for acc in acc_list: 
        row = prot_ncbi(acc)
        print('ASSESSING:', row['species'], row['protein-accession'])
        if row['project-accession'] not in trashed_bioproject: 
            if float(row['protein-length']) >= min_prot_size: # if at least this size 
                ass_ncbi(row) # get assembly info
                if not row['assembly-name']: # if assembly not successful 
                    alt_ass_ncbi(row) # try again through nucleotide database 
                if row['coverage']: # if coverage was successfully acquired
                    if float(row['coverage']) >= min_coverage: # if good coverage 
                        filtered.append(row)
                        print(row['species'], row['protein-accession'], 'WAS ADDED TO FILTERED')
                        continue # go to the next item
                    else:
                        failed_coverage += 1 
                        trashed.append(row) 
                        if row['project-accession'] not in trashed_bioproject: 
                            trashed_bioproject.append(row['project-accession'])
                        continue
                else: 
                    failed_assembly += 1 
                    trashed.append(row) 
                    if row['project-accession'] not in trashed_bioproject: 
                        trashed_bioproject.append(row['project-accession'])
                    continue
            else: 
                failed_size += 1 
                trashed.append(row)
                if row['project-accession'] not in trashed_bioproject: 
                    trashed_bioproject.append(row['project-accession'])
                continue
        else:
            already_failed += 1 


    # log stuff 
    m1 = '\nA total of ' + str(len(acc_list)) + ' proteins were assessed'
    m2 = 'Out of those, ' + str(len(filtered)) + '(' + str(len(filtered)/ len(acc_list)) + ') were successfully curated and obtained'
    m3 = str(failed_size) + ' were discarded due to small protein size'
    m4 = str(failed_assembly) + ' were discarded due to me not finding its assembly information'
    m5 = str(failed_coverage) + ' were discarded due to not having good coverage'
    m6 = str(already_failed) + ' were already checked and discarded'
    
    log = [m1, m2, m3, m4, m5, m6]
    for i in log: 
        print(i)

    return filtered, trashed, log

# export 
def export(filtered, trashed, log, input3): 
    '''
    Function to export these! 
    '''
    # transform these into pd dataframes 
    filtered_data = pd.DataFrame()
    trashed_data = pd.DataFrame()
    for i in filtered: 
        row = pd.DataFrame([i])
        filtered_data = filtered_data.append(row, ignore_index = True, sort = True)
    
    for i in trashed: 
        row = pd.DataFrame([i])
        trashed_data = trashed_data.append(row, ignore_index = True, sort = True)
    
    # exporting 
    path = os.getcwd()
    print('Your files have been saved here: ', path)

    filt_save = input3 + '-filtered.csv'
    trash_save = input3 + '-trashed.csv'
    filtered_data.to_csv(filt_save, index = False, header = True, encoding='utf-8')
    trashed_data.to_csv(trash_save, index = False, header = True, encoding='utf-8')

    log_name = input3 + '-log.txt' 
    with open(log_name, 'w') as f: 
        for line in log: 
            f.write(line)
            f.write('\n')


# IMPORTING DATA AND USER EXPERIENCE 
print("\nHello world! I'm a program to filter through your initial blast results for good quality paralogs :)\n")
print('to use me, answer the following:')
input1 = input("Name of your BLAST result csv file (e.g. '2023-01-31-NHA1-HitTable.csv'): ")
input2 = input("Your wisc email (e.g. 'jdoe@wisc.edu'): ")
input3 = input("Prefix of your output files (e.g. '2023-01-31-NHA1'): ")
blast_res = pd.read_csv(input1)

# RUN SCRIPT 
acc_list = blast_res.iloc[:, 1] # selects only second column containing protein accession numbers
Entrez.email = input2
print('\n\n\n################## RUNNING #####################')
filtered, trashed, log = filter(acc_list)
print('\n#################################################\n')
export(filtered, trashed, log, input3)
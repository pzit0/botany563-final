'''
Parse through these BLAST tables
'''

import os
import pandas as pd
import glob
import re 
import Bio 
from Bio import Entrez 
Entrez.email = "pzito@wisc.edu"
directory = "/Users/pzito/Desktop/botany563-final/data/orthologs/CURATION3-manually_add_paralogs_remove_nhaps/blast"
df = pd.DataFrame()

# merge all .blastn files 
for filename in glob.glob(f"{directory}/*.blastn"):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and os.path.getsize(f) > 0: # checking if it is a file and it's not empty 
        df = pd.concat([df, pd.read_csv(f, sep = "\t", header=None)])

# make sure none of these are XP files
acc_list = df.iloc[:, 1]
acc_noXP = [acc_list.iloc[i,] for i in range(len(acc_list)) if not bool(re.search("XP", str(acc_list.iloc[i,])))]
acc_final = [acc_noXP[i] for i in range(len(acc_noXP)) if acc_noXP[i] == acc_noXP[i]] # remove nans 

# these assemblies have actually already been filtered so 
# I think we really only need to collect the information again 
# prot_ncbi() is from ncbi_parser.py
bioprojects = []
species = []
df2 = pd.DataFrame()

len(acc_final)
first_third = acc_final[0:75]
second_third = acc_final[78:150]
third_third = acc_final[151:226]

for i in range(len(second_third)): 
    row = prot_ncbi(second_third[i])
    print('assessing: ', row['species'], row['protein-accession'], "index: ", i)
    if row['species'] in species and row['project-accession'] not in bioprojects: 
        print("weird accession number, skipping: ", row['species'], row['protein-accession'])
        continue # it's from another assembly, don't collect it 
    else: 
        df2 = pd.concat([df2, pd.DataFrame(row, index = [i])])
        print(row['species'], row['protein-accession'], 'WAS ADDED TO FILTERED')
        bioprojects.append(row['project-accession']) # update list of bioprojects
        species.append(row['species']) # update species

# errors: 
# 1). make sure I get back the XP sequences manually 
# 2). KAI1299850.1 is giving an error? so I'll remove it from the dataset and look at it manually 
# acc_final.remove("KAI1299850.1") # this is the Halotydeus 
# acc_final.remove("KAI1295545.1") # so is this
# ok no it actually just started giving me an error for the accession previous to the ones I removed 
# I'll put these back and divide the dataset into two 
# acc_final.append("KAI1299850.1")
# acc_final.append("KAI1295545.1")
# acc_final.remove("emb|CAD6994394.1|")
# it's an issue with ncbi because it always stops at 76 >:/ 
# I will fucking stab someone 
# acc_final.append("emb|CAD6994394.1|")
# running second half from 78 to 150 so I gotta make sure I'll get 75, 76, 77, 78. 

# get all the accession numbers on df2 
# alert if any in acc_final is not present in df2 
missing = []
acc_check = list(df2.iloc[:, 1])
for i in acc_final: 
    if i not in acc_check: 
        print(i)
        missing.append(i)
print("done")

# let's check if these are here because they have weird accession numbers 
# or if it's something weird happening again 
# I'll do this by cross-matching it with the ultra-conserved df

curation3 = pd.read_csv("/Users/pzito/Desktop/botany563-final/data/orthologs/CURATION3-manually_add_paralogs_remove_nhaps/orthologs-filtered-NHEless-manual_added1.csv")
conservative_prot = curation3.iloc[:, 4]

for i in range(len(missing)):
    if missing[i] in conservative_prot: 
        print("index: ", i, "protein-accession code", missing[i])

# ok sounds good to me, let's export the new dataset? 
# take out all the copies: 

df2.drop_duplicates()

# export 
df2.to_csv("/Users/pzito/Desktop/botany563-final/data/orthologs/CURATION3-manually_add_paralogs_remove_nhaps/orthologs-all-blast-prot-res.csv", index = True, header= True, encoding="utf-8")

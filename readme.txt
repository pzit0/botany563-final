# readme: 
A text file informing each item in this repo. 

# data: 
folder containing HitTables (Blast results), and data-collection.py outputs. Inside there is another folder containing a NHA7 old run (with old code), as well as a curated-ortholog.csv file, which contains the "filtered" orthologs that I did manually from the old-run NHA7 HitTable. I used the latter file to compare the efficiency of the data-collection.ou script. 

# notebook_log: 
A notebook log containing the procedures for this analysis. 

# ortholog-search-procedure: 
Another file (diary style) containing my progress and decisions for data collection. It further details how I wrote data-collection.py, as well as common debugs. 

# data-collection.py: 
Inputs: a csv hit table obtained from running BLAST online 
Outputs: two csv files containing sequences that were filtered and trashed, as well as a log. 

How it works: It uses the Entrez etool to obtain information and then curate it 
Limitations: It will fail to find information if it's not at the exact place it needs to be.
Inputs: a csv hit table obtained from running BLAST online 
Outputs: two csv files containing sequences that were filtered and trashed, as well as a log.txt 
How to use it: write "python3 data-collection.py" on your terminal and answer the questions (no quotation marks please)

Possible errors/ Troubleshooting: 
1. you didn't write the right name for the file 
2. you didn't write the right email address 
3. The authors failed to properly annotate their protein/ assembly entries (check trashed, what is False? Those are the items that failed to be parsed through)
4. ncbi is outdated and cannot find newer assemblies from an Entrez search
6. Node8 url error: ncbi is busy. Try running this file again at another time. 
7. Your input file (HitTable) is not under the same folder as the data-collection.py script

# fasta-compiler.R 
An R script that removes duplicates and compiles species name, protein accession number and sequences into a fasta file. The output of this script is what will be fed into the alignment programs. 



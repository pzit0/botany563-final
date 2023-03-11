# Project: NHA gene/ protein family in E. affinis and closely related species
This file contains the commands, and outputs of finalized data. 

Get URL for git commit: 
echo "$(git config --get remote.origin.url | sed -e 's/\.git$//g')/commit/$(git rev-parse HEAD)"

## Data: 8 paralogs in E. affinis + curated sequences from other species 
	Currently creating a script to obtain and curate these sequences 
	They will be both DNA (CDS) and protein sequences

## Data Collection: 
### Obtining Paralogs in *E. affinis*: 

## Obtaining Orthologs:  
I will be using BLASTP to find ortholog sequences in other arthropods. 

### Why BLASTP: 
My lab seems to have a couple specific genomes they usually use bc they have already verified their quality (some sequences are really just trash, it is best to not include it if it's false). But in my opinion, blasting against specific taxa seems like a very not effective method to get orthologs. This is because (1) not all these species will have copies of the targetted gene (e.g. Daphnea does not have NHA), which would mean a wasted effort; (2) This means a reduced number of species for my phylogeny - I might not have enough to produce a robust tree; and (3) even in obtaining a blast result for a single specific species, I would still have to check that it came from the desired assembly (this is because some species have more than one assembly available). 

To counter this, I will be blasting my predicted protein sequences against all arthropods and curate those sequences after. This ensures that I will be hitting all species with good quality that have my targetted gene. I am also using protein sequences, as opposed to the CDS sequence, in order to get more results. I have already attempted blasting the CDS (excluding E. affinis, because we already have those sequences) and this search yielded no results. I think this protein might not be very well conserved across many taxa. 

I have limited the organisms to only arthropods because I will need more highly conserved sequences for the hyphy analysis in the future, and I have excluded Eurytemora affinis because we already have those sequences. I have also excluded other sequences as a preventive method for bad quality/ repeats and environmental samples. -> I want to maximize good quality arthropod results.

I am also running this online (on the ncbi server) because I feel that I have better control over these parameters. 

### BLASTP search parameters 
Query: Protein sequences from the file: ~/Desktop/botany563-final/data/paralogs/final-cds/choices/NHA-fam-predicted-protein.fa
Search Set: Standard Databases 
Database: Non-redundant protein sequences (nr) 
Organism: (exclude) Eurytemora affinis (taxid: 88015), (include) Arthropoda (taxid: 6656) 
Exclude: Models (XM/XP), Non-redundant RefSeq proteins (WP), Uncultured/ Envirnomental sample sequences 
Program Selection: blastp (protein-protein BLAST)
Default algorithm parameters (BLOSUM62, etc.) 

Results saved as: 2023-03-08-NHAx-HitTable.csv 

### Curation Proccess 
To curate these results, I will be using my ncbi_parser.py script. It accesses the protein and assembly entries on ncbi and returns me sequences that "pass" my curation parameters. These are: 
min_prot_size = 200 # protein size 
min_coverage = 50 # coverage 
max_count = 9000 # scaffold count 
min_N50 = 10000 # scaffold N50

Example of command for NHA1: 
(base) Patricias-MacBook-Air:botany563-final patriciazito$ python3 ncbi_parser.py 

Hello world! I'm a program to filter through your initial blast results for good quality paralogs

to use me, answer the following:
Name of your BLAST result csv file (e.g. '2023-01-31-NHA1-HitTable.csv'): 2023-03-08-NHA1-HitTable.csv
Your wisc email (e.g. 'jdoe@wisc.edu'): pzito@wisc.edu
Prefix of your output files (e.g. '2023-01-31-NHA1'): 2023-03-08-NHA1   

Terminal output for NHA1: 
################## RUNNING #####################
ASSESSING: Tigriopus californicus TRY75264.1
Tigriopus californicus TRY75264.1 WAS ADDED TO FILTERED
ASSESSING: Trinorchestia longiramus KAF2354193.1
FAILED COVERAGE: 41.0
ASSESSING: Homarus americanus KAG7156541.1
FAILED COUNT: 47246.0
ASSESSING: Homarus americanus KAG7156541.1
ASSESSING: Nymphon striatum KAG1663790.1
Nymphon striatum KAG1663790.1 WAS ADDED TO FILTERED
ASSESSING: Nymphon striatum KAG1663790.1
Nymphon striatum KAG1663790.1 WAS ADDED TO FILTERED
ASSESSING: Schistocerca gregaria QVD39181.1
failed assembly
ASSESSING: Penaeus vannamei ROT75079.1
Penaeus vannamei ROT75079.1 WAS ADDED TO FILTERED
ASSESSING: Nymphon striatum KAG1694105.1
Nymphon striatum KAG1694105.1 WAS ADDED TO FILTERED
ASSESSING: Nymphon striatum KAG1694105.1
Nymphon striatum KAG1694105.1 WAS ADDED TO FILTERED
ASSESSING: Nymphon striatum KAG1663789.1
Nymphon striatum KAG1663789.1 WAS ADDED TO FILTERED
ASSESSING: Nymphon striatum KAG1694104.1
Nymphon striatum KAG1694104.1 WAS ADDED TO FILTERED
ASSESSING: Nymphon striatum KAG1694103.1
Nymphon striatum KAG1694103.1 WAS ADDED TO FILTERED
ASSESSING: Diaphorina citri KAI5736882.1
Diaphorina citri KAI5736882.1 WAS ADDED TO FILTERED
ASSESSING: Diaphorina citri KAI5736882.1
Diaphorina citri KAI5736882.1 WAS ADDED TO FILTERED
ASSESSING: Diaphorina citri KAI5704272.1
Diaphorina citri KAI5704272.1 WAS ADDED TO FILTERED
ASSESSING: Diaphorina citri KAI5704272.1
Diaphorina citri KAI5704272.1 WAS ADDED TO FILTERED
ASSESSING: Diaphorina citri KAI5704273.1
Diaphorina citri KAI5704273.1 WAS ADDED TO FILTERED
ASSESSING: Orchesella cincta ODN02785.1
FAILED COVERAGE: 40.0
ASSESSING: Orchesella cincta ODN02785.1
ASSESSING: Timema californicum CAD7578322.1
FAILED COUNT: 660024.0
ASSESSING: Coptotermes formosanus GFG39584.1
FAILED COVERAGE: 10.0
ASSESSING: Armadillidium vulgare RXG52054.1
FAILED COUNT: 43541.0
ASSESSING: Armadillidium vulgare RXG52054.1
ASSESSING: Darwinula stevensoni CAD7247776.1
FAILED COUNT: 62117.0
ASSESSING: Hyalella azteca KAA0203922.1
FAILED COUNT: 17396.0
ASSESSING: Timema tahoe CAD7456214.1
ASSESSING: Bemisia tabaci CAH0753751.1
FAILED COVERAGE: 40.0
ASSESSING: Zootermopsis nevadensis KDR19311.1
FAILED COUNT: 31663.0
ASSESSING: Darwinula stevensoni CAD7241908.1
ASSESSING: Chionoecetes opilio KAG0726903.1
FAILED COUNT: 26514.0
ASSESSING: Chionoecetes opilio KAG0726903.1
ASSESSING: Idotea baltica MCL4129876.1
FAILED N50: 7966.0
ASSESSING: Cryptotermes secundus PNF40993.1
FAILED COVERAGE: 45.0
ASSESSING: Nymphon striatum KAG1663791.1
Nymphon striatum KAG1663791.1 WAS ADDED TO FILTERED
ASSESSING: Ephemera danica KAF4525946.1
Ephemera danica KAF4525946.1 WAS ADDED TO FILTERED
ASSESSING: Darwinula stevensoni CAD7249112.1
ASSESSING: Blattella germanica PSN35039.1
FAILED COUNT: 24818.0
ASSESSING: Hyalella azteca KAA0201437.1
ASSESSING: Notodromas monacha CAD7274489.1
ASSESSING: Notodromas monacha CAD7274489.1
ASSESSING: Medioppia subpectinata CAD7622824.1
FAILED N50: 7017.0
ASSESSING: Timema cristinae CAD7413317.1
ASSESSING: Nezara viridula CAH1388393.1
Nezara viridula CAH1388393.1 WAS ADDED TO FILTERED
ASSESSING: Bemisia tabaci CAH0381819.1
ASSESSING: Idotea baltica MCL4150668.1
ASSESSING: Coptotermes formosanus GFG28126.1
ASSESSING: Ladona fulva KAG8223872.1
FAILED COUNT: 9411.0
ASSESSING: Nymphon striatum KAG1694102.1
Nymphon striatum KAG1694102.1 WAS ADDED TO FILTERED
ASSESSING: Periplaneta americana KAJ4436481.1
FAILED COVERAGE: 40.0
ASSESSING: Stegodyphus mimosarum KFM61102.1
FAILED COUNT: 68653.0

A total of 51 proteins were assessed
Out of those, 18(0.35294117647058826) were successfully curated and obtained
0 were discarded due to small protein size
1 were discarded due to me not finding its assembly information
6 were discarded due to having bad coverage
2 were discarded due to bad scaffold N50
10 were discarded for having too many scaffolds
14 were already checked and discarded
MINIMUM PROTEIN SIZE =200
MINIMUM COVERAGE =50
MINIMUM SCAFFOLD N50 =10000
MAX SCAFFOLD COUNT =9000

#################################################

Your files have been saved here:  /Users/patriciazito/Desktop/botany563-final


The same has been done for the others. 

(base) Patricias-MacBook-Air:botany563-final patriciazito$ ls
2023-03-08-NHA1-HitTable.csv
2023-03-08-NHA1-filtered.csv
2023-03-08-NHA1-log.txt
2023-03-08-NHA1-trashed.csv
2023-03-08-NHA2-HitTable.csv
2023-03-08-NHA2-filtered.csv
2023-03-08-NHA2-log.txt
2023-03-08-NHA2-trashed.csv
2023-03-08-NHA3-HitTable.csv
2023-03-08-NHA3-filtered.csv
2023-03-08-NHA3-log.txt
2023-03-08-NHA3-trashed.csv
2023-03-08-NHA4-HitTable.csv
2023-03-08-NHA4-filtered.csv
2023-03-08-NHA4-log.txt
2023-03-08-NHA4-trashed.csv
2023-03-08-NHA5-HitTable.csv
2023-03-08-NHA5-filtered.csv
2023-03-08-NHA5-log.txt
2023-03-08-NHA5-trashed.csv
2023-03-08-NHA6-HitTable.csv
2023-03-08-NHA6-filtered.csv
2023-03-08-NHA6-log.txt
2023-03-08-NHA6-trashed.csv
2023-03-08-NHA7-HitTable.csv
2023-03-08-NHA7-filtered.csv
2023-03-08-NHA7-log.txt
2023-03-08-NHA7-trashed.csv
2023-03-08-NHA8-HitTable.csv
2023-03-08-NHA8-filtered.csv
2023-03-08-NHA8-log.txt
2023-03-08-NHA8-trashed.csv
Screen Shot 2023-02-05 at 10.34.16 AM.png
data
distance-parsimony-trees.Rmd
eafff_paralog-protocol.md
fasta-compiler.R
ncbi_parser.py
notebook-log.md
ortholog-search-procedure.md
readme.txt
script-for-later


Compile this data into one single 

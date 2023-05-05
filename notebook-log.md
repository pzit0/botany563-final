# Project: NHA gene/ protein family in E. affinis and closely related species
This file contains the commands, and outputs of finalized data. 

Get URL for git commit: 
echo "$(git config --get remote.origin.url | sed -e 's/\.git$//g')/commit/$(git rev-parse HEAD)"

## Program Installation 
### BLAST: 
Conda install -c bioconda blast

### MAFFT
(base) pzito@IBIO-DRW7N0JQY0 ~ % conda install -c biocore mafft
Collecting package metadata (current_repodata.json): done
Solving environment: done

  environment location: /Users/pzito/anaconda3

  added / updated specs:
    - mafft


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    mafft-7.245                |                0         2.3 MB  biocore
    ------------------------------------------------------------
                                           Total:         2.3 MB

The following NEW packages will be INSTALLED:

  mafft              biocore/osx-64::mafft-7.245-0 


Proceed ([y]/n)? y


Downloading and Extracting Packages
                                                                                                                           
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

### biopython
conda install -c bioconda biopython
pip3 install biopython

### IQTree 
conda install -c bioconda iqtree

### R studio
(Downloaded from website) 

### VSCode 
(Downloaded from website) 

### MacVIM
(Downloaded from website) 

### UGENE 
(Downloaded from website) 

### BEAST 
(Downloaded from website)

## Data: 8 paralogs in E. affinis + curated sequences from other species 
	Currently creating a script to obtain and curate these sequences 
	They will be both DNA (CDS) and protein sequences
    most updated dataframe: /Users/pzito/Desktop/botany563-final/data/orthologs/CURATION4-add-outgroups/orthologs-filtered-CONSERVED+outgroups.csv

## Data Collection: 
### Obtining Paralogs in *E. affinis*: 
BLAST+ partial CDS sequences on transcriptome database 
alignment with genome data - confirmation 
path for protein data: 
/Users/pzito/Desktop/botany563-final/data/paralogs/final-cds-choices/NHA-fam-predicted-protein.fa

path for CDS data: 
/Users/pzito/Desktop/botany563-final/data/paralogs/final-cds-choices/NHA-fam-2023-CDS.fa

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


# MAFFT 
(base) pzito@IBIO-DRW7N0JQY0 CURATION4-add-outgroups % mafft orthologs-filtered-ALL+outgroups.fasta > orthologs-filtered-ALL+outgroups-MAFFT.fasta

nseq =  303
distance =  ktuples
iterate =  0
cycle =  2
sparsepickup = 0
nguidetree = 2
nthread = 0
sueff_global = 0.100000
done.
scoremtx = 1
Gap Penalty = -1.53, +0.00, +0.00

tuplesize = 6, dorp = p


Making a distance matrix ..

There are 10 ambiguous characters.
  301 / 303
done.

Constructing a UPGMA tree ... 
  300 / 303
done.

Progressive alignment 1/2... 
STEP   270 / 302 d
Reallocating..done. *alloclen = 4717
STEP   281 / 302 d
Reallocating..done. *alloclen = 5783
STEP   295 / 302 d
Reallocating..done. *alloclen = 7283
STEP   302 / 302 d
done.

Making a distance matrix from msa.. 
  300 / 303
done.

Constructing a UPGMA tree ... 
  300 / 303
done.

Progressive alignment 2/2... 
STEP   283 / 302 d
Reallocating..done. *alloclen = 4803
STEP   294 / 302 d
Reallocating..done. *alloclen = 6091
STEP   298 / 302 d
Reallocating..done. *alloclen = 7923
STEP   302 / 302 d
done.

disttbfast (aa) Version 7.245 alg=A, model=BLOSUM62, 1.53, -0.00, -0.00, noshift, amax=0.0
0 thread(s)


Strategy:
 FFT-NS-2 (Fast but rough)
 Progressive method (guide trees were built 2 times.)

If unsure which option to use, try 'mafft --auto input > output'.
For more information, see 'mafft --help', 'mafft --man' and the mafft page.

The default gap scoring scheme has been changed in version 7.110 (2013 Oct).
It tends to insert more gaps into gap-rich regions than previous versions.
To disable this change, add the --leavegappyregion option.

(base) pzito@IBIO-DRW7N0JQY0 CURATION4-add-outgroups % mafft orthologs-filtered-CONSERVED+outgroups.fasta > orthologs-filtered-CONSERVED+outgroups-MAFFT.fasta

nseq =  90
distance =  ktuples
iterate =  0
cycle =  2
sparsepickup = 0
nguidetree = 2
nthread = 0
sueff_global = 0.100000
done.
scoremtx = 1
Gap Penalty = -1.53, +0.00, +0.00

tuplesize = 6, dorp = p


Making a distance matrix ..

There are 9 ambiguous characters.
    1 / 90
done.

Constructing a UPGMA tree ... 
   80 / 90
done.

Progressive alignment 1/2... 
STEP    80 / 89 d
Reallocating..done. *alloclen = 3510
STEP    89 / 89 d
done.

Making a distance matrix from msa.. 
   80 / 90
done.

Constructing a UPGMA tree ... 
   80 / 90
done.

Progressive alignment 2/2... 
STEP    80 / 89 d
Reallocating..done. *alloclen = 3492
STEP    89 / 89 d
done.

disttbfast (aa) Version 7.245 alg=A, model=BLOSUM62, 1.53, -0.00, -0.00, noshift, amax=0.0
0 thread(s)


Strategy:
 FFT-NS-2 (Fast but rough)
 Progressive method (guide trees were built 2 times.)

If unsure which option to use, try 'mafft --auto input > output'.
For more information, see 'mafft --help', 'mafft --man' and the mafft page.

The default gap scoring scheme has been changed in version 7.110 (2013 Oct).
It tends to insert more gaps into gap-rich regions than previous versions.
To disable this change, add the --leavegappyregion option.

# Trimming alignments 
Gblocks 0.91b (doc) 
https://ngphylogeny.fr/
unavailable for the less conservative dataframe.

# IQTree 
iqtree -s orthologs-filtered-CONSERVED+outgroups-MAFFT-GBlock.fasta -m TEST -bb 5000 -o H.exemplaris-OQV21679.1 -pre orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree

IQ-TREE multicore version 2.0.3 for Mac OS X 64-bit built Dec 19 2020
Developed by Bui Quang Minh, Nguyen Lam Tung, Olga Chernomor,
Heiko Schmidt, Dominik Schrempf, Michael Woodhams.

Host:    IBIO-DRW7N0JQY0.lan (SSE4.2, 16 GB RAM)
Command: iqtree -s orthologs-filtered-CONSERVED+outgroups-MAFFT-GBlock.fasta -m TEST -bb 5000 -o H.exemplaris-OQV21679.1 -pre orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree
Seed:    507202 (Using SPRNG - Scalable Parallel Random Number Generator)
Time:    Tue May  2 22:50:27 2023
OMP: Info #276: omp_set_nested routine deprecated, please use omp_set_max_active_levels instead.
Kernel:  SSE2 - 1 threads (12 CPU cores detected)

HINT: Use -nt option to specify number of threads because your CPU has 12 cores!
HINT: -nt AUTO will automatically determine the best number of threads to use.

Reading alignment file orthologs-filtered-CONSERVED+outgroups-MAFFT-GBlock.fasta ... Fasta format detected
Alignment most likely contains protein sequences
Alignment has 90 sequences with 308 columns, 307 distinct patterns
294 parsimony-informative, 8 singleton sites, 6 constant sites
WARNING: Some sequence names are changed as follows:
NHA1_prot,size=637,strand=+ -> NHA1_prot_size_637_strand__
NHA2_prot,size=656,strand=+ -> NHA2_prot_size_656_strand__
NHA3_prot,size=1204,strand=+ -> NHA3_prot_size_1204_strand__
NHA4_prot,size=786,strand=+ -> NHA4_prot_size_786_strand__
NHA5_prot,size=754,strand=+ -> NHA5_prot_size_754_strand__
NHA6_prot,size=708,strand=+ -> NHA6_prot_size_708_strand__
NHA7_prot,size=589,strand=- -> NHA7_prot_size_589_strand_-

                               Gap/Ambiguity  Composition  p-value
   1  O.gibbosus-KAG8183784.1          0.00%    passed     86.82%
   2  O.gibbosus-KAG8183783.1          0.32%    passed     95.83%
   3  O.gibbosus-KAG8186330.1          0.32%    passed     95.11%
   4  T.californicus-TRY75264.1        0.00%    passed     69.81%
   5  A.amphitrite-KAF0289584.1        0.00%    failed      0.41%
   6  D.citri-KAI5736882.1             0.65%    passed     97.27%
   7  D.citri-KAI5704272.1             0.65%    passed     97.12%
   8  D.citri-KAI5704273.1             0.65%    passed     97.12%
   9  D.citri-KAI5704273.2             0.00%    passed     94.20%
  10  D.citri-KAI5742900.1             0.00%    passed     94.20%
  11  D.citri-KAI5742064.1             0.00%    passed     55.63%
  12  D.kikuchii-KAJ0181768.1          0.00%    passed     99.96%
  13  D.kikuchii-KAJ0175711.1          0.00%    passed    100.00%
  14  D.kikuchii-KAJ0181766.1          0.32%    passed     11.95%
  15  D.kikuchii-KAJ0181767.1          0.65%    passed      7.93%
  16  S.littoralis-CAB3515165.1        0.00%    passed     99.81%
  17  A.plantaginis-CAB3231150.1       0.00%    passed     99.70%
  18  A.plantaginis-CAB3223254.1       0.00%    passed     99.55%
  19  A.plantaginis-CAB3231154.1       0.32%    passed     28.23%
  20  A.plantaginis-CAB3249883.1       0.32%    passed     32.94%
  21  A.plantaginis-CAB3249884.1       0.32%    passed     54.26%
  22  A.plantaginis-CAB3231153.1       0.32%    passed     54.02%
  23  B.ino-CAH0726637.1               0.00%    passed     96.80%
  24  B.ino-CAH0714536.1               0.00%    passed     97.67%
  25  B.ino-CAH0714537.1               0.00%    passed     97.67%
  26  B.ino-CAH0726632.1               0.65%    passed     16.77%
  27  B.ino-CAH0726633.1               0.65%    passed     16.77%
  28  A.plantaginis-CAB3231151.1       0.00%    passed     99.70%
  29  H.armigera-PZC78836.1            0.00%    passed     93.84%
  30  H.armigera-PZC83667.1            0.00%    passed     98.23%
  31  H.armigera-PZC78838.1            0.65%    passed     15.64%
  32  H.armigera-PZC78839.1            0.32%    passed     42.20%
  33  I.podalirius-CAH2066547.1        3.25%    passed     95.74%
  34  I.podalirius-CAH2066549.1        3.25%    passed     95.74%
  35  I.podalirius-CAH2066551.1        3.25%    passed     95.74%
  36  I.podalirius-CAH2066545.1       93.83%    passed     42.50%
  37  I.podalirius-CAH2066543.1        0.32%    passed     31.74%
  38  I.podalirius-CAH2066541.1        0.32%    passed     31.74%
  39  C.capitata-CAD6994394.1          0.00%    passed     26.19%
  40  L.cuprina-KAI8116404.1           0.00%    passed     37.86%
  41  L.cuprina-KAI8130912.2           0.00%    passed     99.84%
  42  G.fuscipes-KAI9577037.1          0.00%    passed     54.34%
  43  T.longispinosus-TGZ49087.1       0.32%    passed     90.72%
  44  T.longispinosus-TGZ32222.1      15.26%    passed     77.70%
  45  E.burchellii-KAH0956584.1        0.00%    passed     98.64%
  46  C.glomerata-KAH0554196.1         0.00%    passed     92.12%
  47  O.biroi-EZA57806.1               0.00%    passed     96.80%
  48  O.biroi-EZA53303.1               0.00%    passed     16.52%
  49  A.compressa-KAG7201324.1         0.00%    passed     91.63%
  50  A.compressa-KAG7212671.1         0.00%    passed      9.65%
  51  C.congregata-CAG5095999.1        0.00%    passed     95.43%
  52  C.congregata-CAG5097411.1        0.00%    failed      3.15%
  53  A.echinatior-EGI60180.1         14.94%    passed     50.26%
  54  P.vanderplanki-KAG5676603.1      0.00%    passed     99.36%
  55  P.vanderplanki-KAG5676604.1      0.00%    passed     99.36%
  56  E.danica-KAF4525624.1            0.00%    passed     98.23%
  57  C.dipterum-CAB3360254.1          0.00%    passed     99.95%
  58  C.dipterum-CAB3360255.1          6.17%    passed     99.69%
  59  C.dipterum-CAB3360256.1          6.17%    passed     99.69%
  60  C.dipterum-CAB3364807.1          0.00%    passed     96.44%
  61  M.usitatus-KAJ1530995.1          1.62%    failed      0.53%
  62  N.viridula-CAH1388387.1         12.01%    passed     25.88%
  63  N.viridula-CAH1388367.1          0.00%    passed     67.87%
  64  A.lucorum-KAF6214444.1           0.00%    passed     83.99%
  65  A.lucorum-KAF6215170.1           0.00%    passed     98.07%
  66  V.vulgaris-KAF7383363.1          0.00%    passed     86.16%
  67  C.dipterum-CAB3360254.1_0001     0.00%    passed     99.95%
  68  D.melanogaster-NM_001260322.1    0.00%    passed     41.45%
  69  D.melanogaster-NP_723224.2       0.00%    passed     99.37%
  70  A.gambiae-EF014219.1             0.00%    passed     98.96%
  71  L.salmonis-XM_040711500.1        0.00%    passed     84.77%
  72  P.americana-KAJ4436481.1         0.00%    passed     98.21%
  73  P.americana-KAJ4439351.1         0.00%    passed     89.70%
  74  P.americana-KAJ4436265.1         0.00%    passed     63.60%
  75  E.sinensis-XP_050686642.1        0.00%    passed     22.40%
  76  O.nitens-XP_054156261.1          0.65%    passed     96.28%
  77  O.nitens-XP_054156387.1          0.65%    passed     90.66%
  78  O.nitens-XP_054169184.1          0.00%    failed      0.00%
  79  H.exemplaris-OQV21679.1          0.00%    passed     64.91%
  80  R.varieornatus-GAU92661.1        0.00%    passed     71.67%
  81  H.exemplaris-OQV26214.1          0.00%    passed     58.54%
  82  R.varieornatus-GAV01898.1        0.00%    passed     39.28%
  83  R.varieornatus-GAV01897.1       42.86%    passed     70.56%
  84  NHA1_prot_size_637_strand__      0.00%    passed     86.33%
  85  NHA2_prot_size_656_strand__      0.00%    passed     90.03%
  86  NHA3_prot_size_1204_strand__     0.00%    passed     87.04%
  87  NHA4_prot_size_786_strand__      0.00%    passed     86.37%
  88  NHA5_prot_size_754_strand__      0.00%    passed     48.58%
  89  NHA6_prot_size_708_strand__      0.00%    passed     32.47%
  90  NHA7_prot_size_589_strand_-      0.00%    passed     63.89%
WARNING: 1 sequences contain more than 50% gaps/ambiguity
****  TOTAL                            2.36%  4 sequences failed composition chi2 test (p-value<5%; df=19)
NOTE: D.citri-KAI5704273.1 is identical to D.citri-KAI5704272.1 but kept for subsequent analysis
NOTE: D.citri-KAI5742900.1 is identical to D.citri-KAI5704273.2 but kept for subsequent analysis
NOTE: A.plantaginis-CAB3231151.1 is identical to A.plantaginis-CAB3231150.1 but kept for subsequent analysis
NOTE: B.ino-CAH0714537.1 is identical to B.ino-CAH0714536.1 but kept for subsequent analysis
NOTE: B.ino-CAH0726633.1 is identical to B.ino-CAH0726632.1 but kept for subsequent analysis
NOTE: I.podalirius-CAH2066549.1 is identical to I.podalirius-CAH2066547.1 but kept for subsequent analysis
NOTE: I.podalirius-CAH2066541.1 is identical to I.podalirius-CAH2066543.1 but kept for subsequent analysis
NOTE: P.vanderplanki-KAG5676604.1 is identical to P.vanderplanki-KAG5676603.1 but kept for subsequent analysis
NOTE: C.dipterum-CAB3360254.1_0001 is identical to C.dipterum-CAB3360254.1 but kept for subsequent analysis
NOTE: C.dipterum-CAB3360256.1 is identical to C.dipterum-CAB3360255.1 but kept for subsequent analysis
NOTE: 1 identical sequences (see below) will be ignored for subsequent analysis
NOTE: I.podalirius-CAH2066551.1 (identical to I.podalirius-CAH2066547.1) is ignored but added at the end
Alignment was printed to orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.uniqueseq.phy

For your convenience alignment with unique sequences printed to orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.uniqueseq.phy


Create initial parsimony tree by phylogenetic likelihood library (PLL)... 0.010 seconds
Perform fast likelihood tree search using LG+I+G model...
Estimate model parameters (epsilon = 5.000)
Perform nearest neighbor interchange...
Estimate model parameters (epsilon = 1.000)
1. Initial log-likelihood: -23334.372
Optimal log-likelihood: -23334.356
Proportion of invariable sites: 0.011
Gamma shape alpha: 1.386
Parameters optimization took 1 rounds (0.174 sec)
Time for fast ML tree search: 1.994 seconds

NOTE: ModelFinder requires 24 MB RAM!
ModelFinder will test up to 168 protein models (sample size: 308) ...
 No. Model         -LnL         df  AIC          AICc         BIC
  1  LG            24186.936    175 48723.872    49190.539    49376.640
  2  LG+I          24134.202    176 48620.405    49096.008    49276.902
  3  LG+G4         23337.244    176 47026.488    47502.091    47682.986
  4  LG+I+G4       23334.360    177 47022.719    47507.427    47682.947
  7  LG+F+G4       23057.883    195 46505.767    47188.267    47233.136
  8  LG+F+I+G4     23058.019    196 46508.038    47203.749    47239.137
 11  WAG+G4        23667.889    176 47687.778    48163.381    48344.275
 12  WAG+I+G4      23663.115    177 47680.231    48164.938    48340.458
 15  WAG+F+G4      23215.845    195 46821.691    47504.191    47549.060
 16  WAG+F+I+G4    23215.706    196 46823.412    47519.123    47554.511
 19  JTT+G4        23672.008    176 47696.016    48171.619    48352.513
 20  JTT+I+G4      23667.207    177 47688.413    48173.121    48348.641
 23  JTT+F+G4      23284.675    195 46959.350    47641.850    47686.720
 24  JTT+F+I+G4    23284.525    196 46961.050    47656.762    47692.150
 27  JTTDCMut+G4   23680.350    176 47712.700    48188.304    48369.198
 28  JTTDCMut+I+G4 23675.639    177 47705.278    48189.986    48365.506
 31  JTTDCMut+F+G4 23283.910    195 46957.821    47640.321    47685.190
 32  JTTDCMut+F+I+G4 23283.786    196 46959.573    47655.285    47690.672
 35  DCMut+G4      23983.115    176 48318.230    48793.833    48974.727
 36  DCMut+I+G4    23979.329    177 48312.658    48797.366    48972.886
 39  DCMut+F+G4    23437.978    195 47265.955    47948.455    47993.325
 40  DCMut+F+I+G4  23438.000    196 47268.000    47963.712    47999.100
 43  VT+G4         23710.583    176 47773.166    48248.769    48429.663
 44  VT+I+G4       23706.040    177 47766.079    48250.787    48426.307
 47  VT+F+G4       23302.351    195 46994.702    47677.202    47722.072
 48  VT+F+I+G4     23301.987    196 46995.973    47691.685    47727.073
 51  PMB+G4        23720.278    176 47792.555    48268.158    48449.053
 52  PMB+I+G4      23716.611    177 47787.221    48271.929    48447.449
 55  PMB+F+G4      23502.027    195 47394.054    48076.554    48121.423
 56  PMB+F+I+G4    23501.766    196 47395.532    48091.244    48126.632
 59  Blosum62+G4   23701.294    176 47754.589    48230.192    48411.086
 60  Blosum62+I+G4 23697.598    177 47749.197    48233.904    48409.424
 63  Blosum62+F+G4 23426.938    195 47243.876    47926.376    47971.245
 64  Blosum62+F+I+G4 23426.419    196 47244.837    47940.549    47975.937
 67  Dayhoff+G4    23980.554    176 48313.108    48788.711    48969.606
 68  Dayhoff+I+G4  23976.788    177 48307.576    48792.284    48967.804
 71  Dayhoff+F+G4  23436.296    195 47262.592    47945.092    47989.961
 72  Dayhoff+F+I+G4 23436.324    196 47264.648    47960.360    47995.748
 75  mtREV+G4      24056.605    176 48465.211    48940.814    49121.709
 76  mtREV+I+G4    24056.593    177 48467.185    48951.893    49127.413
 79  mtREV+F+G4    23357.002    195 47104.004    47786.504    47831.373
 80  mtREV+F+I+G4  23357.032    196 47106.064    47801.776    47837.163
 83  mtART+G4      23693.535    176 47739.070    48214.673    48395.568
 84  mtART+I+G4    23693.529    177 47741.058    48225.765    48401.285
 87  mtART+F+G4    23374.809    195 47139.618    47822.118    47866.988
 88  mtART+F+I+G4  23374.785    196 47141.569    47837.281    47872.669
 91  mtZOA+G4      23239.110    176 46830.220    47305.823    47486.718
 92  mtZOA+I+G4    23239.151    177 46832.303    47317.011    47492.530
 95  mtZOA+F+G4    23157.200    195 46704.400    47386.900    47431.770
 96  mtZOA+F+I+G4  23157.248    196 46706.495    47402.207    47437.595
 99  mtMet+G4      23682.905    176 47717.810    48193.413    48374.308
100  mtMet+I+G4    23683.016    177 47720.031    48204.739    48380.259
103  mtMet+F+G4    23277.709    195 46945.418    47627.918    47672.787
104  mtMet+F+I+G4  23277.759    196 46947.518    47643.230    47678.618
107  mtVer+G4      24153.386    176 48658.773    49134.376    49315.270
108  mtVer+I+G4    24153.425    177 48660.851    49145.559    49321.079
111  mtVer+F+G4    23580.149    195 47550.298    48232.798    48277.667
112  mtVer+F+I+G4  23580.172    196 47552.343    48248.055    48283.443
115  mtInv+G4      23699.421    176 47750.843    48226.446    48407.341
116  mtInv+I+G4    23699.508    177 47753.017    48237.724    48413.244
119  mtInv+F+G4    23137.257    195 46664.515    47347.015    47391.884
120  mtInv+F+I+G4  23137.371    196 46666.743    47362.455    47397.843
123  mtMAM+G4      24472.080    176 49296.161    49771.764    49952.658
124  mtMAM+I+G4    24472.088    177 49298.176    49782.884    49958.403
127  mtMAM+F+G4    23829.839    195 48049.677    48732.177    48777.047
128  mtMAM+F+I+G4  23829.841    196 48051.682    48747.394    48782.782
131  HIVb+G4       24196.179    176 48744.358    49219.961    49400.855
132  HIVb+I+G4     24186.424    177 48726.847    49211.555    49387.075
135  HIVb+F+G4     23709.075    195 47808.150    48490.650    48535.519
136  HIVb+F+I+G4   23708.265    196 47808.529    48504.241    48539.629
139  HIVw+G4       25429.777    176 51211.554    51687.157    51868.052
140  HIVw+I+G4     25419.421    177 51192.841    51677.549    51853.069
143  HIVw+F+G4     24603.218    195 49596.435    50278.935    50323.805
144  HIVw+F+I+G4   24601.323    196 49594.647    50290.358    50325.746
147  FLU+G4        24230.271    176 48812.542    49288.145    49469.040
148  FLU+I+G4      24223.710    177 48801.421    49286.128    49461.648
151  FLU+F+G4      23764.343    195 47918.687    48601.187    48646.056
152  FLU+F+I+G4    23764.453    196 47920.907    48616.618    48652.006
155  rtREV+G4      23788.208    176 47928.417    48404.020    48584.914
156  rtREV+I+G4    23785.141    177 47924.281    48408.989    48584.509
159  rtREV+F+G4    23197.659    195 46785.318    47467.818    47512.688
160  rtREV+F+I+G4  23197.788    196 46787.576    47483.288    47518.676
163  cpREV+G4      23541.785    176 47435.571    47911.174    48092.068
164  cpREV+I+G4    23533.979    177 47421.957    47906.665    48082.185
167  cpREV+F+G4    23189.550    195 46769.100    47451.600    47496.469
168  cpREV+F+I+G4  23188.648    196 46769.296    47465.008    47500.396
Akaike Information Criterion:           LG+F+G4
Corrected Akaike Information Criterion: LG+F+G4
Bayesian Information Criterion:         LG+F+G4
Best-fit model: LG+F+G4 chosen according to BIC

All model information printed to orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.model.gz
CPU time for ModelFinder: 61.740 seconds (0h:1m:1s)
Wall-clock time for ModelFinder: 62.613 seconds (0h:1m:2s)
Generating 5000 samples for ultrafast bootstrap (seed: 507202)...

NOTE: 24 MB RAM (0 GB) is required!
Estimate model parameters (epsilon = 0.100)
1. Initial log-likelihood: -23057.883
Optimal log-likelihood: -23057.882
Gamma shape alpha: 1.191
Parameters optimization took 1 rounds (0.157 sec)
Computing ML distances based on estimated model parameters... 0.540 sec
WARNING: Some pairwise ML distances are too long (saturated)
Computing BIONJ tree...
0.003 seconds
Log-likelihood of BIONJ tree: -23100.117
--------------------------------------------------------------------
|             INITIALIZING CANDIDATE TREE SET                      |
--------------------------------------------------------------------
Generating 98 parsimony trees... 1.296 second
Computing log-likelihood of 98 initial trees ... 5.182 seconds
Current best score: -23057.882

Do NNI search on 20 best initial trees
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 1: -23040.095
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 2: -23025.004
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 4: -23023.656
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 9: -23021.126
Iteration 10 / LogL: -23065.530 / Time: 0h:0m:19s
Iteration 20 / LogL: -23047.777 / Time: 0h:0m:31s
Finish initializing candidate tree set (19)
Current best tree score: -23021.126 / CPU time: 30.855
Number of iterations: 20
--------------------------------------------------------------------
|               OPTIMIZING CANDIDATE TREE SET                      |
--------------------------------------------------------------------
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 27: -23020.721
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 28: -23020.253
Iteration 30 / LogL: -23020.254 / Time: 0h:0m:46s (0h:2m:37s left)
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 40: -23020.227
Iteration 40 / LogL: -23020.227 / Time: 0h:1m:1s (0h:2m:37s left)
Iteration 50 / LogL: -23055.710 / Time: 0h:1m:15s (0h:2m:18s left)
Log-likelihood cutoff on original alignment: -23078.819
Iteration 60 / LogL: -23038.802 / Time: 0h:1m:30s (0h:2m:2s left)
Iteration 70 / LogL: -23035.953 / Time: 0h:1m:44s (0h:1m:46s left)
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 75: -23020.161
Iteration 80 / LogL: -23020.686 / Time: 0h:1m:59s (0h:2m:23s left)
Iteration 90 / LogL: -23020.664 / Time: 0h:2m:14s (0h:2m:7s left)
Iteration 100 / LogL: -23022.635 / Time: 0h:2m:28s (0h:1m:52s left)
Log-likelihood cutoff on original alignment: -23078.819
NOTE: Bootstrap correlation coefficient of split occurrence frequencies: 0.999
Iteration 110 / LogL: -23027.912 / Time: 0h:2m:43s (0h:2m:15s left)
Iteration 120 / LogL: -23020.161 / Time: 0h:2m:59s (0h:2m:0s left)
Iteration 130 / LogL: -23020.264 / Time: 0h:3m:14s (0h:1m:45s left)
Iteration 140 / LogL: -23023.909 / Time: 0h:3m:29s (0h:1m:30s left)
Iteration 150 / LogL: -23020.237 / Time: 0h:3m:43s (0h:1m:14s left)
Log-likelihood cutoff on original alignment: -23076.565
Iteration 160 / LogL: -23020.230 / Time: 0h:3m:58s (0h:1m:0s left)
Iteration 170 / LogL: -23033.000 / Time: 0h:4m:13s (0h:0m:44s left)
TREE SEARCH COMPLETED AFTER 176 ITERATIONS / Time: 0h:4m:22s

--------------------------------------------------------------------
|                    FINALIZING TREE SEARCH                        |
--------------------------------------------------------------------
Performs final model parameters optimization
Estimate model parameters (epsilon = 0.010)
1. Initial log-likelihood: -23020.161
Optimal log-likelihood: -23020.161
Gamma shape alpha: 1.167
Parameters optimization took 1 rounds (0.153 sec)
BEST SCORE FOUND : -23020.161
Creating bootstrap support values...
Split supports printed to NEXUS file orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.splits.nex
Total tree length: 29.591

Total number of iterations: 176
CPU time used for tree search: 259.726 sec (0h:4m:19s)
Wall-clock time used for tree search: 261.301 sec (0h:4m:21s)
Total CPU time used: 261.403 sec (0h:4m:21s)
Total wall-clock time used: 263.004 sec (0h:4m:23s)

Computing bootstrap consensus tree...
Reading input file orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.splits.nex...
89 taxa and 586 splits.
Consensus tree written to orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.contree
Reading input trees file orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.contree
Log-likelihood of consensus tree: -23020.272

Analysis results written to: 
  IQ-TREE report:                orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.iqtree
  Maximum-likelihood tree:       orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.treefile
  Likelihood distances:          orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.mldist

Ultrafast bootstrap approximation results written to:
  Split support values:          orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.splits.nex
  Consensus tree:                orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.contree
  Screen log file:               orthologs-filtered-CONSERVED-MAFFT-GBlock-iqtree.log

Date and Time: Tue May  2 22:55:53 2023

# BEAST 
ran on SD server. https://www.phylo.org/portal2/data!list.action?id=645117
Parameters: xml file 
data type: protein 
min number of sequences for a conserved position (b1): default 
min number of sequences for a flank position (b2): default 
max number of contiguous non-conserved positions (b3): 8
min length of a block (b4): 10
allowed gap positions (b5): with half 

# for the less stringent dataframe 
iqtree -s orthologs-filtered-ALL+outgroups-MAFFT.fasta -m TEST -bb 5000 -o H.exemplaris-OQV21679.1 -pre orthologs-filtered-ALL-MAFFT-iqtree

does not work. need to change the fasta file names. 

# March 21, 2023: Making sure these are NHAs
## possible ways to go about this: ortholog finders or alignment 
I've talked with Claudia and it would be possible to use the orthology finders we saw in class, (in theory they should work), but there's still a possiblity they might not be super accurate. I assume even more so because these have already been filtered during BLASTing, so they are pretty similar sequences to NHA. So I'm thinking I'll have to align every one of my current sequences to NHA and NHE and compare their scores. 

I don't want to have to run these on T-coffee, and they are pairwise alignments so this is what I'm thinking of doing: 
1. make an R script file and import my fasta sequences along with a reference NHA and NHE (probably Drosophila)
2. then make a for loop and keep scores in a table, and general variables in a vector 
3. I can then compare and select for the rows where the score for NHA was higher than for NHE. (Also see the alignments, so that's good). 

Best thing is: I can do this with the protein sequences, so I have to look for the CDS sequences of only "confirmed" NHA sequences. 
Link: https://a-little-book-of-r-for-bioinformatics.readthedocs.io/en/latest/src/chapter4.html#:~:text=The%20%E2%80%9CpairwiseAlignment()%E2%80%9D%20function%20in,given%20a%20particular%20scoring%20system.

I think Nick did things differently. He looked for a specific motif present only in NHA. Honestly, if I was to do that, it sounds like I'd have to blast each sequence, which sounds absolutely disgusting so. Let's try the R thing first. 

# March 13, 2023: Number of species + meeting comments 
## number of taxa 
command: 
dim(data%>%select(species)%>%distinct())

output: 
46

## yesterday's meeting comments
- Bad phylogeny. all over the place. might be due to some of the "ortholog" automated sequences actually being NHE. 
Maybe align those sequences with a certain NHE and NHA and see which ones they fit the best
I think Nick also used a specific motif to confirm the identity of the gene. 
- Another thing about the alignments. Maybe there are frameshifts in the alignment. 
access it manually and check if there could be a better alignment. 


# March 12, 2023: FINALLY. NEW FILTERED.CSV JUST DROPPED YO.
idk why but whenever I don't fail the url node8 thing, one of the entries keeps getting me in trouble: 
error message: 

ASSESSING: Anopheles gambiae str. PEST EAL39028.2
Traceback (most recent call last):
  File "ncbi_parser.py", line 316, in <module>
    filtered, trashed, log = filter(acc_list)
  File "ncbi_parser.py", line 209, in filter
    ass_ncbi(row) # get assembly info
  File "ncbi_parser.py", line 167, in ass_ncbi
    cov =  float(re.findall(r'\d+', assembly_dict['Coverage'])[0]) # in case cov had an x string in it 
IndexError: list index out of range

I think I'll just remove the last protein that gave me an issue + the following one.

Log: 
A total of 214 proteins were assessed
Out of those, 73(0.3411214953271028) were successfully curated and obtained
0 were discarded due to small protein size
3 were discarded due to me not finding its assembly information
35 were discarded due to having bad coverage
2 were discarded due to bad scaffold N50
28 were discarded for having too many scaffolds
73 were already checked and discarded
MINIMUM PROTEIN SIZE =200
MINIMUM COVERAGE =50
MINIMUM SCAFFOLD N50 =10000
MAX SCAFFOLD COUNT =9000

## Removing these two rows: 
"175","AAF80554.1","EAL39028.2",80.74,1054,154,13,142,1157,122,1164,0,1663,85.48
"176","AAF80554.1","AAO34131.1",80.645,1054,154,14,142,1157,122,1163,0,1656,85.39

I can manually check these if need be.

## Prelim alignment 
I'm aligning only the protein sequence to get trees for the abstract submission, and I can think about collecting the CDS sequences later (in a week or so).

just used fasta-compiler.R to create the fasta file. 
Adding Eaff at the end of this fasta file. 

now running t_coffee. 

(base) Patricias-Air:data patriciazito$ t_coffee 2023-03-12-protein_sequence_orthologs.fasta

PROGRAM: T-COFFEE Version_13.45.0.4846264 (2020-10-15 17:52:11 - Revision 5becd5d - Build 620)
-full_log      	S	[0] 
-genepred_score	S	[0] 	nsd
-run_name      	S	[0] 
-mem_mode      	S	[0] 	mem
-extend        	D	[1] 	1 
-extend_mode   	S	[0] 	very_fast_triplet
-max_n_pair    	D	[0] 	10 
-seq_name_for_quadruplet	S	[0] 	all
-compact       	S	[0] 	default
-clean         	S	[0] 	no
-do_self       	FL	[0] 	0
-do_normalise  	D	[0] 	1000 
-template_file 	S	[0] 
-setenv        	S	[0] 	0
-export        	S	[0] 	0
-template_mode 	S	[0] 
-flip          	D	[0] 	0 
-remove_template_file	D	[0] 	0 
-profile_template_file	S	[0] 
-in            	S	[0] 
-seq           	S	[1] 	2023-03-12-protein_sequence_orthologs.fasta
-aln           	S	[0] 
-method_limits 	S	[0] 
-method        	S	[0] 
-lib           	S	[0] 
-profile       	S	[0] 
-profile1      	S	[0] 
-profile2      	S	[0] 
-pdb           	S	[0] 
-relax_lib     	D	[0] 	1 
-filter_lib    	D	[0] 	0 
-shrink_lib    	D	[0] 	0 
-out_lib       	W_F	[0] 	no
-out_lib_mode  	S	[0] 	primary
-lib_only      	D	[0] 	0 
-outseqweight  	W_F	[0] 	no
-seq_source    	S	[0] 	ANY
-cosmetic_penalty	D	[0] 	0 
-gapopen       	D	[0] 	0 
-gapext        	D	[0] 	0 
-fgapopen      	D	[0] 	0 
-fgapext       	D	[0] 	0 
-nomatch       	D	[0] 	0 
-newtree       	W_F	[0] 	default
-tree          	W_F	[0] 	NO
-usetree       	R_F	[0] 
-tree_mode     	S	[0] 	nj
-distance_matrix_mode	S	[0] 	ktup
-distance_matrix_sim_mode	S	[0] 	idmat_sim1
-quicktree     	FL	[0] 	0
-outfile       	W_F	[0] 	default
-maximise      	FL	[1] 	1
-output        	S	[0] 	aln	html
-len           	D	[0] 	0 
-infile        	R_F	[0] 
-matrix        	S	[0] 	default
-tg_mode       	D	[0] 	1 
-profile_mode  	S	[0] 	cw_profile_profile
-profile_comparison	S	[0] 	profile
-dp_mode       	S	[0] 	linked_pair_wise
-ktuple        	D	[0] 	1 
-ndiag         	D	[0] 	0 
-diag_threshold	D	[0] 	0 
-diag_mode     	D	[0] 	0 
-sim_matrix    	S	[0] 	vasiliky
-transform     	S	[0] 
-extend_seq    	FL	[0] 	0
-outorder      	S	[0] 	input
-inorder       	S	[0] 	aligned
-seqnos        	S	[0] 	off
-case          	S	[0] 	keep
-cpu           	D	[0] 	0 
-ulimit        	D	[0] 	-1 
-maxnseq       	D	[0] 	-1 
-maxlen        	D	[0] 	-1 
-sample_dp     	D	[0] 	0 
-weight        	S	[0] 	default
-seq_weight    	S	[0] 	no
-align         	FL	[1] 	1
-mocca         	FL	[0] 	0
-domain        	FL	[0] 	0
-start         	D	[0] 	0 
-len           	D	[0] 	0 
-scale         	D	[0] 	0 
-mocca_interactive	FL	[0] 	0
-method_evaluate_mode	S	[0] 	default
-color_mode    	S	[0] 	new
-aln_line_length	D	[0] 	0 
-evaluate_mode 	S	[0] 	triplet
-get_type      	FL	[0] 	0
-clean_aln     	D	[0] 	0 
-clean_threshold	D	[1] 	1 
-clean_iteration	D	[1] 	1 
-clean_evaluate_mode	S	[0] 	t_coffee_fast
-extend_matrix 	FL	[0] 	0
-prot_min_sim  	D	[0] 	0 
-prot_max_sim  	D	[100] 	100 
-psiJ          	D	[0] 	3 
-psitrim_mode  	S	[0] 	regtrim
-psitrim_tree  	S	[0] 	codnd
-psitrim       	D	[100] 	100 
-prot_min_cov  	D	[90] 	90 
-pdb_type      	S	[0] 	d
-pdb_min_sim   	D	[35] 	35 
-pdb_max_sim   	D	[100] 	100 
-pdb_min_cov   	D	[50] 	50 
-pdb_blast_server	W_F	[0] 	EBI
-blast         	W_F	[0] 
-blast_server  	W_F	[0] 	EBI
-pdb_db        	W_F	[0] 	pdb
-protein_db    	W_F	[0] 	uniref50
-method_log    	W_F	[0] 	no
-struc_to_use  	S	[0] 
-cache         	W_F	[0] 	use
-print_cache   	FL	[0] 	0
-align_pdb_param_file	W_F	[0] 	no
-align_pdb_hasch_mode	W_F	[0] 	hasch_ca_trace_bubble
-external_aligner	S	[0] 	NO
-msa_mode      	S	[0] 	tree
-et_mode       	S	[0] 	et
-master        	S	[0] 	no
-blast_nseq    	D	[0] 	0 
-lalign_n_top  	D	[0] 	10 
-iterate       	D	[0] 	0 
-trim          	D	[0] 	0 
-split         	D	[0] 	0 
-trimfile      	S	[0] 	default
-split         	D	[0] 	0 
-split_nseq_thres	D	[0] 	0 
-split_score_thres	D	[0] 	0 
-check_pdb_status	D	[0] 	0 
-clean_seq_name	D	[0] 	0 
-seq_to_keep   	S	[0] 
-dpa_master_aln	S	[0] 
-dpa_maxnseq   	D	[0] 	0 
-dpa_min_score1	D	[0] 
-dpa_min_score2	D	[0] 
-dpa_keep_tmpfile	FL	[0] 	0
-dpa_debug     	D	[0] 	0 
-multi_core    	S	[0] 	templates_jobs_relax_msa_evaluate
-n_core        	D	[0] 	1 
-thread        	D	[0] 	1 
-max_n_proc    	D	[0] 	1 
-lib_list      	S	[0] 
-prune_lib_mode	S	[0] 	5
-tip           	S	[0] 	none
-rna_lib       	S	[0] 
-no_warning    	D	[0] 	0 
-run_local_script	D	[0] 	0 
-proxy         	S	[0] 	unset
-email         	S	[0] 
-clean_overaln 	D	[0] 	0 
-overaln_param 	S	[0] 
-overaln_mode  	S	[0] 
-overaln_model 	S	[0] 
-overaln_threshold	D	[0] 	0 
-overaln_target	D	[0] 	0 
-overaln_P1    	D	[0] 	0 
-overaln_P2    	D	[0] 	0 
-overaln_P3    	D	[0] 	0 
-overaln_P4    	D	[0] 	0 
-exon_boundaries	S	[0] 
-display       	D	[0] 	100 

INPUT FILES
	Input File (S) 2023-03-12-protein_sequence_orthologs.fasta  Format fasta_seq
	Input File (M) proba_pair 

pid 84738 -- Sequence Nymphon is duplicated in file 2023-03-12-protein_sequence_orthologs.fasta. The sequence will be renamed

Identify Master Sequences [no]:

Master Sequences Identified
INPUT SEQUENCES: 81 SEQUENCES  [PROTEIN]
	Multi Core Mode (read): 1 processor(s):

	--- Process Method/Library/Aln S2023-03-12-protein_sequence_orthologs.fasta
	xxx Retrieved S2023-03-12-protein_sequence_orthologs.fasta
	--- Process Method/Library/Aln Mproba_pair
	xxx Retrieved Mproba_pair

	All Methods Retrieved

MANUAL PENALTIES: gapopen=0 gapext=0

	Library Total Size: [12714362]

Library Relaxation: Multi_proc [1]
 
!		[Relax Library][TOT=   81][  6 %][EST. REMAINING TIME:   15 sec.!		[Relax Library][TOT=   81][  7 %][EST. REMAINING TIME:   13 sec.!		[Relax Library][TOT=   81][  8 %][EST. REMAINING TIME:   11 sec.!		[Relax Library][TOT=   81][  9 %][EST. REMAINING TIME:   20 sec.!		[Relax Library][TOT=   81][ 11 %][EST. REMAINING TIME:   16 sec.!		[Relax Library][TOT=   81][ 12 %][EST. REMAINING TIME:   14 sec.!		[Relax Library][TOT=   81][ 13 %][EST. REMAINING TIME:   20 sec.!		[Relax Library][TOT=   81][ 14 %][EST. REMAINING TIME:   18 sec.!		[Relax Library][TOT=   81][ 16 %][EST. REMAINING TIME:   15 sec.!		[Relax Library][TOT=   81][ 17 %][EST. REMAINING TIME:   19 sec.!		[Relax Library][TOT=   81][ 18 %][EST. REMAINING TIME:   18 sec.!		[Relax Library][TOT=   81][ 19 %][EST. REMAINING TIME:   17 sec.!		[Relax Library][TOT=   81][ 20 %][EST. REMAINING TIME:   16 sec.!		[Relax Library][TOT=   81][ 22 %][EST. REMAINING TIME:   17 sec.!		[Relax Library][TOT=   81][ 23 %][EST. REMAINING TIME:   16 sec.!		[Relax Library][TOT=   81][ 24 %][EST. REMAINING TIME:   15 sec.!		[Relax Library][TOT=   81][ 25 %][EST. REMAINING TIME:   18 sec.!		[Relax Library][TOT=   81][ 27 %][EST. REMAINING TIME:   16 sec.!		[Relax Library][TOT=   81][ 28 %][EST. REMAINING TIME:   15 sec.!		[Relax Library][TOT=   81][ 29 %][EST. REMAINING TIME:   17 sec.!		[Relax Library][TOT=   81][ 30 %][EST. REMAINING TIME:   16 sec.!		[Relax Library][TOT=   81][ 32 %][EST. REMAINING TIME:   14 sec.!		[Relax Library][TOT=   81][ 33 %][EST. REMAINING TIME:   14 sec.!		[Relax Library][TOT=   81][ 34 %][EST. REMAINING TIME:   15 sec.!		[Relax Library][TOT=   81][ 35 %][EST. REMAINING TIME:   14 sec.!		[Relax Library][TOT=   81][ 37 %][EST. REMAINING TIME:   13 sec.!		[Relax Library][TOT=   81][ 38 %][EST. REMAINING TIME:   14 sec.!		[Relax Library][TOT=   81][ 39 %][EST. REMAINING TIME:   14 sec.!		[Relax Library][TOT=   81][ 40 %][EST. REMAINING TIME:   13 sec.!		[Relax Library][TOT=   81][ 41 %][EST. REMAINING TIME:   14 sec.!		[Relax Library][TOT=   81][ 43 %][EST. REMAINING TIME:   13 sec.!		[Relax Library][TOT=   81][ 44 %][EST. REMAINING TIME:   12 sec.!		[Relax Library][TOT=   81][ 45 %][EST. REMAINING TIME:   13 sec.!		[Relax Library][TOT=   81][ 46 %][EST. REMAINING TIME:   12 sec.!		[Relax Library][TOT=   81][ 48 %][EST. REMAINING TIME:   13 sec.!		[Relax Library][TOT=   81][ 49 %][EST. REMAINING TIME:   12 sec.!		[Relax Library][TOT=   81][ 50 %][EST. REMAINING TIME:   12 sec.!		[Relax Library][TOT=   81][ 51 %][EST. REMAINING TIME:   12 sec.!		[Relax Library][TOT=   81][ 53 %][EST. REMAINING TIME:   11 sec.!		[Relax Library][TOT=   81][ 54 %][EST. REMAINING TIME:   11 sec.!		[Relax Library][TOT=   81][ 55 %][EST. REMAINING TIME:   11 sec.!		[Relax Library][TOT=   81][ 56 %][EST. REMAINING TIME:   11 sec.!		[Relax Library][TOT=   81][ 58 %][EST. REMAINING TIME:   10 sec.!		[Relax Library][TOT=   81][ 59 %][EST. REMAINING TIME:   10 sec.!		[Relax Library][TOT=   81][ 60 %][EST. REMAINING TIME:   10 sec.!		[Relax Library][TOT=   81][ 61 %][EST. REMAINING TIME:    9 sec.!		[Relax Library][TOT=   81][ 62 %][EST. REMAINING TIME:    9 sec.!		[Relax Library][TOT=   81][ 64 %][EST. REMAINING TIME:    9 sec.!		[Relax Library][TOT=   81][ 65 %][EST. REMAINING TIME:    8 sec.!		[Relax Library][TOT=   81][ 66 %][EST. REMAINING TIME:    8 sec.!		[Relax Library][TOT=   81][ 67 %][EST. REMAINING TIME:    8 sec.!		[Relax Library][TOT=   81][ 69 %][EST. REMAINING TIME:    7 sec.!		[Relax Library][TOT=   81][ 70 %][EST. REMAINING TIME:    7 sec.!		[Relax Library][TOT=   81][ 71 %][EST. REMAINING TIME:    7 sec.!		[Relax Library][TOT=   81][ 72 %][EST. REMAINING TIME:    7 sec.!		[Relax Library][TOT=   81][ 74 %][EST. REMAINING TIME:    6 sec.!		[Relax Library][TOT=   81][ 75 %][EST. REMAINING TIME:    6 sec.!		[Relax Library][TOT=   81][ 76 %][EST. REMAINING TIME:    6 sec.!		[Relax Library][TOT=   81][ 77 %][EST. REMAINING TIME:    5 sec.!		[Relax Library][TOT=   81][ 79 %][EST. REMAINING TIME:    5 sec.!		[Relax Library][TOT=   81][ 80 %][EST. REMAINING TIME:    5 sec.!		[Relax Library][TOT=   81][ 81 %][EST. REMAINING TIME:    4 sec.!		[Relax Library][TOT=   81][ 82 %][EST. REMAINING TIME:    4 sec.!		[Relax Library][TOT=   81][ 83 %][EST. REMAINING TIME:    4 sec.!		[Relax Library][TOT=   81][ 85 %][EST. REMAINING TIME:    3 sec.!		[Relax Library][TOT=   81][ 86 %][EST. REMAINING TIME:    3 sec.!		[Relax Library][TOT=   81][ 87 %][EST. REMAINING TIME:    3 sec.!		[Relax Library][TOT=   81][ 88 %][EST. REMAINING TIME:    3 sec.!		[Relax Library][TOT=   81][ 90 %][EST. REMAINING TIME:    2 sec.!		[Relax Library][TOT=   81][ 91 %][EST. REMAINING TIME:    2 sec.!		[Relax Library][TOT=   81][ 92 %][EST. REMAINING TIME:    2 sec.!		[Relax Library][TOT=   81][ 93 %][EST. REMAINING TIME:    1 sec.!		[Relax Library][TOT=   81][ 95 %][EST. REMAINING TIME:    1 sec.!		[Relax Library][TOT=   81][ 96 %][EST. REMAINING TIME:    1 sec.!		[Relax Library][TOT=   81][100 %][ ELAPSED  TIME:   25 sec.]

Relaxation Summary: [12714362]--->[6434833]



UN-WEIGHTED MODE: EVERY SEQUENCE WEIGHTS 1

MAKE GUIDE TREE 
	[MODE=nj][DONE]

PROGRESSIVE_ALIGNMENT [Tree Based]
Group    1: Acromyrmex
Group    2: Acromyrmex_1
Group    3: Amphibalanus
Group    4: Ampulex
Group    5: Ampulex_1
Group    6: Ampulex_2
Group    7: Apis
Group    8: Apolygus
Group    9: Arctia
Group   10: Arctia_1
Group   11: Atta
Group   12: Brenthis
Group   13: Ceratitis
Group   14: Cloeon
Group   15: Cloeon_1
Group   16: Cotesia
Group   17: Cotesia_1
Group   18: Dendroctonus
Group   19: Dendroctonus_1
Group   20: Dendrolimus
Group   21: Diabrotica
Group   22: Diaphorina
Group   23: Diaphorina_1
Group   24: Diaphorina_2
Group   25: Diaphorina_3
Group   26: Diaphorina_4
Group   27: Eciton
Group   28: Eciton_1
Group   29: Ephemera
Group   30: Frieseomelitta
Group   31: Glossina
Group   32: Harpegnathos
Group   33: Helicoverpa
Group   34: Holotrichia
Group   35: Iphiclides
Group   36: Iphiclides_1
Group   37: Iphiclides_2
Group   38: Lamprigera
Group   39: Lamprigera_1
Group   40: Lucilia
Group   41: Megalurothrips
Group   42: Mischocyttarus
Group   43: NHA1_prot_size=637_strand=+
Group   44: NHA2_prot_size=656_strand=+
Group   45: NHA3_prot_size=1204_strand=+
Group   46: NHA4_prot_size=786_strand=+
Group   47: NHA5_prot_size=754_strand=+
Group   48: NHA6_prot_size=708_strand=+
Group   49: NHA7_prot_size=589_strand=-
Group   50: NHA8_prot_size=329_strand=+
Group   51: Nezara
Group   52: Nymphon
Group   53: Nymphon_1
Group   54: Nymphon_2
Group   55: Nymphon_3
Group   56: Nymphon_4
Group   57: Nymphon_5
Group   58: Nymphon_6
Group   59: Oedothorax
Group   60: Ooceraea
Group   61: Ooceraea_1
Group   62: Ooceraea_2
Group   63: Penaeus
Group   64: Polistes
Group   65: Polypedilum
Group   66: Polypedilum_1
Group   67: Polypedilum_2
Group   68: Spodoptera
Group   69: Spodoptera_1
Group   70: Spodoptera_2
Group   71: Temnothorax
Group   72: Temnothorax_1
Group   73: Tenebrio
Group   74: Tigriopus
Group   75: Trachymyrmex
Group   76: Trachymyrmex_1
Group   77: Vespula
Group   78: Vespula_1
Group   79: Vespula_2
Group   80: Vespula_3
Group   81: Zophobas

Single Thread
	Group   82: [Group   62 (   1 seq)] with [Group   28 (   1 seq)]-->[Len=  621][PGroup   83: [Group   72 (   1 seq)] with [Group   82 (   2 seq)]-->[Len=  622][PGroup   84: [Group   83 (   3 seq)] with [Group    6 (   1 seq)]-->[Len=  622][PGroup   85: [Group   84 (   4 seq)] with [Group    2 (   1 seq)]-->[Len=  622][PGroup   86: [Group   80 (   1 seq)] with [Group   85 (   5 seq)]-->[Len=  671][PGroup   87: [Group   17 (   1 seq)] with [Group   16 (   1 seq)]-->[Len=  618][PGroup   88: [Group   87 (   2 seq)] with [Group   86 (   6 seq)]-->[Len=  678][PGroup   89: [Group   39 (   1 seq)] with [Group   88 (   8 seq)]-->[Len=  695][PGroup   90: [Group   10 (   1 seq)] with [Group    9 (   1 seq)]-->[Len=  770][PGroup   91: [Group   70 (   1 seq)] with [Group   69 (   1 seq)]-->[Len=  773][PGroup   92: [Group   91 (   2 seq)] with [Group   68 (   1 seq)]-->[Len=  807][PGroup   93: [Group   92 (   3 seq)] with [Group   33 (   1 seq)]-->[Len=  813][PGroup   94: [Group   93 (   4 seq)] with [Group   90 (   2 seq)]-->[Len=  828][PGroup   95: [Group   37 (   1 seq)] with [Group   36 (   1 seq)]-->[Len=  706][PGroup   96: [Group   95 (   2 seq)] with [Group   35 (   1 seq)]-->[Len=  806][PGroup   97: [Group   96 (   3 seq)] with [Group   12 (   1 seq)]-->[Len=  821][PGroup   98: [Group   20 (   1 seq)] with [Group   97 (   4 seq)]-->[Len=  842][PGroup   99: [Group   98 (   5 seq)] with [Group   94 (   6 seq)]-->[Len=  895][PGroup  100: [Group   99 (  11 seq)] with [Group   89 (   9 seq)]-->[Len=  944][PGroup  101: [Group   15 (   1 seq)] with [Group  100 (  20 seq)]-->[Len=  945][PGroup  102: [Group   50 (   1 seq)] with [Group    3 (   1 seq)]-->[Len=  593][PGroup  103: [Group   63 (   1 seq)] with [Group  102 (   2 seq)]-->[Len=  594][PGroup  104: [Group   54 (   1 seq)] with [Group   52 (   1 seq)]-->[Len=  556][PGroup  105: [Group   56 (   1 seq)] with [Group   55 (   1 seq)]-->[Len= 1007][PGroup  106: [Group  105 (   2 seq)] with [Group   53 (   1 seq)]-->[Len= 1007][PGroup  107: [Group  106 (   3 seq)] with [Group  104 (   2 seq)]-->[Len= 1007][PGroup  108: [Group   58 (   1 seq)] with [Group   57 (   1 seq)]-->[Len= 1008][PGroup  109: [Group  108 (   2 seq)] with [Group  107 (   5 seq)]-->[Len= 1015][PGroup  110: [Group  109 (   7 seq)] with [Group  103 (   3 seq)]-->[Len= 1057][PGroup  111: [Group   74 (   1 seq)] with [Group  110 (  10 seq)]-->[Len= 1068][PGroup  112: [Group   44 (   1 seq)] with [Group   43 (   1 seq)]-->[Len=  721][PGroup  113: [Group   49 (   1 seq)] with [Group   47 (   1 seq)]-->[Len=  758][PGroup  114: [Group   48 (   1 seq)] with [Group  113 (   2 seq)]-->[Len=  759][PGroup  115: [Group  114 (   3 seq)] with [Group   45 (   1 seq)]-->[Len= 1299][PGroup  116: [Group   46 (   1 seq)] with [Group  115 (   4 seq)]-->[Len= 1382][PGroup  117: [Group  116 (   5 seq)] with [Group  112 (   2 seq)]-->[Len= 1414][PGroup  118: [Group  117 (   7 seq)] with [Group  111 (  11 seq)]-->[Len= 1888][PGroup  119: [Group   51 (   1 seq)] with [Group    8 (   1 seq)]-->[Len=  769][PGroup  120: [Group   23 (   1 seq)] with [Group   22 (   1 seq)]-->[Len=  552][PGroup  121: [Group   24 (   1 seq)] with [Group  120 (   2 seq)]-->[Len=  556][PGroup  122: [Group  121 (   3 seq)] with [Group  119 (   2 seq)]-->[Len=  797][PGroup  123: [Group   26 (   1 seq)] with [Group   25 (   1 seq)]-->[Len=  529][PGroup  124: [Group  123 (   2 seq)] with [Group  122 (   5 seq)]-->[Len=  804][PGroup  125: [Group   29 (   1 seq)] with [Group   14 (   1 seq)]-->[Len=  504][PGroup  126: [Group   41 (   1 seq)] with [Group  125 (   2 seq)]-->[Len=  556][PGroup  127: [Group  126 (   3 seq)] with [Group  124 (   7 seq)]-->[Len=  824][PGroup  128: [Group  127 (  10 seq)] with [Group  118 (  18 seq)]-->[Len= 2013][PGroup  129: [Group  128 (  28 seq)] with [Group  101 (  21 seq)]-->[Len= 2214][PGroup  130: [Group  129 (  49 seq)] with [Group   59 (   1 seq)]-->[Len= 2227][PGroup  131: [Group   40 (   1 seq)] with [Group   31 (   1 seq)]-->[Len=  820][PGroup  132: [Group  131 (   2 seq)] with [Group   13 (   1 seq)]-->[Len=  866][PGroup  133: [Group   66 (   1 seq)] with [Group   65 (   1 seq)]-->[Len=  524][PGroup  134: [Group  133 (   2 seq)] with [Group  132 (   3 seq)]-->[Len=  887][PGroup  135: [Group  134 (   5 seq)] with [Group  130 (  50 seq)]-->[Len= 2378][PGroup  136: [Group   75 (   1 seq)] with [Group    1 (   1 seq)]-->[Len=  729][PGroup  137: [Group   11 (   1 seq)] with [Group  136 (   2 seq)]-->[Len=  752][PGroup  138: [Group   76 (   1 seq)] with [Group  137 (   3 seq)]-->[Len=  752][PGroup  139: [Group   61 (   1 seq)] with [Group   60 (   1 seq)]-->[Len=  723][PGroup  140: [Group  139 (   2 seq)] with [Group   27 (   1 seq)]-->[Len=  727][PGroup  141: [Group  140 (   3 seq)] with [Group  138 (   4 seq)]-->[Len=  754][PGroup  142: [Group   71 (   1 seq)] with [Group  141 (   7 seq)]-->[Len= 1101][PGroup  143: [Group    5 (   1 seq)] with [Group    4 (   1 seq)]-->[Len=  737][PGroup  144: [Group   30 (   1 seq)] with [Group    7 (   1 seq)]-->[Len=  758][PGroup  145: [Group  144 (   2 seq)] with [Group  143 (   2 seq)]-->[Len=  764][PGroup  146: [Group  145 (   4 seq)] with [Group  142 (   8 seq)]-->[Len= 1121][PGroup  147: [Group   32 (   1 seq)] with [Group  146 (  12 seq)]-->[Len= 1127][PGroup  148: [Group   64 (   1 seq)] with [Group   42 (   1 seq)]-->[Len=  781][PGroup  149: [Group   79 (   1 seq)] with [Group   78 (   1 seq)]-->[Len=  745][PGroup  150: [Group  149 (   2 seq)] with [Group   77 (   1 seq)]-->[Len=  745][PGroup  151: [Group  150 (   3 seq)] with [Group  148 (   2 seq)]-->[Len=  787][PGroup  152: [Group  151 (   5 seq)] with [Group  147 (  13 seq)]-->[Len= 1160][PGroup  153: [Group   19 (   1 seq)] with [Group   18 (   1 seq)]-->[Len=  832][PGroup  154: [Group   81 (   1 seq)] with [Group   73 (   1 seq)]-->[Len=  688][PGroup  155: [Group  154 (   2 seq)] with [Group   34 (   1 seq)]-->[Len=  708][PGroup  156: [Group  155 (   3 seq)] with [Group   21 (   1 seq)]-->[Len=  718][PGroup  157: [Group  156 (   4 seq)] with [Group  153 (   2 seq)]-->[Len=  897][PGroup  158: [Group   38 (   1 seq)] with [Group  157 (   6 seq)]-->[Len=  909][PGroup  159: [Group  158 (   7 seq)] with [Group  152 (  18 seq)]-->[Len= 1375][PGroup  160: [Group   67 (   1 seq)] with [Group  159 (  25 seq)]-->[Len= 1786][PGroup  161: [Group  160 (  26 seq)] with [Group  135 (  55 seq)]-->[Len= 3397][PID:84738]


!		[Final Evaluation][TOT= 1698][100 %][ ELAPSED  TIME:    1 sec.]



OUTPUT RESULTS
	#### File Type= GUIDE_TREE      Format= newick          Name= 2023-03-12-protein_sequence_orthologs.dnd
	#### File Type= MSA             Format= aln             Name= 2023-03-12-protein_sequence_orthologs.aln
	#### File Type= MSA             Format= html            Name= 2023-03-12-protein_sequence_orthologs.html

 Command Line: t_coffee 2023-03-12-protein_sequence_orthologs.fasta  [PROGRAM:T-COFFEE]
 T-COFFEE Memory Usage: Current= 61.113 Mb, Max= 283.711 Mb
 Results Produced with T-COFFEE Version_13.45.0.4846264 (2020-10-15 17:52:11 - Revision 5becd5d - Build 620)
 T-COFFEE is available from http://www.tcoffee.org
 Register on: https://groups.google.com/group/tcoffee/


*************************************************************************************************
                        MESSAGES RECAPITULATION                                    
84738 -- WARNING: Sequence Nymphon is duplicated in file 2023-03-12-protein_sequence_orthologs.fasta. The sequence will be renamed
*************************************************************************************************

## Prelim tree: http://iqtree.cibiv.univie.ac.at/
parameters 
alignment file: 2023-03-12-protein_orthologs.aln
use example alignment: no
sequence type: protein
partition file: - 

substitution model: auto
FreeRate heterogeneity: -
Ascertainment bias correction: -

Bootstrap analysis: Ultrafast
Create .ufboot file: -
Max iterations: 1000
Min corr coefficient: 0.99
Number of boostrap alignments: 1000
SH-aLRT branch test: yes, replicates = 1000
Approximate Bayes test: yes

Pertubation strenght: 0.5
IQ-TREE stopping value

Result:
IQ-TREE 1.6.12 built Aug 15 2019

Input file name: 2023-03-12-protein_sequence_orthologs.aln
Type of analysis: ModelFinder + tree reconstruction + ultrafast bootstrap (1000 replicates)
Random seed number: 628317

REFERENCES
----------

To cite ModelFinder please use: 

Subha Kalyaanamoorthy, Bui Quang Minh, Thomas KF Wong, Arndt von Haeseler,
and Lars S Jermiin (2017) ModelFinder: Fast model selection for
accurate phylogenetic estimates. Nature Methods, 14:587–589.
https://doi.org/10.1038/nmeth.4285

To cite IQ-TREE please use:

Lam-Tung Nguyen, Heiko A. Schmidt, Arndt von Haeseler, and Bui Quang Minh
(2015) IQ-TREE: A fast and effective stochastic algorithm for estimating
maximum likelihood phylogenies. Mol Biol Evol, 32:268-274.
https://doi.org/10.1093/molbev/msu300

Since you used ultrafast bootstrap (UFBoot) please also cite: 

Diep Thi Hoang, Olga Chernomor, Arndt von Haeseler, Bui Quang Minh,
and Le Sy Vinh (2017) UFBoot2: Improving the ultrafast bootstrap
approximation. Mol Biol Evol, in press.
https://doi.org/10.1093/molbev/msx281

SEQUENCE ALIGNMENT
------------------

Input data: 81 sequences with 3397 amino-acid sites
Number of constant sites: 1588 (= 46.7471% of all sites)
Number of invariant (constant or ambiguous constant) sites: 1588 (= 46.7471% of all sites)
Number of parsimony informative sites: 1075
Number of distinct site patterns: 2149

ModelFinder
-----------

Best-fit model according to BIC: VT+G4

List of models sorted by BIC scores: 

Model             LogL          AIC      w-AIC      AICc     w-AICc       BIC      w-BIC
VT+G4           -52957.7084 106235.4169 + 0.7288 106251.3377 + 0.7485 107216.3205 + 0.9829
VT+I+G4         -52957.6969 106237.3938 + 0.2712 106253.5187 + 0.2515 107224.4282 - 0.0171
LG+G4           -52974.7550 106269.5100 - 0.0000 106285.4309 - 0.0000 107250.4137 - 0.0000
LG+I+G4         -52974.7663 106271.5327 - 0.0000 106287.6576 - 0.0000 107258.5670 - 0.0000
VT+F+G4         -53002.0763 106362.1526 - 0.0000 106382.1837 - 0.0000 107459.5386 - 0.0000
WAG+F+G4        -53003.6175 106365.2350 - 0.0000 106385.2661 - 0.0000 107462.6210 - 0.0000
VT+F+I+G4       -53002.0254 106364.0509 - 0.0000 106384.3121 - 0.0000 107467.5675 - 0.0000
WAG+F+I+G4      -53003.6680 106367.3361 - 0.0000 106387.5973 - 0.0000 107470.8527 - 0.0000
LG+F+G4         -53017.4297 106392.8594 - 0.0000 106412.8905 - 0.0000 107490.2454 - 0.0000
WAG+G4          -53094.8199 106509.6398 - 0.0000 106525.5607 - 0.0000 107490.5435 - 0.0000
LG+F+I+G4       -53017.4108 106394.8217 - 0.0000 106415.0829 - 0.0000 107498.3383 - 0.0000
WAG+I+G4        -53094.8319 106511.6637 - 0.0000 106527.7886 - 0.0000 107498.6981 - 0.0000
JTT+G4          -53140.6497 106601.2994 - 0.0000 106617.2203 - 0.0000 107582.2031 - 0.0000
JTT+I+G4        -53140.6043 106603.2085 - 0.0000 106619.3334 - 0.0000 107590.2429 - 0.0000
JTTDCMut+G4     -53148.1941 106616.3881 - 0.0000 106632.3090 - 0.0000 107597.2918 - 0.0000
JTTDCMut+I+G4   -53148.1970 106618.3939 - 0.0000 106634.5188 - 0.0000 107605.4283 - 0.0000
Blosum62+G4     -53192.2375 106704.4750 - 0.0000 106720.3959 - 0.0000 107685.3787 - 0.0000
Blosum62+I+G4   -53192.2405 106706.4811 - 0.0000 106722.6060 - 0.0000 107693.5154 - 0.0000
cpREV+F+G4      -53123.8644 106605.7288 - 0.0000 106625.7599 - 0.0000 107703.1148 - 0.0000
cpREV+F+I+G4    -53123.8909 106607.7818 - 0.0000 106628.0430 - 0.0000 107711.2985 - 0.0000
PMB+G4          -53219.9822 106759.9644 - 0.0000 106775.8853 - 0.0000 107740.8681 - 0.0000
JTTDCMut+F+G4   -53146.2276 106650.4552 - 0.0000 106670.4862 - 0.0000 107747.8411 - 0.0000
PMB+I+G4        -53219.9784 106761.9567 - 0.0000 106778.0816 - 0.0000 107748.9910 - 0.0000
JTT+F+G4        -53147.2541 106652.5083 - 0.0000 106672.5393 - 0.0000 107749.8942 - 0.0000
JTTDCMut+F+I+G4 -53146.2123 106652.4246 - 0.0000 106672.6858 - 0.0000 107755.9412 - 0.0000
JTT+F+I+G4      -53147.1948 106654.3896 - 0.0000 106674.6508 - 0.0000 107757.9062 - 0.0000
rtREV+F+G4      -53172.1370 106702.2739 - 0.0000 106722.3050 - 0.0000 107799.6599 - 0.0000
Blosum62+F+G4   -53176.1164 106710.2327 - 0.0000 106730.2638 - 0.0000 107807.6187 - 0.0000
rtREV+F+I+G4    -53172.1246 106704.2492 - 0.0000 106724.5104 - 0.0000 107807.7658 - 0.0000
cpREV+G4        -53255.4423 106830.8846 - 0.0000 106846.8055 - 0.0000 107811.7883 - 0.0000
Blosum62+F+I+G4 -53176.0727 106712.1454 - 0.0000 106732.4066 - 0.0000 107815.6621 - 0.0000
cpREV+I+G4      -53255.4865 106832.9730 - 0.0000 106849.0979 - 0.0000 107820.0073 - 0.0000
PMB+F+G4        -53214.3257 106786.6513 - 0.0000 106806.6824 - 0.0000 107884.0373 - 0.0000
PMB+F+I+G4      -53214.2956 106788.5912 - 0.0000 106808.8524 - 0.0000 107892.1078 - 0.0000
mtInv+F+G4      -53231.1858 106820.3715 - 0.0000 106840.4026 - 0.0000 107917.7575 - 0.0000
mtInv+F+I+G4    -53231.1899 106822.3797 - 0.0000 106842.6409 - 0.0000 107925.8964 - 0.0000
rtREV+G4        -53444.8712 107209.7424 - 0.0000 107225.6633 - 0.0000 108190.6461 - 0.0000
rtREV+I+G4      -53444.8691 107211.7381 - 0.0000 107227.8630 - 0.0000 108198.7724 - 0.0000
DCMut+F+G4      -53391.9979 107141.9958 - 0.0000 107162.0268 - 0.0000 108239.3817 - 0.0000
Dayhoff+F+G4    -53392.4293 107142.8586 - 0.0000 107162.8897 - 0.0000 108240.2446 - 0.0000
DCMut+F+I+G4    -53391.9825 107143.9649 - 0.0000 107164.2261 - 0.0000 108247.4815 - 0.0000
Dayhoff+F+I+G4  -53392.5228 107145.0456 - 0.0000 107165.3068 - 0.0000 108248.5623 - 0.0000
mtMet+F+G4      -53506.6351 107371.2703 - 0.0000 107391.3014 - 0.0000 108468.6563 - 0.0000
mtMet+F+I+G4    -53506.6187 107373.2373 - 0.0000 107393.4985 - 0.0000 108476.7540 - 0.0000
mtZOA+F+G4      -53542.1360 107442.2719 - 0.0000 107462.3030 - 0.0000 108539.6579 - 0.0000
mtZOA+F+I+G4    -53542.1491 107444.2982 - 0.0000 107464.5594 - 0.0000 108547.8149 - 0.0000
DCMut+G4        -53695.4728 107710.9456 - 0.0000 107726.8665 - 0.0000 108691.8493 - 0.0000
mtREV+F+G4      -53618.3518 107594.7036 - 0.0000 107614.7347 - 0.0000 108692.0896 - 0.0000
Dayhoff+G4      -53695.9939 107711.9878 - 0.0000 107727.9087 - 0.0000 108692.8915 - 0.0000
DCMut+I+G4      -53695.4628 107712.9256 - 0.0000 107729.0505 - 0.0000 108699.9599 - 0.0000
mtREV+F+I+G4    -53618.3298 107596.6597 - 0.0000 107616.9209 - 0.0000 108700.1763 - 0.0000
Dayhoff+I+G4    -53695.7997 107713.5995 - 0.0000 107729.7244 - 0.0000 108700.6338 - 0.0000
FLU+G4          -53866.8279 108053.6558 - 0.0000 108069.5767 - 0.0000 109034.5595 - 0.0000
FLU+I+G4        -53866.7817 108055.5633 - 0.0000 108071.6882 - 0.0000 109042.5976 - 0.0000
FLU+F+G4        -53804.0111 107966.0222 - 0.0000 107986.0533 - 0.0000 109063.4082 - 0.0000
FLU+F+I+G4      -53803.9654 107967.9308 - 0.0000 107988.1920 - 0.0000 109071.4475 - 0.0000
HIVb+F+G4       -53952.6897 108263.3795 - 0.0000 108283.4105 - 0.0000 109360.7654 - 0.0000
HIVb+F+I+G4     -53952.6772 108265.3544 - 0.0000 108285.6156 - 0.0000 109368.8710 - 0.0000
mtART+F+G4      -53978.1747 108314.3495 - 0.0000 108334.3805 - 0.0000 109411.7354 - 0.0000
mtART+F+I+G4    -53978.1716 108316.3433 - 0.0000 108336.6045 - 0.0000 109419.8599 - 0.0000
mtVer+F+G4      -54041.6363 108441.2726 - 0.0000 108461.3037 - 0.0000 109538.6586 - 0.0000
mtVer+F+I+G4    -54041.6201 108443.2402 - 0.0000 108463.5014 - 0.0000 109546.7568 - 0.0000
HIVb+G4         -54163.8796 108647.7591 - 0.0000 108663.6800 - 0.0000 109628.6628 - 0.0000
HIVb+I+G4       -54163.8653 108649.7306 - 0.0000 108665.8555 - 0.0000 109636.7649 - 0.0000
mtMAM+F+G4      -54628.2107 109614.4214 - 0.0000 109634.4524 - 0.0000 110711.8073 - 0.0000
mtMAM+F+I+G4    -54628.2787 109616.5574 - 0.0000 109636.8186 - 0.0000 110720.0741 - 0.0000
mtZOA+G4        -54831.8000 109983.6000 - 0.0000 109999.5209 - 0.0000 110964.5037 - 0.0000
mtZOA+I+G4      -54831.7960 109985.5921 - 0.0000 110001.7170 - 0.0000 110972.6264 - 0.0000
VT+I            -54891.4270 110102.8540 - 0.0000 110118.7748 - 0.0000 111083.7576 - 0.0000
VT              -54963.8935 110245.7870 - 0.0000 110261.5052 - 0.0000 111220.5600 - 0.0000
HIVw+F+G4       -54954.0657 110266.1314 - 0.0000 110286.1625 - 0.0000 111363.5174 - 0.0000
HIVw+F+I+G4     -54954.0418 110268.0837 - 0.0000 110288.3449 - 0.0000 111371.6003 - 0.0000
VT+F+I          -54988.7197 110335.4393 - 0.0000 110355.4704 - 0.0000 111432.8253 - 0.0000
WAG+I           -55110.6581 110541.3162 - 0.0000 110557.2371 - 0.0000 111522.2199 - 0.0000
mtMet+G4        -55117.0216 110554.0431 - 0.0000 110569.9640 - 0.0000 111534.9468 - 0.0000
mtMet+I+G4      -55117.0087 110556.0173 - 0.0000 110572.1422 - 0.0000 111543.0517 - 0.0000
VT+F            -55054.7173 110465.4347 - 0.0000 110485.2370 - 0.0000 111556.6900 - 0.0000
PMB+I           -55132.8639 110585.7278 - 0.0000 110601.6487 - 0.0000 111566.6315 - 0.0000
Blosum62+I      -55136.1185 110592.2371 - 0.0000 110608.1580 - 0.0000 111573.1408 - 0.0000
WAG             -55175.7857 110669.5715 - 0.0000 110685.2897 - 0.0000 111644.3445 - 0.0000
WAG+F+I         -55098.3420 110554.6839 - 0.0000 110574.7150 - 0.0000 111652.0699 - 0.0000
PMB             -55190.1193 110698.2385 - 0.0000 110713.9568 - 0.0000 111673.0115 - 0.0000
Blosum62        -55193.2714 110704.5428 - 0.0000 110720.2611 - 0.0000 111679.3158 - 0.0000
WAG+F           -55154.1068 110664.2135 - 0.0000 110684.0159 - 0.0000 111755.4689 - 0.0000
Blosum62+F+I    -55174.3993 110706.7986 - 0.0000 110726.8296 - 0.0000 111804.1845 - 0.0000
PMB+F+I         -55206.0032 110770.0063 - 0.0000 110790.0374 - 0.0000 111867.3923 - 0.0000
Blosum62+F      -55231.4274 110818.8548 - 0.0000 110838.6571 - 0.0000 111910.1101 - 0.0000
PMB+F           -55261.6880 110879.3760 - 0.0000 110899.1783 - 0.0000 111970.6313 - 0.0000
cpREV+F+I       -55274.9224 110907.8447 - 0.0000 110927.8758 - 0.0000 112005.2307 - 0.0000
mtREV+G4        -55353.0057 111026.0115 - 0.0000 111041.9324 - 0.0000 112006.9152 - 0.0000
mtREV+I+G4      -55353.0048 111028.0096 - 0.0000 111044.1345 - 0.0000 112015.0440 - 0.0000
LG+I            -55360.0010 111040.0021 - 0.0000 111055.9230 - 0.0000 112020.9058 - 0.0000
cpREV+I         -55365.3913 111050.7825 - 0.0000 111066.7034 - 0.0000 112031.6862 - 0.0000
JTTDCMut+I      -55370.4434 111060.8868 - 0.0000 111076.8077 - 0.0000 112041.7905 - 0.0000
JTT+I           -55375.5809 111071.1617 - 0.0000 111087.0826 - 0.0000 112052.0654 - 0.0000
cpREV+F         -55324.8066 111005.6131 - 0.0000 111025.4155 - 0.0000 112096.8685 - 0.0000
cpREV           -55412.7203 111143.4406 - 0.0000 111159.1589 - 0.0000 112118.2136 - 0.0000
mtInv+G4        -55414.0909 111148.1819 - 0.0000 111164.1028 - 0.0000 112129.0856 - 0.0000
mtInv+I+G4      -55414.0756 111150.1512 - 0.0000 111166.2761 - 0.0000 112137.1856 - 0.0000
LG              -55422.7271 111163.4542 - 0.0000 111179.1724 - 0.0000 112138.2272 - 0.0000
JTTDCMut        -55462.8422 111243.6845 - 0.0000 111259.4027 - 0.0000 112218.4575 - 0.0000
JTT             -55470.6792 111259.3584 - 0.0000 111275.0767 - 0.0000 112234.1315 - 0.0000
JTTDCMut+F+I    -55460.5247 111279.0494 - 0.0000 111299.0804 - 0.0000 112376.4353 - 0.0000
JTT+F+I         -55470.0352 111298.0705 - 0.0000 111318.1016 - 0.0000 112395.4565 - 0.0000
LG+F+I          -55521.9237 111401.8474 - 0.0000 111421.8785 - 0.0000 112499.2334 - 0.0000
JTTDCMut+F      -55545.3640 111446.7279 - 0.0000 111466.5303 - 0.0000 112537.9833 - 0.0000
JTT+F           -55557.4777 111470.9554 - 0.0000 111490.7577 - 0.0000 112562.2107 - 0.0000
mtART+G4        -55641.5999 111603.1999 - 0.0000 111619.1208 - 0.0000 112584.1036 - 0.0000
HIVw+G4         -55644.2087 111608.4174 - 0.0000 111624.3383 - 0.0000 112589.3211 - 0.0000
mtART+I+G4      -55641.6171 111605.2342 - 0.0000 111621.3591 - 0.0000 112592.2685 - 0.0000
HIVw+I+G4       -55644.2014 111610.4029 - 0.0000 111626.5278 - 0.0000 112597.4372 - 0.0000
LG+F            -55580.4720 111516.9441 - 0.0000 111536.7465 - 0.0000 112608.1994 - 0.0000
rtREV+F+I       -55609.6575 111577.3150 - 0.0000 111597.3461 - 0.0000 112674.7010 - 0.0000
rtREV+I         -55717.7195 111755.4389 - 0.0000 111771.3598 - 0.0000 112736.3426 - 0.0000
rtREV+F         -55658.9538 111673.9077 - 0.0000 111693.7100 - 0.0000 112765.1630 - 0.0000
mtVer+G4        -55748.0891 111816.1782 - 0.0000 111832.0991 - 0.0000 112797.0819 - 0.0000
mtVer+I+G4      -55748.0821 111818.1642 - 0.0000 111834.2891 - 0.0000 112805.1985 - 0.0000
rtREV           -55767.3271 111852.6542 - 0.0000 111868.3725 - 0.0000 112827.4272 - 0.0000
DCMut+F+I       -55718.9291 111795.8582 - 0.0000 111815.8893 - 0.0000 112893.2442 - 0.0000
Dayhoff+F+I     -55724.0530 111806.1060 - 0.0000 111826.1371 - 0.0000 112903.4920 - 0.0000
DCMut+F         -55802.2720 111960.5440 - 0.0000 111980.3464 - 0.0000 113051.7993 - 0.0000
Dayhoff+F       -55807.4128 111970.8255 - 0.0000 111990.6279 - 0.0000 113062.0809 - 0.0000
DCMut+I         -55918.3260 112156.6521 - 0.0000 112172.5729 - 0.0000 113137.5557 - 0.0000
Dayhoff+I       -55923.9342 112167.8684 - 0.0000 112183.7893 - 0.0000 113148.7721 - 0.0000
DCMut           -56014.3226 112346.6452 - 0.0000 112362.3634 - 0.0000 113321.4182 - 0.0000
Dayhoff         -56019.9793 112357.9586 - 0.0000 112373.6768 - 0.0000 113332.7316 - 0.0000
mtInv+F+I       -55960.9059 112279.8118 - 0.0000 112299.8429 - 0.0000 113377.1978 - 0.0000
mtInv+F         -56033.4993 112422.9986 - 0.0000 112442.8010 - 0.0000 113514.2540 - 0.0000
mtMAM+G4        -56452.7158 113225.4316 - 0.0000 113241.3525 - 0.0000 114206.3353 - 0.0000
mtMAM+I+G4      -56452.7341 113227.4681 - 0.0000 113243.5930 - 0.0000 114214.5025 - 0.0000
mtREV+F+I       -56388.3108 113134.6217 - 0.0000 113154.6528 - 0.0000 114232.0077 - 0.0000
mtREV+F         -56428.5221 113213.0443 - 0.0000 113232.8466 - 0.0000 114304.2996 - 0.0000
mtMet+F+I       -56534.2121 113426.4242 - 0.0000 113446.4553 - 0.0000 114523.8102 - 0.0000
FLU+I           -56675.0736 113670.1472 - 0.0000 113686.0680 - 0.0000 114651.0508 - 0.0000
mtMet+F         -56607.0064 113570.0127 - 0.0000 113589.8151 - 0.0000 114661.2681 - 0.0000
FLU             -56763.3943 113844.7886 - 0.0000 113860.5069 - 0.0000 114819.5616 - 0.0000
FLU+F+I         -56731.1718 113820.3436 - 0.0000 113840.3747 - 0.0000 114917.7296 - 0.0000
HIVb+I          -56873.9081 114067.8163 - 0.0000 114083.7371 - 0.0000 115048.7199 - 0.0000
FLU+F           -56805.6853 113967.3705 - 0.0000 113987.1729 - 0.0000 115058.6259 - 0.0000
HIVb+F+I        -56811.2063 113980.4126 - 0.0000 114000.4437 - 0.0000 115077.7986 - 0.0000
mtZOA+F+I       -56841.2602 114040.5204 - 0.0000 114060.5515 - 0.0000 115137.9064 - 0.0000
mtZOA+F         -56902.1748 114160.3496 - 0.0000 114180.1520 - 0.0000 115251.6050 - 0.0000
HIVb            -56986.6983 114291.3966 - 0.0000 114307.1148 - 0.0000 115266.1696 - 0.0000
HIVb+F          -56917.9047 114191.8095 - 0.0000 114211.6118 - 0.0000 115283.0648 - 0.0000
mtVer+F+I       -57278.4551 114914.9102 - 0.0000 114934.9413 - 0.0000 116012.2962 - 0.0000
mtVer+F         -57355.4253 115066.8507 - 0.0000 115086.6530 - 0.0000 116158.1060 - 0.0000
mtART+F+I       -57749.8718 115857.7436 - 0.0000 115877.7747 - 0.0000 116955.1296 - 0.0000
mtART+F         -57797.0883 115950.1766 - 0.0000 115969.9789 - 0.0000 117041.4319 - 0.0000
HIVw+F+I        -57950.4724 116258.9448 - 0.0000 116278.9759 - 0.0000 117356.3308 - 0.0000
HIVw+F          -58093.5597 116543.1194 - 0.0000 116562.9217 - 0.0000 117634.3747 - 0.0000
mtInv+I         -58345.4052 117010.8104 - 0.0000 117026.7313 - 0.0000 117991.7141 - 0.0000
mtMet+I         -58383.4500 117086.8999 - 0.0000 117102.8208 - 0.0000 118067.8036 - 0.0000
mtREV+I         -58385.9784 117091.9568 - 0.0000 117107.8777 - 0.0000 118072.8605 - 0.0000
mtInv           -58407.1312 117132.2624 - 0.0000 117147.9807 - 0.0000 118107.0354 - 0.0000
mtREV           -58419.6364 117157.2727 - 0.0000 117172.9910 - 0.0000 118132.0458 - 0.0000
mtZOA+I         -58438.6755 117197.3509 - 0.0000 117213.2718 - 0.0000 118178.2546 - 0.0000
mtMet           -58443.1222 117204.2443 - 0.0000 117219.9626 - 0.0000 118179.0173 - 0.0000
mtZOA           -58493.6751 117305.3501 - 0.0000 117321.0684 - 0.0000 118280.1231 - 0.0000
mtMAM+F+I       -58424.2995 117206.5990 - 0.0000 117226.6301 - 0.0000 118303.9850 - 0.0000
mtMAM+F         -58472.9149 117301.8298 - 0.0000 117321.6321 - 0.0000 118393.0851 - 0.0000
HIVw+I          -58611.7887 117543.5774 - 0.0000 117559.4983 - 0.0000 118524.4811 - 0.0000
HIVw            -58759.6775 117837.3550 - 0.0000 117853.0733 - 0.0000 118812.1280 - 0.0000
mtVer+I         -59379.4474 119078.8948 - 0.0000 119094.8156 - 0.0000 120059.7984 - 0.0000
mtVer           -59439.6628 119197.3256 - 0.0000 119213.0439 - 0.0000 120172.0986 - 0.0000
mtART+I         -59785.4640 119890.9279 - 0.0000 119906.8488 - 0.0000 120871.8316 - 0.0000
mtART           -59830.8271 119979.6543 - 0.0000 119995.3726 - 0.0000 120954.4273 - 0.0000
mtMAM+I         -60768.1455 121856.2911 - 0.0000 121872.2119 - 0.0000 122837.1947 - 0.0000
mtMAM           -60811.4060 121940.8119 - 0.0000 121956.5302 - 0.0000 122915.5850 - 0.0000

AIC, w-AIC   : Akaike information criterion scores and weights.
AICc, w-AICc : Corrected AIC scores and weights.
BIC, w-BIC   : Bayesian information criterion scores and weights.

Plus signs denote the 95% confidence sets.
Minus signs denote significant exclusion.

SUBSTITUTION PROCESS
--------------------

Model of substitution: VT+G4

State frequencies: (model)

Model of rate heterogeneity: Gamma with 4 categories
Gamma shape alpha: 0.7120

 Category  Relative_rate  Proportion
  1         0.0767         0.2500
  2         0.3691         0.2500
  3         0.9292         0.2500
  4         2.6249         0.2500
Relative rates are computed as MEAN of the portion of the Gamma distribution falling in the category.

MAXIMUM LIKELIHOOD TREE
-----------------------

Log-likelihood of the tree: -52896.4147 (s.e. 1252.3366)
Unconstrained log-likelihood (without tree): -24030.5354
Number of free parameters (#branches + #model parameters): 160
Akaike information criterion (AIC) score: 106112.8294
Corrected Akaike information criterion (AICc) score: 106128.7503
Bayesian information criterion (BIC) score: 107093.7331

Total tree length (sum of branch lengths): 61.0261
Sum of internal branch lengths: 33.8587 (55.4823% of tree length)

WARNING: 2 near-zero internal branches (<0.0003) should be treated with caution
         Such branches are denoted by '**' in the figure below

NOTE: Tree is UNROOTED although outgroup taxon 'Nymphon' is drawn at root
Numbers in parentheses are SH-aLRT support (%) / aBayes support / ultrafast bootstrap support (%)

+**Nymphon
|
|     +**Nymphon_1
|  +**| (0/0.333/93)
|  |  +**Nymphon_3
+--| (97.9/1/98)
|  |         +--------Oedothorax
|  |     +---| (99.9/1/100)
|  |     |   |  +---Penaeus
|  |     |   +--| (30.8/0.799/80)
|  |     |      |        +---Tigriopus
|  |     |      |     +--| (97.3/1/99)
|  |     |      |     |  +--NHA8_prot_size_329_strand__
|  |     |      |  +--| (92.5/0.998/96)
|  |     |      |  |  |                        +--Diaphorina
|  |     |      |  |  |                     +--| (38.8/0.552/46)
|  |     |      |  |  |                     |  +**Diaphorina_1
|  |     |      |  |  |                 +---| (100/1/100)
|  |     |      |  |  |                 |   +--Diaphorina_2
|  |     |      |  |  |              +--| (52.8/0.927/84)
|  |     |      |  |  |              |  |  +--Nezara
|  |     |      |  |  |              |  +--| (99.7/1/100)
|  |     |      |  |  |              |     +--Apolygus
|  |     |      |  |  |           +--| (98.3/1/100)
|  |     |      |  |  |           |  |    +**Diaphorina_3
|  |     |      |  |  |           |  +----| (100/1/100)
|  |     |      |  |  |           |       +--Diaphorina_4
|  |     |      |  |  |        +--| (74.6/0.969/90)
|  |     |      |  |  |        |  +------Megalurothrips
|  |     |      |  |  |     +--| (95.5/1/100)
|  |     |      |  |  |     |  |  +--Ephemera
|  |     |      |  |  |     |  +--| (99.9/1/100)
|  |     |      |  |  |     |     +--Cloeon
|  |     |      |  |  |  +--| (98.7/1/100)
|  |     |      |  |  |  |  |                                                      +--Holotrichia
|  |     |      |  |  |  |  |                                                   +--| (97.2/1/95)
|  |     |      |  |  |  |  |                                                   |  |     +--Tenebrio
|  |     |      |  |  |  |  |                                                   |  |  +--| (96.6/1/100)
|  |     |      |  |  |  |  |                                                   |  |  |  +--Zophobas
|  |     |      |  |  |  |  |                                                   |  +--| (90.4/0.999/95)
|  |     |      |  |  |  |  |                                                   |     |  +--Diabrotica
|  |     |      |  |  |  |  |                                                   |     +--| (75.1/0.824/95)
|  |     |      |  |  |  |  |                                                   |        |  +--Dendroctonus
|  |     |      |  |  |  |  |                                                   |        +--| (100/1/100)
|  |     |      |  |  |  |  |                                                   |           +**Dendroctonus_1
|  |     |      |  |  |  |  |                                                +--| (88/0.991/95)
|  |     |      |  |  |  |  |                                                |  +--Lamprigera
|  |     |      |  |  |  |  |                                         +------| (99.3/1/99)
|  |     |      |  |  |  |  |                                         |      |        +--Vespula
|  |     |      |  |  |  |  |                                         |      |     +--| (99.6/1/100)
|  |     |      |  |  |  |  |                                         |      |     |  |  +--Vespula_1
|  |     |      |  |  |  |  |                                         |      |     |  +--| (68.2/0.589/100)
|  |     |      |  |  |  |  |                                         |      |     |     +--Vespula_2
|  |     |      |  |  |  |  |                                         |      |  +--| (99.7/1/92)
|  |     |      |  |  |  |  |                                         |      |  |  |  +--Polistes
|  |     |      |  |  |  |  |                                         |      |  |  +--| (99.5/1/94)
|  |     |      |  |  |  |  |                                         |      |  |     +--Mischocyttarus
|  |     |      |  |  |  |  |                                         |      +--| (91.2/0.995/90)
|  |     |      |  |  |  |  |                                         |         |           +--Eciton
|  |     |      |  |  |  |  |                                         |         |        +--| (83.9/0.97/96)
|  |     |      |  |  |  |  |                                         |         |        |  |  +--Ooceraea
|  |     |      |  |  |  |  |                                         |         |        |  +--| (94.7/1/98)
|  |     |      |  |  |  |  |                                         |         |        |     +--Ooceraea_1
|  |     |      |  |  |  |  |                                         |         |     +--| (99.9/1/100)
|  |     |      |  |  |  |  |                                         |         |     |  |     +--Temnothorax
|  |     |      |  |  |  |  |                                         |         |     |  |  +--| (98.9/1/100)
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |        +--Atta
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |     +--| (38/0.623/91)
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |     |  +--Acromyrmex
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |  +--| (93.9/1/96)
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |  |  +--Trachymyrmex
|  |     |      |  |  |  |  |                                         |         |     |  |  |  +--| (91.6/0.994/99)
|  |     |      |  |  |  |  |                                         |         |     |  |  |     +--Trachymyrmex_1
|  |     |      |  |  |  |  |                                         |         |     |  +--| (33.9/0.947/76)
|  |     |      |  |  |  |  |                                         |         |     |     +--Harpegnathos
|  |     |      |  |  |  |  |                                         |         |  +--| (40.7/0.802/73)
|  |     |      |  |  |  |  |                                         |         |  |  |  +--Frieseomelitta
|  |     |      |  |  |  |  |                                         |         |  |  +--| (100/1/100)
|  |     |      |  |  |  |  |                                         |         |  |     +--Apis
|  |     |      |  |  |  |  |                                         |         +--| (90.2/0.998/83)
|  |     |      |  |  |  |  |                                         |            |  +--Ampulex
|  |     |      |  |  |  |  |                                         |            +--| (100/1/100)
|  |     |      |  |  |  |  |                                         |               +--Ampulex_1
|  |     |      |  |  |  |  |           +-----------------------------| (100/1/100)
|  |     |      |  |  |  |  |           |                             +-----------Polypedilum_2
|  |     |      |  |  |  |  |        +--| (82.2/0.994/91)
|  |     |      |  |  |  |  |        |  |     +--Dendrolimus
|  |     |      |  |  |  |  |        |  |  +--| (82.3/0.985/87)
|  |     |      |  |  |  |  |        |  |  |  |        +--Spodoptera
|  |     |      |  |  |  |  |        |  |  |  |     +--| (93.4/1/100)
|  |     |      |  |  |  |  |        |  |  |  |     |  |  +**Spodoptera_1
|  |     |      |  |  |  |  |        |  |  |  |     |  +--| (95.5/1/100)
|  |     |      |  |  |  |  |        |  |  |  |     |     +--Spodoptera_2
|  |     |      |  |  |  |  |        |  |  |  |  +--| (93.2/1/99)
|  |     |      |  |  |  |  |        |  |  |  |  |  +--Helicoverpa
|  |     |      |  |  |  |  |        |  |  |  +--| (99.5/1/99)
|  |     |      |  |  |  |  |        |  |  |     |  +--Arctia
|  |     |      |  |  |  |  |        |  |  |     +--| (100/1/100)
|  |     |      |  |  |  |  |        |  |  |        +--Arctia_1
|  |     |      |  |  |  |  |        |  +--| (69.6/0.647/48)
|  |     |      |  |  |  |  |        |     |  +--Brenthis
|  |     |      |  |  |  |  |        |     +--| (52.2/0.916/50)
|  |     |      |  |  |  |  |        |        |     +--Iphiclides
|  |     |      |  |  |  |  |        |        |  +--| (98.3/1/89)
|  |     |      |  |  |  |  |        |        |  |  +--Iphiclides_1
|  |     |      |  |  |  |  |        |        +--| (99.8/1/97)
|  |     |      |  |  |  |  |        |           +--Iphiclides_2
|  |     |      |  |  |  |  |     +--| (69.4/0.955/87)
|  |     |      |  |  |  |  |     |  |  +--Lamprigera_1
|  |     |      |  |  |  |  |     |  +--| (99.8/1/99)
|  |     |      |  |  |  |  |     |     |              +--Temnothorax_1
|  |     |      |  |  |  |  |     |     |           +--| (78.9/0.999/97)
|  |     |      |  |  |  |  |     |     |           |  +--Acromyrmex_1
|  |     |      |  |  |  |  |     |     |        +--| (99.9/1/100)
|  |     |      |  |  |  |  |     |     |        |  |  +--Eciton_1
|  |     |      |  |  |  |  |     |     |        |  +--| (98.5/1/100)
|  |     |      |  |  |  |  |     |     |        |     +--Ooceraea_2
|  |     |      |  |  |  |  |     |     |     +--| (85/0.991/94)
|  |     |      |  |  |  |  |     |     |     |  +--Ampulex_2
|  |     |      |  |  |  |  |     |     |  +--| (94/1/95)
|  |     |      |  |  |  |  |     |     |  |  +--Vespula_3
|  |     |      |  |  |  |  |     |     +--| (100/1/99)
|  |     |      |  |  |  |  |     |        |  +--Cotesia
|  |     |      |  |  |  |  |     |        +--| (100/1/100)
|  |     |      |  |  |  |  |     |           +--Cotesia_1
|  |     |      |  |  |  |  |  +--| (100/1/100)
|  |     |      |  |  |  |  |  |  +---Cloeon_1
|  |     |      |  |  |  |  +--| (85.8/0.988/94)
|  |     |      |  |  |  |     |             +--Ceratitis
|  |     |      |  |  |  |     |          +--| (12.5/0.445/93)
|  |     |      |  |  |  |     |          |  +--Lucilia
|  |     |      |  |  |  |     |       +--| (99.3/1/100)
|  |     |      |  |  |  |     |       |  +--Glossina
|  |     |      |  |  |  |     +-------| (100/1/100)
|  |     |      |  |  |  |             |  +--Polypedilum
|  |     |      |  |  |  |             +--| (100/1/100)
|  |     |      |  |  |  |                +**Polypedilum_1
|  |     |      |  |  +--| (64.5/0.943/75)
|  |     |      |  |     |        +--NHA1_prot_size_637_strand__
|  |     |      |  |     |     +--| (78.9/0.904/73)
|  |     |      |  |     |     |  +--NHA2_prot_size_656_strand__
|  |     |      |  |     +-----| (100/1/100)
|  |     |      |  |           |     +--NHA3_prot_size_1204_strand__
|  |     |      |  |           |  +--| (28/0.877/63)
|  |     |      |  |           |  |  |     +--NHA5_prot_size_754_strand__
|  |     |      |  |           |  |  |  +--| (91.2/1/98)
|  |     |      |  |           |  |  |  |  +--NHA6_prot_size_708_strand__
|  |     |      |  |           |  |  +--| (100/1/100)
|  |     |      |  |           |  |     +--NHA7_prot_size_589_strand_-
|  |     |      |  |           +--| (100/1/100)
|  |     |      |  |              +--NHA4_prot_size_786_strand__
|  |     |      +--| (26.1/0.733/74)
|  |     |         +----Amphibalanus
|  |  +--| (93.5/0.997/98)
|  |  |  |  +--Nymphon_5
|  |  |  +--| (100/1/100)
|  |  |     +**Nymphon_6
|  +**| (0/0.334/88)
|     +--Nymphon_4
|
+--Nymphon_2

Tree in newick format:

(Nymphon:0.0000021483,((Nymphon_1:0.0000021462,Nymphon_3:0.0000021462)0/0.333/93:0.0000021483,(((Oedothorax:2.8370541434,(Penaeus:1.2713698524,(((Tigriopus:1.3035384111,NHA8_prot_size_329_strand__:0.7833631191)97.3/1/99:0.5382364304,((((((((Diaphorina:0.0075404242,Diaphorina_1:0.0000021462)38.8/0.552/46:0.0318135496,Diaphorina_2:0.0519400756)100/1/100:1.2010271060,(Nezara:0.6273662064,Apolygus:1.0379855705)99.7/1/100:0.5354950634)52.8/0.927/84:0.2491075723,(Diaphorina_3:0.0000024300,Diaphorina_4:0.0271183308)100/1/100:1.5628748930)98.3/1/100:0.4973384996,Megalurothrips:2.0933184420)74.6/0.969/90:0.2264202630,(Ephemera:0.9342712352,Cloeon:0.9419381855)99.9/1/100:0.7410525178)95.5/1/100:0.2684324946,((((((((Holotrichia:0.2359571642,((Tenebrio:0.1261012611,Zophobas:0.1891877633)96.6/1/100:0.0942879406,(Diabrotica:0.1940102473,(Dendroctonus:0.0546950172,Dendroctonus_1:0.0000028837)100/1/100:0.1998091393)75.1/0.824/95:0.0281656487)90.4/0.999/95:0.0569804858)97.2/1/95:0.0896832576,Lamprigera:0.2796403188)88/0.991/95:0.1597373272,(((Vespula:0.0057836007,(Vespula_1:0.0017012786,Vespula_2:0.0056280645)68.2/0.589/100:0.0024710436)99.6/1/100:0.0660130918,(Polistes:0.0220949015,Mischocyttarus:0.0371762012)99.5/1/94:0.0558315636)99.7/1/92:0.1390929434,((((Eciton:0.0688131466,(Ooceraea:0.0026782362,Ooceraea_1:0.0063546504)94.7/1/98:0.0482443515)83.9/0.97/96:0.0196687452,((Temnothorax:0.2251510887,(((Atta:0.0288972583,Acromyrmex:0.0206908062)38/0.623/91:0.0039849810,Trachymyrmex:0.0178234411)93.9/1/96:0.0198074408,Trachymyrmex_1:0.0235231774)91.6/0.994/99:0.0313940974)98.9/1/100:0.0726957189,Harpegnathos:0.1100330490)33.9/0.947/76:0.0458247114)99.9/1/100:0.1011530466,(Frieseomelitta:0.0526008365,Apis:0.1077271905)100/1/100:0.1608301914)40.7/0.802/73:0.0280770143,(Ampulex:0.0038160828,Ampulex_1:0.0075300661)100/1/100:0.1902602108)90.2/0.998/83:0.0422167899)91.2/0.995/90:0.1344027657)99.3/1/99:2.1805925720,Polypedilum_2:3.5648484475)100/1/100:8.7101843100,((Dendrolimus:0.2050519663,(((Spodoptera:0.0052949396,(Spodoptera_1:0.0000027237,Spodoptera_2:0.0684073733)95.5/1/100:0.0161697494)93.4/1/100:0.0351658159,Helicoverpa:0.1724214445)93.2/1/99:0.0716309341,(Arctia:0.0112964230,Arctia_1:0.0659442449)100/1/100:0.2314545212)99.5/1/99:0.1010099344)82.3/0.985/87:0.0706591950,(Brenthis:0.2127533449,((Iphiclides:0.0129929607,Iphiclides_1:0.0371073111)98.3/1/89:0.0562807423,Iphiclides_2:0.0118712712)99.8/1/97:0.1819630936)52.2/0.916/50:0.1022024700)69.6/0.647/48:0.1108231479)82.2/0.994/91:0.7906846049,(Lamprigera_1:0.8540387194,(((((Temnothorax_1:0.0312962944,Acromyrmex_1:0.2137410250)78.9/0.999/97:0.0309298722,(Eciton_1:0.0466543160,Ooceraea_2:0.0195247088)98.5/1/100:0.0603694965)99.9/1/100:0.1008975296,Ampulex_2:0.0738929093)85/0.991/94:0.0600958160,Vespula_3:0.3311383944)94/1/95:0.0933935819,(Cotesia:0.0203255141,Cotesia_1:0.0057584287)100/1/100:0.4871747859)100/1/99:0.4712365673)99.8/1/99:0.4330559831)69.4/0.955/87:0.2063552064,Cloeon_1:1.3953755050)100/1/100:1.0443178680,(((Ceratitis:0.6345646797,Lucilia:0.4880013039)12.5/0.445/93:0.0755157092,Glossina:0.7600929664)99.3/1/100:0.5719711406,(Polypedilum:0.0315462802,Polypedilum_1:0.0000027255)100/1/100:1.0549660320)100/1/100:2.3533370370)85.8/0.988/94:0.2583936439)98.7/1/100:0.4634672311,((NHA1_prot_size_637_strand__:0.3352242571,NHA2_prot_size_656_strand__:0.7975725099)78.9/0.904/73:0.1947732988,((NHA3_prot_size_1204_strand__:0.5395922044,((NHA5_prot_size_754_strand__:0.1906861751,NHA6_prot_size_708_strand__:0.1666493900)91.2/1/98:0.0947410651,NHA7_prot_size_589_strand_-:0.1451444363)100/1/100:0.6010927401)28/0.877/63:0.2136857553,NHA4_prot_size_786_strand__:0.4142764279)100/1/100:0.8547070884)100/1/100:1.7327316150)64.5/0.943/75:0.1566889279)92.5/0.998/96:0.2751258689,Amphibalanus:1.5015480949)26.1/0.733/74:0.1701527374)30.8/0.799/80:0.2499179207)99.9/1/100:1.1652986660,(Nymphon_5:0.0435267585,Nymphon_6:0.0000024391)100/1/100:0.0338349160)93.5/0.997/98:0.0097002234,Nymphon_4:0.0038532576)0/0.334/88:0.0000022950)97.9/1/98:0.0395085595,Nymphon_2:0.0109981170);

CONSENSUS TREE
--------------

Consensus tree is constructed from 1000bootstrap trees
Log-likelihood of consensus tree: -52896.567539
Robinson-Foulds distance between ML tree and consensus tree: 2

Branches with support >0.000000% are kept (extended consensus)
Branch lengths are optimized by maximum likelihood on original alignment
Numbers in parentheses are bootstrap supports (%)

+--Nymphon
|
|     +--Nymphon_1
|  +--| (93)
|  |  +--Nymphon_3
+--| (98)
|  |         +---------Oedothorax
|  |     +---| (100)
|  |     |   |  +---Penaeus
|  |     |   +--| (80)
|  |     |      |        +---Tigriopus
|  |     |      |     +--| (99)
|  |     |      |     |  +--NHA8_prot_size_329_strand__
|  |     |      |  +--| (96)
|  |     |      |  |  |                     +--Diaphorina
|  |     |      |  |  |                 +---| (100)
|  |     |      |  |  |                 |   |  +--Diaphorina_1
|  |     |      |  |  |                 |   +--| (54)
|  |     |      |  |  |                 |      +--Diaphorina_2
|  |     |      |  |  |              +--| (84)
|  |     |      |  |  |              |  |  +--Nezara
|  |     |      |  |  |              |  +--| (100)
|  |     |      |  |  |              |     +--Apolygus
|  |     |      |  |  |           +--| (100)
|  |     |      |  |  |           |  |    +--Diaphorina_3
|  |     |      |  |  |           |  +----| (100)
|  |     |      |  |  |           |       +--Diaphorina_4
|  |     |      |  |  |        +--| (90)
|  |     |      |  |  |        |  +------Megalurothrips
|  |     |      |  |  |     +--| (100)
|  |     |      |  |  |     |  |  +--Ephemera
|  |     |      |  |  |     |  +--| (100)
|  |     |      |  |  |     |     +--Cloeon
|  |     |      |  |  |  +--| (100)
|  |     |      |  |  |  |  |                                                      +--Holotrichia
|  |     |      |  |  |  |  |                                                   +--| (95)
|  |     |      |  |  |  |  |                                                   |  |     +--Tenebrio
|  |     |      |  |  |  |  |                                                   |  |  +--| (100)
|  |     |      |  |  |  |  |                                                   |  |  |  +--Zophobas
|  |     |      |  |  |  |  |                                                   |  +--| (95)
|  |     |      |  |  |  |  |                                                   |     |  +--Diabrotica
|  |     |      |  |  |  |  |                                                   |     +--| (95)
|  |     |      |  |  |  |  |                                                   |        |  +--Dendroctonus
|  |     |      |  |  |  |  |                                                   |        +--| (100)
|  |     |      |  |  |  |  |                                                   |           +--Dendroctonus_1
|  |     |      |  |  |  |  |                                                +--| (95)
|  |     |      |  |  |  |  |                                                |  +--Lamprigera
|  |     |      |  |  |  |  |                                         +------| (99)
|  |     |      |  |  |  |  |                                         |      |        +--Vespula
|  |     |      |  |  |  |  |                                         |      |     +--| (100)
|  |     |      |  |  |  |  |                                         |      |     |  |  +--Vespula_1
|  |     |      |  |  |  |  |                                         |      |     |  +--| (100)
|  |     |      |  |  |  |  |                                         |      |     |     +--Vespula_2
|  |     |      |  |  |  |  |                                         |      |  +--| (92)
|  |     |      |  |  |  |  |                                         |      |  |  |  +--Polistes
|  |     |      |  |  |  |  |                                         |      |  |  +--| (94)
|  |     |      |  |  |  |  |                                         |      |  |     +--Mischocyttarus
|  |     |      |  |  |  |  |                                         |      +--| (90)
|  |     |      |  |  |  |  |                                         |         |           +--Eciton
|  |     |      |  |  |  |  |                                         |         |        +--| (96)
|  |     |      |  |  |  |  |                                         |         |        |  |  +--Ooceraea
|  |     |      |  |  |  |  |                                         |         |        |  +--| (98)
|  |     |      |  |  |  |  |                                         |         |        |     +--Ooceraea_1
|  |     |      |  |  |  |  |                                         |         |     +--| (100)
|  |     |      |  |  |  |  |                                         |         |     |  |     +--Temnothorax
|  |     |      |  |  |  |  |                                         |         |     |  |  +--| (100)
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |        +--Atta
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |     +--| (91)
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |     |  +--Acromyrmex
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |  +--| (96)
|  |     |      |  |  |  |  |                                         |         |     |  |  |  |  |  +--Trachymyrmex
|  |     |      |  |  |  |  |                                         |         |     |  |  |  +--| (99)
|  |     |      |  |  |  |  |                                         |         |     |  |  |     +--Trachymyrmex_1
|  |     |      |  |  |  |  |                                         |         |     |  +--| (76)
|  |     |      |  |  |  |  |                                         |         |     |     +--Harpegnathos
|  |     |      |  |  |  |  |                                         |         |  +--| (73)
|  |     |      |  |  |  |  |                                         |         |  |  |  +--Frieseomelitta
|  |     |      |  |  |  |  |                                         |         |  |  +--| (100)
|  |     |      |  |  |  |  |                                         |         |  |     +--Apis
|  |     |      |  |  |  |  |                                         |         +--| (83)
|  |     |      |  |  |  |  |                                         |            |  +--Ampulex
|  |     |      |  |  |  |  |                                         |            +--| (100)
|  |     |      |  |  |  |  |                                         |               +--Ampulex_1
|  |     |      |  |  |  |  |           +-----------------------------| (100)
|  |     |      |  |  |  |  |           |                             +-----------Polypedilum_2
|  |     |      |  |  |  |  |        +--| (91)
|  |     |      |  |  |  |  |        |  |     +--Dendrolimus
|  |     |      |  |  |  |  |        |  |  +--| (87)
|  |     |      |  |  |  |  |        |  |  |  |        +--Spodoptera
|  |     |      |  |  |  |  |        |  |  |  |     +--| (100)
|  |     |      |  |  |  |  |        |  |  |  |     |  |  +--Spodoptera_1
|  |     |      |  |  |  |  |        |  |  |  |     |  +--| (100)
|  |     |      |  |  |  |  |        |  |  |  |     |     +--Spodoptera_2
|  |     |      |  |  |  |  |        |  |  |  |  +--| (99)
|  |     |      |  |  |  |  |        |  |  |  |  |  +--Helicoverpa
|  |     |      |  |  |  |  |        |  |  |  +--| (99)
|  |     |      |  |  |  |  |        |  |  |     |  +--Arctia
|  |     |      |  |  |  |  |        |  |  |     +--| (100)
|  |     |      |  |  |  |  |        |  |  |        +--Arctia_1
|  |     |      |  |  |  |  |        |  +--| (48)
|  |     |      |  |  |  |  |        |     |  +--Brenthis
|  |     |      |  |  |  |  |        |     +--| (50)
|  |     |      |  |  |  |  |        |        |     +--Iphiclides
|  |     |      |  |  |  |  |        |        |  +--| (89)
|  |     |      |  |  |  |  |        |        |  |  +--Iphiclides_1
|  |     |      |  |  |  |  |        |        +--| (97)
|  |     |      |  |  |  |  |        |           +--Iphiclides_2
|  |     |      |  |  |  |  |     +--| (87)
|  |     |      |  |  |  |  |     |  |  +--Lamprigera_1
|  |     |      |  |  |  |  |     |  +--| (99)
|  |     |      |  |  |  |  |     |     |              +--Temnothorax_1
|  |     |      |  |  |  |  |     |     |           +--| (97)
|  |     |      |  |  |  |  |     |     |           |  +--Acromyrmex_1
|  |     |      |  |  |  |  |     |     |        +--| (100)
|  |     |      |  |  |  |  |     |     |        |  |  +--Eciton_1
|  |     |      |  |  |  |  |     |     |        |  +--| (100)
|  |     |      |  |  |  |  |     |     |        |     +--Ooceraea_2
|  |     |      |  |  |  |  |     |     |     +--| (94)
|  |     |      |  |  |  |  |     |     |     |  +--Ampulex_2
|  |     |      |  |  |  |  |     |     |  +--| (95)
|  |     |      |  |  |  |  |     |     |  |  +--Vespula_3
|  |     |      |  |  |  |  |     |     +--| (99)
|  |     |      |  |  |  |  |     |        |  +--Cotesia
|  |     |      |  |  |  |  |     |        +--| (100)
|  |     |      |  |  |  |  |     |           +--Cotesia_1
|  |     |      |  |  |  |  |  +--| (100)
|  |     |      |  |  |  |  |  |  +---Cloeon_1
|  |     |      |  |  |  |  +--| (94)
|  |     |      |  |  |  |     |             +--Ceratitis
|  |     |      |  |  |  |     |          +--| (93)
|  |     |      |  |  |  |     |          |  +--Lucilia
|  |     |      |  |  |  |     |       +--| (100)
|  |     |      |  |  |  |     |       |  +--Glossina
|  |     |      |  |  |  |     +-------| (100)
|  |     |      |  |  |  |             |  +--Polypedilum
|  |     |      |  |  |  |             +--| (100)
|  |     |      |  |  |  |                +--Polypedilum_1
|  |     |      |  |  +--| (75)
|  |     |      |  |     |        +--NHA1_prot_size_637_strand__
|  |     |      |  |     |     +--| (73)
|  |     |      |  |     |     |  +--NHA2_prot_size_656_strand__
|  |     |      |  |     +-----| (100)
|  |     |      |  |           |     +--NHA3_prot_size_1204_strand__
|  |     |      |  |           |  +--| (63)
|  |     |      |  |           |  |  |     +--NHA5_prot_size_754_strand__
|  |     |      |  |           |  |  |  +--| (98)
|  |     |      |  |           |  |  |  |  +--NHA6_prot_size_708_strand__
|  |     |      |  |           |  |  +--| (100)
|  |     |      |  |           |  |     +--NHA7_prot_size_589_strand_-
|  |     |      |  |           +--| (100)
|  |     |      |  |              +--NHA4_prot_size_786_strand__
|  |     |      +--| (74)
|  |     |         +----Amphibalanus
|  |  +--| (98)
|  |  |  |  +--Nymphon_5
|  |  |  +--| (100)
|  |  |     +--Nymphon_6
|  +--| (88)
|     +--Nymphon_4
|
+--Nymphon_2


Consensus tree in newick format: 

(Nymphon:0.0000021483,((Nymphon_1:0.0000021462,Nymphon_3:0.0000021462)93:0.0000027237,(((Oedothorax:2.8377984600,(Penaeus:1.2715669649,(((Tigriopus:1.3038871513,NHA8_prot_size_329_strand__:0.7843199428)99:0.5387436047,(((((((Diaphorina:0.0000023866,(Diaphorina_1:0.0000021496,Diaphorina_2:0.0835556111)54:0.0075388602)100:1.1978009358,(Nezara:0.6265390674,Apolygus:1.0409312660)100:0.5336692528)84:0.2509263406,(Diaphorina_3:0.0000024525,Diaphorina_4:0.0271306573)100:1.5642599518)100:0.4981474267,Megalurothrips:2.0802039340)90:0.2333405408,(Ephemera:0.9346574963,Cloeon:0.9421628035)100:0.7398312409)100:0.2742349193,((((((((Holotrichia:0.2360574687,((Tenebrio:0.1261565487,Zophobas:0.1892703982)100:0.0943206211,(Diabrotica:0.1940882647,(Dendroctonus:0.0547154425,Dendroctonus_1:0.0000029933)100:0.1999070255)95:0.0281711999)95:0.0570063107)95:0.0897118995,Lamprigera:0.2797986912)95:0.1600676082,(((Vespula:0.0057855619,(Vespula_1:0.0017034672,Vespula_2:0.0056307615)100:0.0024731553)100:0.0660407617,(Polistes:0.0221016959,Mischocyttarus:0.0371910215)94:0.0558479525)92:0.1391304779,((((Eciton:0.0688427729,(Ooceraea:0.0026793369,Ooceraea_1:0.0063577255)98:0.0482581922)96:0.0196753065,((Temnothorax:0.2252392987,(((Atta:0.0289086978,Acromyrmex:0.0206986613)91:0.0039860041,Trachymyrmex:0.0178308038)96:0.0198145778,Trachymyrmex_1:0.0235329122)99:0.0313978363)100:0.0727242867,Harpegnathos:0.1100739535)76:0.0458397563)100:0.1011886286,(Frieseomelitta:0.0526148512,Apis:0.1077725359)100:0.1609028031)73:0.0280772093,(Ampulex:0.0038183597,Ampulex_1:0.0075333574)100:0.1903543017)83:0.0422484209)90:0.1341885044)99:2.1648263273,Polypedilum_2:3.5786605541)100:8.6434158754,((Dendrolimus:0.2050805240,(((Spodoptera:0.0052943712,(Spodoptera_1:0.0000027237,Spodoptera_2:0.0684107426)100:0.0161719521)100:0.0351588257,Helicoverpa:0.1724494653)99:0.0716456641,(Arctia:0.0112995643,Arctia_1:0.0659477842)100:0.2314682482)99:0.1010174922)87:0.0708138874,(Brenthis:0.2126955075,((Iphiclides:0.0129960911,Iphiclides_1:0.0371110348)89:0.0563040220,Iphiclides_2:0.0118509564)97:0.1820208503)50:0.1020577912)48:0.1715361689)91:0.7322515291,(Lamprigera_1:0.8547605729,(((((Temnothorax_1:0.0313048372,Acromyrmex_1:0.2137833138)97:0.0309311804,(Eciton_1:0.0466610482,Ooceraea_2:0.0195313842)100:0.0603832210)100:0.1009229382,Ampulex_2:0.0739015043)94:0.0600840166,Vespula_3:0.3312481422)95:0.0934015871,(Cotesia:0.0203237254,Cotesia_1:0.0057660916)100:0.4872958130)99:0.4705281414)99:0.4313071885)87:0.2069944372,Cloeon_1:1.3970049594)100:1.0465613372,(((Ceratitis:0.6350277829,Lucilia:0.4882119180)93:0.0753965890,Glossina:0.7607399481)100:0.5725469787,(Polypedilum:0.0315657374,Polypedilum_1:0.0000027255)100:1.0552597217)100:2.3541216413)94:0.2578097757)100:0.4622903169,((NHA1_prot_size_637_strand__:0.3354389426,NHA2_prot_size_656_strand__:0.7977404682)73:0.1947949330,((NHA3_prot_size_1204_strand__:0.5394680843,((NHA5_prot_size_754_strand__:0.1906610085,NHA6_prot_size_708_strand__:0.1666402691)98:0.0946880274,NHA7_prot_size_589_strand_-:0.1452332552)100:0.6009933537)63:0.2137140196,NHA4_prot_size_786_strand__:0.4142513436)100:0.8540978910)100:1.7298404500)75:0.1573311986)96:0.2743903673,Amphibalanus:1.5022496469)74:0.1697470137)80:0.2502799701)100:1.1662595479,(Nymphon_5:0.0435192839,Nymphon_6:0.0000021483)100:0.0338354262)98:0.0097037400,Nymphon_4:0.0038542346)88:0.0000021483)98:0.0395023570,Nymphon_2:0.0109970899);

TIME STAMP
----------

Date and time: Sun Mar 12 22:04:06 2023
Total CPU time used: 1115.46 seconds (0h:18m:35s)
Total wall-clock time used: 1128.14723 seconds (0h:18m:48s)

visualized in: http://www.trex.uqam.ca/view.php 

# March 10, 2023: Actually blasting these species 
## cytochrome c oxidase?? 
Also, I noticed that cytochrome c oxidase comes up pretty frequently. I wonder why. I'll try aligning these in Drosophila. 
ok I aligned NHA2 and cytochrome c oxidase in humans and there is virtually no overlap. So I'm not collecting those sequences.

Total protein accession numbers from all the HitTables: 555
 
## links for cytochrome c oxidase and NHA sequences:
https://www.genecards.org/cgi-bin/carddisp.pl?gene=SLC9B2#proteins
https://www.genecards.org/cgi-bin/carddisp.pl?gene=MT-CO1#proteins-references

## HitTable.compiler.R (!!!!!)
output = 2023-03-10-all_protein_orthologs_HitTable.csv
number of rows: 216 
contains merged HitTables with duplicate protein accession numbers removed 

## Running ncbi_parser.py
It's March 10, at 2:36 pm. error: 

Traceback (most recent call last):
  File "ncbi_parser.py", line 312, in <module>
    filtered, trashed, log = filter(acc_list)
  File "ncbi_parser.py", line 201, in filter
    row = prot_ncbi(acc)
  File "ncbi_parser.py", line 30, in prot_ncbi
    prot_handle = Entrez.efetch(db = 'protein', id = acc, rettype = 'gb', retmode = 'xml')
  File "/Users/patriciazito/anaconda3/lib/python3.7/site-packages/Bio/Entrez/__init__.py", line 196, in efetch
    return _open(request)
  File "/Users/patriciazito/anaconda3/lib/python3.7/site-packages/Bio/Entrez/__init__.py", line 586, in _open
    handle = urlopen(request)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 531, in open
    response = meth(req, response)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 641, in http_response
    'http', request, response, code, msg, hdrs)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 569, in error
    return self._call_chain(*args)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 503, in _call_chain
    result = func(*args)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 400: Bad Request__

I'll try running this again in 30 min or so. 
Same code at 2:54 pm:

Traceback (most recent call last):
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "/Users/patriciazito/anaconda3/lib/python3.7/http/client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/Users/patriciazito/anaconda3/lib/python3.7/http/client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/Users/patriciazito/anaconda3/lib/python3.7/http/client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/Users/patriciazito/anaconda3/lib/python3.7/http/client.py", line 1016, in _send_output
    self.send(msg)
  File "/Users/patriciazito/anaconda3/lib/python3.7/http/client.py", line 956, in send
    self.connect()
  File "/Users/patriciazito/anaconda3/lib/python3.7/http/client.py", line 1384, in connect
    super().connect()
  File "/Users/patriciazito/anaconda3/lib/python3.7/http/client.py", line 928, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "/Users/patriciazito/anaconda3/lib/python3.7/socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "/Users/patriciazito/anaconda3/lib/python3.7/socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "ncbi_parser.py", line 312, in <module>
    filtered, trashed, log = filter(acc_list)
  File "ncbi_parser.py", line 201, in filter
    row = prot_ncbi(acc)
  File "ncbi_parser.py", line 30, in prot_ncbi
    prot_handle = Entrez.efetch(db = 'protein', id = acc, rettype = 'gb', retmode = 'xml')
  File "/Users/patriciazito/anaconda3/lib/python3.7/site-packages/Bio/Entrez/__init__.py", line 196, in efetch
    return _open(request)
  File "/Users/patriciazito/anaconda3/lib/python3.7/site-packages/Bio/Entrez/__init__.py", line 586, in _open
    handle = urlopen(request)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 525, in open
    response = self._open(req, data)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 543, in _open
    '_open', req)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 503, in _call_chain
    result = func(*args)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/Users/patriciazito/anaconda3/lib/python3.7/urllib/request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>__ 

same code at 3:11 and I'm getting the first error message.I'm checking the vs code. for some reason the importing read_csv broke. ok somewhere in merging the goddamn columns it fucked up. This is an error from the R code. 

But ok the R code looks normal. the compiled dataframe has everything in order. 
I just changed the indexing. Before, when I used the csv table directly from ncbi, the accesion number was the second column. I don't know if R changed the number of columns because it was processed there, but now it works fine. 

Running ncbi_parser.py again. Second error (node8). maybe try again in like 10 min. I did not wait 10 minutes but I got the first eror again, which is like, weird. Omg, it's reading "X2" as an entry. That's the header, of course it'ns not going to find any protein accession number under silly goofy "X2".

just tested: 
>>> acc_list[0]
'KAG7156541.1'

so. let's see if it fixes that. nope. node8 error again. I'm inclined to think that it's weird that it's not even telling me which accession number it's assessing, so maybe it's not an error bc of the time of the day.

I tried running only the first accession number (acc_list[0]) and it returned me node8 (twice). I think ncbi just told me I worked too much today. I'm gonna have to do this step either tomorrow (before travelling) or later tonight (preferrable). After filtering through them I still have to check them manually to (1) check they're not like weird or partial sequences, but also to get the cds. 

Actually thinking about it, I don't think the partial sequences should be an issue. I'm (hopefully) getting so many species anyways, I doubt I'll have a perfect alignment, I will have to trim these at some point anyways. I'll leave them here and if they throw everything off, I'll take them out, but otherwise, I don't see the issue.

Tried running again at 5:54. It ran up to some point and then I got the node8 error again. I do think this is a server/ internet issue. :/ 

# March 9, 2-23: BLASTing more species 
I want to blast and do this whole procedure to get more species. To do this, I'm going on ncbi and acquiring more "confirmed" species. I will use their protein sequences to do blastp and see THEIR closely related sequences within arthropods. 

These are the protein accession/ species I found and will be using as the query: 

Searching: "SLC9B" (all organisms) 
JAB97576, Ceratitis capitata (vespa)
OQV26214.1, Hypsibius exemplaris (tardigrada)

Searching: NA+/H+ antiporter AND "arthrpods"[porgn:__txid6656]__
AAF80554.1, Aedes aegypti (mosquito) 
KRT81874.1, Oryctes borbonicus (beetle) 
ACM47586.1, Anopheles gambiae (mosquito) 
KOB72952.1, Operophtera brumata (moth) 
EEB12185.1, Pediculus humanus corporis (tick)
EFN88906.1, Harpergnathos saltator (ant) 
GFQ82017.1, Trichonephila clavata (arachnid) 

can't forget I will also have to change the r script: make a for loop and rbind all Hittable files within  folder. Then remove duplicates. Then manually check each of them. Then write another quick script to select columns and cat()/ sink() to write new fasta files :) 


# March 8, 2023: Redoing BLAST yet again 
This is literally the third time I'm doing this. But it's gonna be worth it. I think. I hope. 
I'm just SO SO SO tired of having to redo the same work again and again. Oh my god. 
ok I only got about 20 protein sequences, so I think I need to relax some of these curation parameters, also to avoid some of the extra work, I'm thinking of compiling the HitTables, that way I won't have to run ncbi_parser for each NHA gene again. save the extra work oof. 

## resources: 
Hey these people did the same thing as I did (basically!). But prettier. 
https://widdowquinn.github.io/2018-03-06-ibioic/01-introduction/03-parsing.html 

## comments from 1x1 meeting: 
- Sean’s paper: review NHA function, DD motif, different domains (evolutionary changes, structural and functional domains, etc.) look new papers? And how do they evolve. 
- SMBE essay 
- alignments don't look right: 
	- check alignments: 5, 6, 7 together, also align TRY (CDS and full gene) and 8  (full gene and CDS), and 1 2 and 3
- check parameters for ncbi parser:
	- they look ok 
- which trimming software: hmmcleaner or trimmal 
	- (do later) - think about this after creating all initial phylogenies  
- mitochondrial results? 
 	- include them, but take note of which are which 
- NHA1 and NHA2? 
	- My question was regarding the NHA1 and NHA2 paralogs in other species. It seems like both Drosophila and humans have two copies of the gene. So if we're "coalescing" our eaff paralogs, how do we know which sequence came from which (ancestral NHA1 or ancestral NHA2). But Carol pointed out Drosophila is more derived, so I guess it's true, I might not have to worry about this in the future. 
- introduce variation without compromising gene sequence (conserve introns, or gene duplication for E. affinis). 
	- I wonder the trade-offs for these two mechanisms. 
- check alignments: 5, 6, 7 together, also align TRY (CDS and full gene) and 8  (full gene and CDS), and 1 2 and 3
	- I've just checked. I'll have to see if I can find the insertion of NHA3 anywhere else. Also fix NHA7. Might do genome x transcriptome again. 

# Feb 29, 2023: Tigriopus disappeared 
I ran the code this morning and that seemed to do the trick. I'm now getting about 75% of all the proteins in the filtered section. 
Looking again, however, I noticed I'm simply not getting some of the proteins I had before? I might've screwed something up on getting the 
or checking the coverage of proteins that have an assembly page. 
Honestly, this would be a lot easier if I just set BLAST to give those sequences (no XP. nothing). Cuz the other ones usually have scaffold information too. The others don't. Pros and cons, I might be getting less sequences, but they get correctly curated, and I have less work to do. I might make two different codes - one for the normal good sequences and another to deal with the XP ones that come up on the search. I feel like I might already get enough sequences anyways so. ugh. I can never find the right balance to work and things of the sort. I still have to work on my other shit, god fucking damn it. 


# Feb 28, 2023: Redoing BLAST 
Since I'm having trouble validating my CDS sequences, I'll be using Nick's as the query. 
Additionally, I'll be removing E. affinis from the potential taxa, so we may get more of other species.
The query MUST be proteins, otherwise no results will show up. NHA doesn't seem to be well conserved across other taxa. 

I tweaked my alt_ass_ncbi() so it takes in the XP sequences, but now I'm getting WAY too many results. 
I think I'll have to increase the threshold for coverage, and see if I can filter for scaffold N50 and number of scaffolds again. ---> Decrease manual work!!! 
Also: I'll still have to get the CDS sequences for these. Think about how.
Actually, the XP girlies have a link to the CDS. Lemme see if that works. nope. I have no idea how I'll get these goddamn CDS sequences because they simply don't have them, it's usually the whole scaffold. I think I have no other choice: I'll have to blast their assemblies. 

it was working up to now, but it started throwing me node 8 erorrs. I'll have to run this tomorrow. 


# Feb 26, 2023: Links for Genbank + ncbi database "standards" 
## links: 
https://www.ncbi.nlm.nih.gov/genbank/samplerecord/
https://www.ncbi.nlm.nih.gov/assembly/basics/#Comparative
https://www.ncbi.nlm.nih.gov/assembly/model/


# Feb 20, 2023: Tweaking 
## Changes in ass_ncbi(): 
I had to change a couple of things on this function bc it kept throwing me errors when I tried running it on my NHA1 HitTable. 
(e.g. sometimes they had no results from the assembly search thingy -> I made another another if to check that it will have any
results, as well as set all defaults to be False). There was another error for RSSeq I think (getting the bioproject accession
number. I decided to just delete that. If the authors can't put the bioproject accession code on the right place then fuck it. 
Probably not a good sequence anyways. I'd rather lose a couple of assemblies than to keep tweaking this code to fit to very ind. 
errors that each author makes on their sequences. 

I'll have to run this new code on NHA7 again though just to see if that changed a lot. I'll put all the usable data inside a data
folder and the "old versions" of this code output into another folder called "old-runs".

## Alex and Joye's comments: 
Okay, so a few notes:
Formatting notes: I think the contig n50 and scaffold n50 columns should be together. I also think that the columns related to the overall sequencing/assembly project should be grouped together, with the gene-specific info not interspersed.
Having coverage number without sequencing technology information isn't super helpful imo. If possible, fetching the sequencing technology used would be really helpful for knowing what to look out for.
It is super important to get nucleotide sequences  (the CDS specifically) for the work most of us are doing. I know that starts to massively complicate things, as there are a a number of entries that have protein entries that aren't tied to a corresponding sequence. However, most of the time (especially for decent quality entries), there is a transcript entry that is linked to the protein (on the entry in NCBI, they are hyperlinked in a standardized way).
On the topic of nucleotide sequences, it would be awesome if we could also get the gene position. I typically record the chromosome/scaffold, start and stop position, and whether it's sense/antisense (+/-).
Would it be possible to retain the sequences that are being discarded for missing information and just flag/highlight them for manual review? The amount of effort that each uploader includes varies very widely, as you've seen, so it would be best if we could make the final call on discarding them on our own (plus, that help us keep track of which ones we've consciously chosen not to include rather than simply missed or something).

## Adjustments: 
I'll try to implement a couple of these things and also re-do the BLAST searches already excluding E. affinis -> so hopefully 
Ill be able to get more different species. 

# Feb 18 and 19, 2023: Quality check 1? 
## comparison to my manual work 
So this works, but I'm missing 8 species from my manual collection. Kind of going through which step they were filtered out, I 
think it's either during coverage or during assembly. This is mostly because the ncbi annotation thingy doesn't seem to have a 
clear standard on what it should and should not have. Some entries don't have a link to the assembly page, and some don't have 
coverage information, you have to go to their bioproject or manually search for it. (SO ANNOYING). I've also tried efetching and 
esummarying from the bioproject page but it seems like the biopython Entrez package just wasn't designed to get that information? 
See commit for more information, but in summary, it can't read it as an xml. Downloading the information as a text doesn't provide
any information and esummary doesn't have any info either. ugh.

## A couple of things I'm thinking of implementing: 
1. getting gene id 
2. getting CDS sequence
3. find original paper id on pubmed? 
4. manually searching for assembly, but matching it with the bioproject id. 

## ok I think I got #4, but god damn it it doesn't work bc of annotation again 
so I'm searching on assemblies for the species name. (testing w the first missing result, Hyalella azteca
Error 1: The right bioproject doesn't come up. These scientists did two bioprojects, one much better than the other. The best one
shows up on the BLAST result, but not the second one. Sarching both through Entrez and online, the only assembly that shows up 
is the BAD ONE. NOT THE GOOD ONE. And guess what, 4 entries come out!!! They seem to be the same thing, but with different notations
so when I try parse through, the same information shows up in difference places!!!! :) (: :) (: 

## ok I think I got it 
Now instead of getting 14 proteins, I'm getting 30. Still have to re-implement getting genome coverage though. And I guess the 
assembly saerch problem there's not much else I can do. I'm checking the missing ones again, (I now have 6), and I'm missing Salmon
Louse. I don't really know the others, so I don't care much. But I'll try to fix it for this one. 
it's literally bc it doesn't show up on the assembly search. fine. I guess I'll have to add those by myself. In the meantime I'll 
try getting the original paper id and the nucl sequence? 

run blast on a specific organism: https://www.biostars.org/p/208772/

## finished it
hallelujah. Now onto working on my grants, homework, quizzes and next scripts. 


## the nucl issue. (Can't find paralogs as easily blasting DNA -> it's not a very conserved protein).
just realized I probably will have to start all over again with the nucleotide sequence, THEN protein, THEN assembly. :( 
But also I tried blasting it with the nucleotide sequence (excluding E affinis) and I'm getting no results. I think this really 
is the best way to go about this. (Getting more proteins without compromising sequence quality).
So I'm gonna finish the code as it is, I think and manually add Hyalela azteca and salmon louse individually. I think in the grand
scheme of things I'll be getting a lot of other species to make up for losing a couple of these anyways. In the future: write script
to combine all dataframes, remove duplicates, find remaining paralogs and get nucleotide sequences.  


# Feb 16, 2023: Filtering works! 
## progress on filter(): 
it now works! I ran the whole list of accession numbers that I got for my first blast search and it resulted in 14 good acces-
sions. This is good, but also I had more in my previous one. I think one flaw of this program is that bc I'm looking at a par-
ticular place (e.g. assembly) entry, if the protein annotation isn't VERY good and standard (e.g. they have the link for some-
thing like, on bioproject, or nuccore, anywhere else but here), my code discards the protein bc it just can't find the info. 
rip. 
it works though. I tried implementing a log thingy for the results, but it failed me. I might tweak it again in the future. 
I think for now I'll try getting the accession number and blast paralog thingy. 

## progress2 on filter(): 
I've installed a maybe list, where it checks whether it was either sequenced on pacbio or if it's available on refseq. I ran it 
again and I got 74 protein entries in there. That's a lot. 
I'll have to ask Alex if these are immediate green flags and can be added into "filtered" or if I should look and see if there's
any other pattern that I can look and parse through. (e.g. I'd have to find other ways to get assembly information). TIRING. 
ugh. but ok. at least it works. 
Also. I'm thinking that if it is a paralog... maybe it should show up on this original blast result... Should we really have
to look for other paralogs? Maybe I can finish this script as it is, and start another one to combine datasets (e.g. results from
running this script on the blast result for paralog1, paralog2, paralogn, etc. And while checking for duplicates, also search for
possible paralogs.

## maybes 
ok I actually just searched it up online (https://www.ncbi.nlm.nih.gov/books/NBK50679/), we can only trust that refseq sequences
are truly good if they have been curating (i.e. their refseq status = "REVIEWED" or at leas "VALIDATED").
link: https://www.ncbi.nlm.nih.gov/books/NBK21091/table/ch18.T.refseq_status_codes/?report=objectonly  
Where to find this information? 


# Feb 15, 2023: Pandas and local blast 
## Thoughts on pandas
I'm thinking of using pandas for both reading and writing the initial and final csv results. I'll have to relearn how to use 
it, just looking at some of the tutorials, I think filtering will be MUCH easier, if I work with pandas dataframes as opposed
to the dictionaries that I am currently using. Maybe something to work on this weekend. 
I'll actually keep using the dictionary cuz I feel like I'm still not sure about how many columns I want, or what parameters 
I might have to add and tweak, and so working w indexes sounds like shit.

## Thoughts on BLAST+ 
Alex asked something interesting. It'd be nice if we could use "remote" blast from our command line into the online database.
I found some links online that might be helpful. This could maybe not only compliment well this part of the project (writing)
a single script to obtain orthologs, but maybe it could be helpful in looking for the orthologs in that species. (Maybe write 
another script for this). Will probably have to manually add them though. (I find it hard to think about hard parameters for 
deciding whether it looks like a paralog or not. A real human has to look at the alignment and decide? Or maybe decide by iden-
tity percentage, e-value, and size? Good god. That is a lot of work.)

## Links for remote BLAST+ tutorials
https://github.com/jarekbryk/localblast
https://www.biostars.org/p/350628/
https://widdowquinn.github.io/2018-03-06-ibioic/02-sequence_databases/03-programming_for_blast.html
https://www.tutorialspoint.com/biopython/biopython_overview_of_blast.htm
https://www.ncbi.nlm.nih.gov/books/NBK569856/

## Summary of things to implement: 
1. Maybe also get the accession number for the original paper (this has to checked manually)
2. Remote python BLAST+ for paralogs? (maybe incorporate this into pipeline) -> solves issue 2 (Feb 10)


# Feb 14, 2023: Eureka! look_ncbi() works!   
## Progress 
the code works. I've made into a function so it only needs an accession number and it retrieves all the information for the
what it's going to be the columns. 
I'll work on the other functions during the week. I've also spoken to Alex and Joye and I'll have them review the results for
my first test dataframe (possibly solve issue 1 from Feb 10). They'll tell if this curation process is actually quality control 
for the sequences. I know it's not perfect, but it might save a lot of time for starting. I'll just be in charge or reviewing 
the papers (see if inbred and stuff) and looking for paralogs in that species. Even that might be automated someday, who knows. I 
need to figure out local blast into the online database.


# Feb 12, 2023: crying at a coffee shop on a Sunday morning.
## A possible (bitter) solution for issues 2 and 5 (see Feb 10, 2023): 
I'm thinking I'll collect at least these protein sequences and THEN blast them into their respective genome. 
Which is basically what the folks at JC are doing, but I'm doing an extra whole step (this script) before that. 
Is this unnecessary. I feel like it is. I've come too far and I'm too proud to stop. fuck my life. :( 

if I do this, these would be the next steps: 
1. BLAST NHA sequence into online BLAST 
2. download that CSV file 
3. import CSV file into python and extract column containing protein accession numbers 
4. Entrez that shit and extract info -> put those into new variables 
4. load all of these new variables into a new row dataset for the accession number 
5. filter through according to new parameters (e.g. scaffolds) 
6. export new dataset 
7. do this again for all NHA sequences 
8. compile these into one master doc and delete repeated (but tell me if they showed up multiple times) 
9. find out if they are inbred (manual?). if not: out, if yes: keep it 
10. local blast to their genome and see if they have any paralogs in that organism. 
11. use these sequences for tree. 

## Progress + possible cause of node8 and or url error 
the summary for assemblies now works. 
I think the errors I keep randomly getting from the same code (sometimes it works and then it just doesn't anymore) is because
I use the same handle. I think the command works again once I handle.close() or change the variable name. OR there is a problem
with the input. (e.g. wrong parameters, id does not work, etc.) Maybe certain code would've worked, so make sure you close the 
handle AND change the name of the variable, just to be sure. This could've saved me SO MUCH TIME. but oh well, you live and you learn.

## the link that helped me get through this part of the coding: 
https://dmnfarrell.github.io/bioinformatics/assemblies-genbank-python

## things to work on next work session: 
Now that this works I should be almost done with the core of the script. I just need to get the input.
So: find a way to get assembly iud.  


# Feb 10, 2023: Entrez is not a bitch. I'm just extremely obtuse. 
## Progress 
Entrez is now working. I just didn't realize the dict was nested inside the output of the .read() function. 
I've had a meeting w Carol and she said this might not be the best way to deal w the gene mining thing bc it's hard curating. 
(might get a lot of trash sequences). it's true. 
I'll have to work on these over the weekend, but these issues have been on my mind: 

## Issues to think about: 
1. hard to curate (I'm having a hard time extracting scaffold info from the Entrez databases) 
2. I'll probably still have to back to each species one to look for each respective paralogs 
3. will have to go back at each individual paper and look to see if species was inbred before genome sequencing 
4. could cause a bias? most of the species I'm using will be somewhat closely related? 
5. will probably have to do both a BLAST for nucleotides AND proteins. a lot of these are not linked together?  
this is literally making me cry. 

## If this doesn't work: 
I'll have to look at each species genome and transcript. I'll end up with a much smaller number of species, but hopefully their
quality will be better. 


# Feb 7, 2023: Entrez is a bitch 
## Comments on progress 
I've spent my whole weekend trying to work with Entrez. I was able to access the Genbank information from my accession number, 
however, the same command can be run and sometimes work and sometimes not work. I've also didn't realize that, potentially, one
of the reasons my .read() or xmltodict() function wasn't working is because I wasn't using the right function. 
Maybe I didn't have to create a new whole ass function, I could've used .parse(), which is already a function on etools. 
The painful thing is: I could've seen it. I just can't fucking read. 
The function itself isn't working right now, but I bet it's because etools is being moody again. 
I still have a quiz today + find papers so I don't know how much I'll be able to work on this today. ugh. 

## Current efetch attempt: 
handl = Entrez.efetch(db = "protein", id = "TRY75264.1", rettype = "gb", retmode = "xml")
readabl = handle.parse()
handl.close()


# Feb 5, 2023: Learning Entrez 
## Useful Links 
video tutorial: https://www.youtube.com/watch?v=iCFVVexp30o
and: https://www.youtube.com/watch?v=aETx4MyXukk
available in unix: https://www.ncbi.nlm.nih.gov/books/NBK179288/ 
convert accession number to UID: https://www.ncbi.nlm.nih.gov/IEB/ToolBox/SDKDOCS/ACCESS.HTML 

## Script Structure/ Plan 
I want my script to do the following: 
1. BASH: Getting Accession numbers 
Input: query (NHA predicted protein sequence)
Do: Run blast save csv file. 
	save organism, e-value, identity percentage and the accession columns 
Output: query-blast-res-summary.csv: a new dataframe containing these four columns

2. Python: Scrape info 
Input: query-blast-res-sum.csv
Do: Entrez.fetch() each accession number
	save the following as new columns: protein accession, protein sequence, protein-size, chromosome
	add these columns to quert-blast-res-sum.csv
	then do Entrez.elink() to get assembly accession number 
	do another Entrez.fetch() to corresponding assembly accession id 
	save the following as new columns: accession number, sequencing tech, number of scaffolds, N50, coverage, assembly method
	add these columns to query-blast-res-sum.csv
Output: query-blast-res-detailed.csv: a new dataframe containing 14 columns 

3. R: Filter 
Input: query-blast-res-detailed.csv 
Do: filter these according to number of scaffolds, N50, coverage and assembly method 
	save rows that are being filtered out and add another column with what step they were filtered out 
	save rows that are passing 
Outputs: query-ortholog-trash.csv: contains all rows that were filtered out
	query-ortholog-filtered.csv: contains all rows that have passed
	query-ortholog-log.txt: contains percentage of rows passed/ not, why not etc. 

Possible Problems: 
Might have to filter as I go (during step 2) because it might be more efficient. I like doing this in R though because I already 
	know how to do it.
After doing this for every paralog, I'll have to combine it into a masterdoc csv file. will have to program this too so it does 
	by itself and gets rid of duplicates. (perhaps by protein accession) 
Then I'll also have to search for individual paralogs in those species. perhaps another script?    

I'll save the files of this project on my computer and on the phylogenetics-final github page (it's how I'm acquiring my data) 
Then after this is done and working I can think about moving files. 


# Feb 4, 2023: Automating Ortholog Search
## Comments
This process is SO tedious. And there are 8 paralogs that I'd have to search through. Considering the size of each results page
I've decided that I'll try to write a code to automate this proccess. 

I've watched a couple of videos on BeautifulSoup to see if it was possible to web scrape ncbi, but apparently: 
1. there is already an e-utilities package for that (Entrez) 
2. ncbi is NOT a static page and I don't have a clue about java 
3. I think I could maybe get some info from the protein accession page, but the assembly page that contains some of the information 
I want is not directly linked to it. So I'd have to browse through more than 2-3 pages and I don't know how to do that yet. 

Here is how I was planning on scrapping WITHOUT Entrez 
Get-assembly-info
1. give an acession number 
2. URL has a structure, ftp the assembly_stats.txt file 
3. open it on a
grep columns of interest 
4. write new csv file  

Find-accession-numbers-from-BLAST 
1. run BLAST online  
2. save csv file 
3. filtering step? 
4. get Genbank accession -> new URL
5. ?

These are data I need for my columns: 
1. organism: ORGN 
2. protein accession: ACCN 
3. protein sequence 
4. chromosome 
5. protein size 
6. sequencing-tech
7. number of scaffolds 
8. scaffold-N50
9. coverage 
10. assembly-method
11. genome-accession 


# Feb 2, 2023: NCBI BLASTP 
## Comments 
I've found 12 crustaceans that contain NHA gene. I'll have to go back and search through the original papers to see 
if they did inbreeding for the genome sequencing. This is essential because if mapping algorithms often can't differentiate
heterozygous sequences from other paralogs. 

After this "filtration" step, I'll also have to search each individual species for all their paralogs. 

This will have to be repeated for the the other species. One curious thing, however, most of the species I've found from this 
initial search are hexapods, chelicerates and crustaceans. I've also tried blasting Dmel-NHA2 and all the results were Drosophila.
I wonder if this is because NHA is not well conserved across animals, or if this is a bias in the genome information. (a LOT of 
Drosophila everywhere and not enough of anything else). I've tried filtering "Crustacea" [Organism] and none came up.


# Jan 31, 2023: NCBI BLASTP
## Search Parameters: 
query sequence: (NHA7 CDS sequence by Nick)
MHGTTRRNSRYQQIPPATVHEDEVPQYPPPAYPGKIKNPGRIKKAYDSFKQTLQTNRITSHFFPPKGEVATNITLMIAVVIIFFCARAVLGKYSALGGTIFAVFILVFFALVAGQIVLQFAALISKLAGFDIRIPQLLGMMAVGIFCKNVPYNSHEFNSPECLNRSLTQGTIHEAFHGNISALTGHDDPNAHGVVMNVHDALKDEHERIVEHLEKTTVNPKFSSTARIFHAKVQDFKSSTSNDSQSSHSEHLDGEGIKSMPESDDHHHRARRSGGHDEPAVYRDPCVKRFIGGDVDPTVKGILRSTCLTVILLMAGLELDPPQLWRLKWIVLRTTFIPCIVEAFAAALFCYLILGFPFLPGLCFGFVLCGVSPAVIIPGLVNLSQRGYGVKKGIPTLVIATCSADDLVAIGGFGIAAGITFNPDASISDLASHGPLEVLLGIAFGIFWGYICQWFPSKQNANHVFFRWVLLTAGGLFALFGAHMVHYDGAGGLACVIMAFVASIQWRREGWGDHNPVTDIYNKVWIILSPVIFSLIGTNINAEKMDGATVGLGVAVLFCCFITRSFFTFWSAVCGGLETKEKLFLSISWLPKATVQAALGMGETILTLAVLSIAISAPIGAILILALGPVLLPNDFEGEDGEAGLKEVAKEHMTEVKHH

Database: non-redundant protein sequences 

Organism: Arthropoda (taxid: 6656) 

## Results
Results are saved on this folder under: 2023-01-31-NHA7-HitTable
Relevant sequences will be stored in curated-orthologs.csv file on my personal google drive

## Comments 
I've found this method slightly more efficient than looking for specific species like the the Molecular Journal Club does. 
(They seem to search through specific taxa and their genomes?) 
Simply because it saves me the time of blasting to see if they even have the gene. (e.g. Daphnia)

I wonder, however, if this won't give me some sort of bias in my future phylogenetic trees. (e.g. the gene might appear more
conserved or younger than it actually is?). 

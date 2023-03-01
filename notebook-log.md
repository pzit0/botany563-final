# Project: NHA gene/ protein family in E. affinis and closely related species
This file contains the commands, and outputs of finalized data. 

Get URL for git commit: 
echo "$(git config --get remote.origin.url | sed -e 's/\.git$//g')/commit/$(git rev-parse HEAD)"

## Data: 8 paralogs in E. affinis + curated sequences from other species 
	Currently creating a script to obtain and curate these sequences 
	They will be both DNA (CDS) and protein sequences

## Data Collection: 
###Blast search: 
I'm using Nick's original CDS sequences and translating them into amino acids through the following link: 
https://web.expasy.org/translate/ 

NHA1: 
Blast query: 
MKTKGMAVLSDHHWYNIKSKIELRNLILDLWSNGGASGTATTLDLENPPVQAPKKQPGTVKKSYKKVKSGLQSNRVTTKFFPPQGEVSTVLTITLTVIAVFFVARTVLGPIAGPGGTIFALLVLILFALIGGMAVKMLGMGISCLCGVDIRLPPLLGMLIVGIVMKNVPYNIGQFGREECQGNRSVQFADSLNDLDLNSTDFKEKLMGFDVNIEKYGVLHESMDLPEKMGSNDFKTVGVNSRRRRSSGSHPEPTLIQEKYDPCRKKYIGHELDPLISRSLRTICLTVILLMAGLELDPVALWNLSGMVVRATFVPCFVEAIAVAVFSNLILGFPWSVGFMLGFVLAAVSPAVIIPSLMNLSERGYGVAKGIPTLVIAACSADDVVAISGFGIFLGITFNADAPVLDLALHGPIEVAIGLSFGIGWGILAQWIPNQHHKNMVFFRFLILFSGGLIALFGAGLIHYDGAGGLAAIIMAFVAGMRWRKEGWGDHNPVSKTFRKMWIILEPVIFALIGTEIQIDKIDPATLGLGILVLVLALTLRMIGTFFAVSCGNLNFKEKIFMAFAWLPKATVQAALGPIFLDNAIKNGLTEYIPMGEQILTLAVLSILITAPLGAISILALGPKLLTSNKLEAGLPVHAEDHDVHDEEGEEEEEHH

Deafult options, excluding Eurytemora affinis, excluding uncultured samples, non-representative sequences, etc.  
Output file: 2023-02-28-NHA1-HitTable.csv

NHA2: 
Blast query: 
MDKHIKAVIADTHWCNFGSKEHPKEKTSLFRGTEATYGSVENVDPENSMNHPPAQPGCLSKTMNKIKITLQENMFTTKFFPPQGNVASVLTLCFAVVSVFLMARLVFGPIAGPGGTIFALLILILFALIGGQLIKFIGICLSRITGMDIRLPPLLGMLLVGILMKNVPYNFGQFGRAECFGNRQMDFVDSLHDFPVNTTEFSENFKGKFIDIESYSGKESGEIMNSSVLDLDNGTMDRFLSGEQNSGVDFSSCKKKYIGHELDPVLSRTLRFICLTVLLLMAGLELDPDALWNLSGMVIRATFIPCIVEAMSVAIFSHLILGFPWTVGWMLGFVLAAVSPAVIIPSLLSLSERGYGVAKGIPTLVIAACSADDVVAISGFGIFLGITFNANAPLIDLILHGPMEVAIGVSGGLVWGGLAQWIPNQHSPHVAFFRFIILFFGGLISQFGALLINYDGAGSLAVIIMAFVASLRWRKEGWGDHNPVSLTFRKLWIILEAVIFSLIGTEIQIDKIDTESMWNGILVLCLALILRMISTYFAVSCGNLNVKEKIFMAFAWFPKATVQAAIGTVFLDFAIMNGRTDLIPMGEQVLTLAVLSILITAPLGAIGILGLGPKLLSCDLPAAGQEQDLEENQDPETNQDQTIDPNSEEVIDLQRKQDKFIESENKIGERVKDNDKTREKDLQELLLVISEDETWDGRGEKMKGSNE

NHA3: 
Blast query: 
MDNPNYEEDELGGTTRVLYGATPLYRRGSRIIGGDEEPAGTFAMLRRGSKQTGTEDDRPDYRIRSGSIGGVYPALRRLSIQMGLPGLPVYEEIDLPDDNDDKPSSFTEEKKKPGRVKKSYKKIKRGLQGNKVTSQFFPPKGDVAENITLIIATIILFLMARAVLGTLAAPGGTIFAIFILILFSLIAGQIVIQCAALITKLVGVDIKIPQLLGMMAVGIALKNVPYNQSQFNSPECMNISKSIHDHSDIDVNSTEFVNELGGFRIDPKDVHINHQHSDIAKSLKNIDNINLHGENSVDTENHPNSGPSHHTGVESISNNEDHADQNKTDASKQEPDNEEKHGLNHVEEKEVSHDISHDSNVKTVQQEKHNHGDDQTKDEHGHHITTEEKEEVKHMQVSIMKDHNHTVQQEENIHHEKEVMNIPVHRTPDNHHMIQQEEDSNNSEHSHDEHNHSIVHDKKEEIKNTPVHCTPDQHHMIQQEEHSNNSEHSHDEHYHHEMHEKKEDIKNTPVHITPDRNYTIQQEEDTSRNEYSHDAQDVIHKKIEEVKHTPVHTTPDHNNKYEQLVNNDNPINETNIHSLAKEEKDEVTHVEPHSLQDHNDKKVEHGRSDEQTKHKDIHNQNQGEVKNPRQHLHTDGEAQNQNNETVHNENKMILNHMEDEKSQDSRMTPHSIYDHNEKKITHQQIDNLNNKPITEVLNRPLNKNELNNDVKDSNDINGQGISQQEKKEASQTPQYESKNQKDENGHEMHLHDVKSDNINQDNKEQALANNNTKMKTTPDDAVLNGTDISEIAQGVTKHDVEAAVTKIYQQNVLYNSYEKDESTTENSAEDLVDTKIQNRSRRSSGHDEPQIYVDPCKKRFIGNDLDPLLTRTLRSICLTVILLMAGLELDPPALWRLKWIVLRTTFIPCIIEAFAASLFCYLILGFPFSVGLCFGFVLCGVSPAVIIPGLVNLSQRGYGVKKGIPTLVIATCSADDLVAIGGFGIALSITYNPDAPILSLAFHGPSEVIMGIAFGIFWGYICQWFPSKQNPNHVLFRFIILFSGGLFALFGAHLIHYDGAGGLACVIMAFVASIQWRKEGWGDHNPITDIFGKMWIILAPIIFSLIGTNIVVEKMDGESVALGIAVIVLSMIVRMVFTYFAAVCGGMTAKEKIFLSISWLPKATVQAALGPVFLDNALRDGITEYIPYGEQILTMAVLSIVVTAPLGAILILALGPLLLQSDMVDEDDGQRFDMEEIGSMEKVDEEDEDEIKQH

NHA4: 
Blast query:
MEEMNNNNIEMDKYKQSPPAETVNPGYKDENKPTFVKARKTKRLRMRKSLVKVKRNLQANKVTTQFFPPQGEVATNLTLIVAVIIIFFCARAVLGTIAAPGGTIFALFILILLSLIAGQIVIQVASWISKLVGIDIKIPPLLGMMAVGITLKNVPYNFGQFGRAECIGNVSVEFADSLHNFEINSSEFDEELMGFTVKPSIRLHDIYGAEAQHSLDHTVSENQRISSNVDQHEVFPLNDHEYNPSTADDTLSNVVQKSTPYQERLQGIIQNHIDTLTKIGELHQELTKPTTPSDEDVIGSKHPKMNVFKSPKWPTDHSSEENILNLMDSRHKRTLRSEHAEESTSLPEDSCKKRFIGHELDPLLSRTLRSICLTVILLMAGLELDPPALWRLKWIVLRTTFIPCLVEAFAASLFCYLILGFPFLPGLCFGFVLCGVSPAVIIPGLVNLSQRGYGVKKGIPTLVIATCSADDLVAIGGFGIALGITFNPDASITDLASHGPIEVTMGIGFGIFWGYVCQWLPSRHNKDYILFRFIILFCGGLFALFGAHLIHYDGAGGLACVIMAFVASIQWRKEGWGDHNPITDIFGKMWIILAPIIFSLIGTNIQVDKMNGDTVGLGVAVIVCCILTRSFFTYWSATFGGLNTKEKLFLSLAWLPKATVQAALGPVFLDNALRSGITEFVPYGEQILNMAVLSIVISAPLGAVLILATGPLLLHSDLEVKGSTDEGSDLEEAEKEEEGQEEDAEEREEEDAEDREDEERVEENANKSFKNNSKMLNNEMESVDVCQGDLSVDNKKIVKEHLN 

NHA5: 
Blast query: 
MDNQGYVQNEKVDRRLSLAGMELPGPVSRRNSRAPPPYVPEVPKYRADRRLSLSGMEIPGPVSRRNSRAPPPFVPEVPVNRGERRLSLSGMEIPNVVSRRNSKYQQVVHPHPVVEDKEEVSEYSPPAYPGDKKQPGKVKKSYKRVKQVLQNNKITSNFFPPKGDVAINITLMITVVIIFLCARTVLGPYSALGGTIFAVFILIFFALVAGQIVLQAAALLSKMVGFDIRIPQLLGMMAVGIFCKNVPYNAHEFNSPECLNRSLAHGNLYKELHGNDSHLIDHEGLNLHSDDPNAHGVMMDVHASLKEGHSAIVDHLEKTTDNPKFSTTAKIFHAKAKEFKSPSNASQALKSHGEGFKPIPDSETLHHRARRSGGHDEPAVYRDPCVKRFIGGDVDPTVKGILRSACLTFILLMAGLELDPPQLWRLKWIVLRTTFIPCIVEAFAAALFCYLILGFPFLPGLCFGFVLCGVSPAVIIPGLVNLSQRGYGVKKGIPTLVIATCSADDLVAIGGFGIAAGITFNPDASISDLASHGPLEVLLGIAFGIFWGYICQWFPSKQYENYVFFRWVLLTAGGAFALFGAHMIHYDGAGGLACVIMAFVASIQWRREGWGDHNPVTDIYNKVWIILSPVIFSLIGTNINAEKMDGATVGMGVAVLVCCFLTRGFFTYWSAVCGGLDTKEKIFLAISWLPKATVQAALGPAFLEKAIAANLPEYVPIGETILTMAVISIAISAPIGAILILALGPVLLPNDFEGDEDEDEEAGELDVIKENMKEITKEAHH

NHA6: 
Blast query: 
MDNRGYNVTNEKNDRRLSLSGMEMPGLYSRRGSKAPPPFVPEVSEDRGDRRLSLSGMELPIPYSRRGSKYQPVQEPVQETFELPEDPPPAYQGNKKAPGKVKKSYKRVKQALQSNRITSNFFPPKGEVATNITLMIAVVIIFLCARTVLGSYSALGGTIFAVFILVFFALVAGQIVLQLAAIISKLAGFDIRIPQLLGMMAVGIFCKNVPYNSHEFNSPECLNRSLTHSDLHEDVHGNESHLILHGDTDLHHLNVHGKIMDIHASFNEGHAKIVEHLKNSTFSSTAEINHNDHPESIGSTNNTHEDKLDTHTNGEGFKPIPDSENHHHRARRSGGHDEPVVYRDPCVKRFIGNDVDPTVKTILRSACLTCILLMAGLELDPPQLWRLKWIVLRTTFIPCIVEAFAAALFCYLILGFPFLPGLCFGFVLCGVSPAVIIPGLVNLSQRGYGVKKGIPTLVIATCSADDLVAIGGFGIAAGITFNPDASISDLASHGPLEVLLGIAFGIFWGYICQWFPSKQNANYVFFRWVILTAGGLFALFGAHMIHYDGAGGLACVIMAFVASIQWRREGWGDHNPVTDIYNKVWIILSPVIFSLIGTNINAEKMDGATVGLGVAVLFCCFITRGFFTFWSAVCGGLDTKEKIFLAVAWLPKATVQAALGPAFLEKAISAGLTDFIPMGETILTMAVISIAISAPIGAILILALGPVLLPNDFEDKEDDPEDNTDREGIIENMKEVVHH

NHA7:
Blast query: 
MHGTTRRNSRYQQIPPATVHEDEVPQYPPPAYPGKIKNPGRIKKAYDSFKQTLQTNRITSHFFPPKGEVATNITLMIAVVIIFFCARAVLGKYSALGGTIFAVFILVFFALVAGQIVLQFAALISKLAGFDIRIPQLLGMMAVGIFCKNVPYNSHEFNSPECLNRSLTQGTIHEAFHGNISALTGHDDPNAHGVVMNVHDALKDEHERIVEHLEKTTVNPKFSSTARIFHAKVQDFKSSTSNDSQSSHSEHLDGEGIKSMPESDDHHHRARRSGGHDEPAVYRDPCVKRFIGGDVDPTVKGILRSTCLTVILLMAGLELDPPQLWRLKWIVLRTTFIPCIVEAFAAALFCYLILGFPFLPGLCFGFVLCGVSPAVIIPGLVNLSQRGYGVKKGIPTLVIATCSADDLVAIGGFGIAAGITFNPDASISDLASHGPLEVLLGIAFGIFWGYICQWFPSKQNANHVFFRWVLLTAGGLFALFGAHMVHYDGAGGLACVIMAFVASIQWRREGWGDHNPVTDIYNKVWIILSPVIFSLIGTNINAEKMDGATVGLGVAVLFCCFITRSFFTFWSAVCGGLETKEKLFLSISWLPKATVQAALGMGETILTLAVLSIAISAPIGAILILALGPVLLPNDFEGEDGEAGLKEVAKEHMTEVKHH

NHA8:
Blast query: 
MLVVGIVLKNVPYIDVGRGLDPSWSAALRSTALAVILLRAGLGLDPRALKQLSAMVFRLAFFPCLVEATVVAISSHLLLGFPWLWGFMLGFILAAVSPAVVVPCLLSLQERGFGVEKGIPTLVIAAASVDDVLAISVFTILLGVTFNTNQDNLYQLILQGPLEAIVGVLGGFIWGVLVIFLPPSPHPNVLLRVVLLFGGSLFALFGSAMAGFPGAGALGVLVLAFVAGLGWRRQGWKEDNPVSQTLAQMWIIFQPLLFGLIGTEIQVDKLDPETVGLGIGVLVCGLSARLVLSYISVLGGDVNHRERMFIALAWLPKATVQAAIGPLALDLATQALRKAGMDGENLPELNEQLELAEKVLTLAVLVILITAPIGAVAIMASGPRLLTKMNKPLPYDIKEEGEEMSEMIS

### Curating Assemblies 
Because not assemblies have good quality, I'm running my data-collection.py, which 
curates sequences according to protein size, coverage, scaffold n50 scores, etc. 

Command: python3 data-collection.py

Outputs were stored inside data/ folder as such: 
2023-02-19-NHA1-HitTable.csv	2023-02-20-NHA5-HitTable.csv
2023-02-20-NHA1-filtered.csv	2023-02-20-NHA5-filtered.csv
2023-02-20-NHA1-log.txt		2023-02-20-NHA5-log.txt
2023-02-20-NHA1-trashed.csv	2023-02-20-NHA5-trashed.csv
2023-02-20-NHA2-HitTable.csv	2023-02-20-NHA6-HitTable.csv
2023-02-20-NHA2-filtered.csv	2023-02-20-NHA6-filtered.csv
2023-02-20-NHA2-log.txt		2023-02-20-NHA6-log.txt
2023-02-20-NHA2-trashed.csv	2023-02-20-NHA6-trashed.csv
2023-02-20-NHA3-HitTable.csv	2023-02-20-NHA7-HitTable.csv
2023-02-20-NHA3-filtered.csv	2023-02-20-NHA7-filtered.csv
2023-02-20-NHA3-log.txt		2023-02-20-NHA7-log.txt
2023-02-20-NHA3-trashed.csv	2023-02-20-NHA7-trashed.csv
2023-02-20-NHA4-HitTable.csv	2023-02-21-all_orthologs.fa
2023-02-20-NHA4-filtered.csv	curated-orthologs.xlsx
2023-02-20-NHA4-log.txt		old-runs
2023-02-20-NHA4-trashed.csv

old-runs contains my first attempt of the script with NHA7 and will not be considered for
final analysis. curated-orthologs.xlsx contains a manual curation for quality control of
my script. 

## Compiling Orthologs 
I've written a quick script: fasta-compiler.R, to remove all duplicates and write a new 
fasta file for all ortholog sequences. 

Command: Rscript fasta-compiler.R 
Output: 2023-02-21-sequence_orthologs.fa

## Alignment: ClustalW
Command: clustalw2 -ALIGN -INFILE=2023-02-21-sequence_orthologs.fasta -OUTFILE=2023-02-21-alignment_orthologs.fasta -OUTPUT=FASTA
Output: 2023-02-21-alignment_orthologs.fasta

Message: 
 CLUSTAL 2.1 Multiple Sequence Alignments


Sequence format is Pearson
Sequence 1: TRY75264.1     555 aa
Sequence 2: KAF2354193.1  1026 aa
Sequence 3: KAA0203922.1   343 aa
Sequence 4: WAQ97368.1     562 aa
Sequence 5: KAG1663790.1   539 aa
Sequence 6: KAI0224210.1   586 aa
Sequence 7: CAG2239237.1   450 aa
Sequence 8: KAG5713906.1   510 aa
Sequence 9: CAC5409661.1   531 aa
Sequence 10: VDI61892.1     555 aa
Sequence 11: VDI61893.1     532 aa
Sequence 12: KAG1694105.1   990 aa
Sequence 13: KAI8745152.1   534 aa
Sequence 14: KAG1694104.1   997 aa
Sequence 15: ROT75079.1     487 aa
Sequence 16: KAG1663789.1   556 aa
Sequence 17: PVD38526.1     624 aa
Sequence 18: RXG52054.1     557 aa
Sequence 19: KAI5704272.1   552 aa
Sequence 20: KAI5736882.1   552 aa
Sequence 21: KAI5704273.1   519 aa
Sequence 22: KAG1694103.1  1007 aa
Sequence 23: GFN98310.1     542 aa
Sequence 24: KAH9519772.1   431 aa
Sequence 25: CAG5128447.1   565 aa
Sequence 26: CAD5122438.1   557 aa
Sequence 27: CAH1794646.1   662 aa
Sequence 28: ODN02785.1     531 aa
Sequence 29: CAD7247776.1   539 aa
Sequence 30: GFR63527.1     547 aa
Sequence 31: CAG5128446.1   527 aa
Sequence 32: CAD7578322.1   381 aa
Sequence 33: CAH1388393.1   555 aa
Sequence 34: CAD7456214.1   464 aa
Sequence 35: CAE1272954.1   550 aa
Sequence 36: GFN81860.1     618 aa
Start of Pairwise alignments
Aligning...

Sequences (1:2) Aligned. Score:  47
Sequences (1:3) Aligned. Score:  56
Sequences (1:4) Aligned. Score:  42
Sequences (1:5) Aligned. Score:  42
Sequences (1:6) Aligned. Score:  43
Sequences (1:7) Aligned. Score:  45
Sequences (1:8) Aligned. Score:  37
Sequences (1:9) Aligned. Score:  43
Sequences (1:10) Aligned. Score:  41
Sequences (1:11) Aligned. Score:  43
Sequences (1:12) Aligned. Score:  42
Sequences (1:13) Aligned. Score:  44
Sequences (1:14) Aligned. Score:  42
Sequences (1:15) Aligned. Score:  45
Sequences (1:16) Aligned. Score:  41
Sequences (1:17) Aligned. Score:  40
Sequences (1:18) Aligned. Score:  40
Sequences (1:19) Aligned. Score:  38
Sequences (1:20) Aligned. Score:  38
Sequences (1:21) Aligned. Score:  40
Sequences (1:22) Aligned. Score:  42
Sequences (1:23) Aligned. Score:  43
Sequences (1:24) Aligned. Score:  49
Sequences (1:25) Aligned. Score:  41
Sequences (1:26) Aligned. Score:  44
Sequences (1:27) Aligned. Score:  39
Sequences (1:28) Aligned. Score:  41
Sequences (1:29) Aligned. Score:  42
Sequences (1:30) Aligned. Score:  42
Sequences (1:31) Aligned. Score:  40
Sequences (1:32) Aligned. Score:  45
Sequences (1:33) Aligned. Score:  36
Sequences (1:34) Aligned. Score:  42
Sequences (1:35) Aligned. Score:  41
Sequences (1:36) Aligned. Score:  39
Sequences (2:3) Aligned. Score:  84
Sequences (2:4) Aligned. Score:  43
Sequences (2:5) Aligned. Score:  46
Sequences (2:6) Aligned. Score:  42
Sequences (2:7) Aligned. Score:  49
Sequences (2:8) Aligned. Score:  37
Sequences (2:9) Aligned. Score:  49
Sequences (2:10) Aligned. Score:  47
Sequences (2:11) Aligned. Score:  48
Sequences (2:12) Aligned. Score:  26
Sequences (2:13) Aligned. Score:  44
Sequences (2:14) Aligned. Score:  26
Sequences (2:15) Aligned. Score:  57
Sequences (2:16) Aligned. Score:  44
Sequences (2:17) Aligned. Score:  38
Sequences (2:18) Aligned. Score:  50
Sequences (2:19) Aligned. Score:  38
Sequences (2:20) Aligned. Score:  38
Sequences (2:21) Aligned. Score:  39
Sequences (2:22) Aligned. Score:  25
Sequences (2:23) Aligned. Score:  46
Sequences (2:24) Aligned. Score:  49
Sequences (2:25) Aligned. Score:  41
Sequences (2:26) Aligned. Score:  43
Sequences (2:27) Aligned. Score:  35
Sequences (2:28) Aligned. Score:  40
Sequences (2:29) Aligned. Score:  42
Sequences (2:30) Aligned. Score:  44
Sequences (2:31) Aligned. Score:  43
Sequences (2:32) Aligned. Score:  47
Sequences (2:33) Aligned. Score:  41
Sequences (2:34) Aligned. Score:  43
Sequences (2:35) Aligned. Score:  44
Sequences (2:36) Aligned. Score:  36
Sequences (3:4) Aligned. Score:  50
Sequences (3:5) Aligned. Score:  52
Sequences (3:6) Aligned. Score:  50
Sequences (3:7) Aligned. Score:  51
Sequences (3:8) Aligned. Score:  46
Sequences (3:9) Aligned. Score:  51
Sequences (3:10) Aligned. Score:  51
Sequences (3:11) Aligned. Score:  51
Sequences (3:12) Aligned. Score:  53
Sequences (3:13) Aligned. Score:  49
Sequences (3:14) Aligned. Score:  53
Sequences (3:15) Aligned. Score:  54
Sequences (3:16) Aligned. Score:  51
Sequences (3:17) Aligned. Score:  48
Sequences (3:18) Aligned. Score:  61
Sequences (3:19) Aligned. Score:  44
Sequences (3:20) Aligned. Score:  44
Sequences (3:21) Aligned. Score:  44
Sequences (3:22) Aligned. Score:  52
Sequences (3:23) Aligned. Score:  50
Sequences (3:24) Aligned. Score:  48
Sequences (3:25) Aligned. Score:  47
Sequences (3:26) Aligned. Score:  52
Sequences (3:27) Aligned. Score:  48
Sequences (3:28) Aligned. Score:  46
Sequences (3:29) Aligned. Score:  48
Sequences (3:30) Aligned. Score:  49
Sequences (3:31) Aligned. Score:  46
Sequences (3:32) Aligned. Score:  43
Sequences (3:33) Aligned. Score:  48
Sequences (3:34) Aligned. Score:  44
Sequences (3:35) Aligned. Score:  51
Sequences (3:36) Aligned. Score:  48
Sequences (4:5) Aligned. Score:  44
Sequences (4:6) Aligned. Score:  46
Sequences (4:7) Aligned. Score:  62
Sequences (4:8) Aligned. Score:  45
Sequences (4:9) Aligned. Score:  61
Sequences (4:10) Aligned. Score:  57
Sequences (4:11) Aligned. Score:  60
Sequences (4:12) Aligned. Score:  42
Sequences (4:13) Aligned. Score:  50
Sequences (4:14) Aligned. Score:  42
Sequences (4:15) Aligned. Score:  45
Sequences (4:16) Aligned. Score:  42
Sequences (4:17) Aligned. Score:  50
Sequences (4:18) Aligned. Score:  40
Sequences (4:19) Aligned. Score:  37
Sequences (4:20) Aligned. Score:  37
Sequences (4:21) Aligned. Score:  39
Sequences (4:22) Aligned. Score:  42
Sequences (4:23) Aligned. Score:  51
Sequences (4:24) Aligned. Score:  56
Sequences (4:25) Aligned. Score:  50
Sequences (4:26) Aligned. Score:  48
Sequences (4:27) Aligned. Score:  43
Sequences (4:28) Aligned. Score:  41
Sequences (4:29) Aligned. Score:  40
Sequences (4:30) Aligned. Score:  51
Sequences (4:31) Aligned. Score:  49
Sequences (4:32) Aligned. Score:  45
Sequences (4:33) Aligned. Score:  36
Sequences (4:34) Aligned. Score:  43
Sequences (4:35) Aligned. Score:  50
Sequences (4:36) Aligned. Score:  47
Sequences (5:6) Aligned. Score:  48
Sequences (5:7) Aligned. Score:  51
Sequences (5:8) Aligned. Score:  39
Sequences (5:9) Aligned. Score:  45
Sequences (5:10) Aligned. Score:  46
Sequences (5:11) Aligned. Score:  47
Sequences (5:12) Aligned. Score:  97
Sequences (5:13) Aligned. Score:  44
Sequences (5:14) Aligned. Score:  97
Sequences (5:15) Aligned. Score:  48
Sequences (5:16) Aligned. Score:  99
Sequences (5:17) Aligned. Score:  41
Sequences (5:18) Aligned. Score:  42
Sequences (5:19) Aligned. Score:  36
Sequences (5:20) Aligned. Score:  36
Sequences (5:21) Aligned. Score:  38
Sequences (5:22) Aligned. Score:  97
Sequences (5:23) Aligned. Score:  44
Sequences (5:24) Aligned. Score:  53
Sequences (5:25) Aligned. Score:  44
Sequences (5:26) Aligned. Score:  45
Sequences (5:27) Aligned. Score:  44
Sequences (5:28) Aligned. Score:  42
Sequences (5:29) Aligned. Score:  39
Sequences (5:30) Aligned. Score:  41
Sequences (5:31) Aligned. Score:  39
Sequences (5:32) Aligned. Score:  46
Sequences (5:33) Aligned. Score:  39
Sequences (5:34) Aligned. Score:  42
Sequences (5:35) Aligned. Score:  43
Sequences (5:36) Aligned. Score:  41
Sequences (6:7) Aligned. Score:  52
Sequences (6:8) Aligned. Score:  45
Sequences (6:9) Aligned. Score:  50
Sequences (6:10) Aligned. Score:  49
Sequences (6:11) Aligned. Score:  51
Sequences (6:12) Aligned. Score:  45
Sequences (6:13) Aligned. Score:  49
Sequences (6:14) Aligned. Score:  45
Sequences (6:15) Aligned. Score:  50
Sequences (6:16) Aligned. Score:  46
Sequences (6:17) Aligned. Score:  46
Sequences (6:18) Aligned. Score:  42
Sequences (6:19) Aligned. Score:  37
Sequences (6:20) Aligned. Score:  37
Sequences (6:21) Aligned. Score:  40
Sequences (6:22) Aligned. Score:  45
Sequences (6:23) Aligned. Score:  49
Sequences (6:24) Aligned. Score:  54
Sequences (6:25) Aligned. Score:  47
Sequences (6:26) Aligned. Score:  49
Sequences (6:27) Aligned. Score:  44
Sequences (6:28) Aligned. Score:  41
Sequences (6:29) Aligned. Score:  38
Sequences (6:30) Aligned. Score:  46
Sequences (6:31) Aligned. Score:  44
Sequences (6:32) Aligned. Score:  47
Sequences (6:33) Aligned. Score:  39
Sequences (6:34) Aligned. Score:  42
Sequences (6:35) Aligned. Score:  47
Sequences (6:36) Aligned. Score:  41
Sequences (7:8) Aligned. Score:  52
Sequences (7:9) Aligned. Score:  93
Sequences (7:10) Aligned. Score:  99
Sequences (7:11) Aligned. Score:  99
Sequences (7:12) Aligned. Score:  52
Sequences (7:13) Aligned. Score:  51
Sequences (7:14) Aligned. Score:  52
Sequences (7:15) Aligned. Score:  45
Sequences (7:16) Aligned. Score:  51
Sequences (7:17) Aligned. Score:  54
Sequences (7:18) Aligned. Score:  46
Sequences (7:19) Aligned. Score:  41
Sequences (7:20) Aligned. Score:  41
Sequences (7:21) Aligned. Score:  41
Sequences (7:22) Aligned. Score:  52
Sequences (7:23) Aligned. Score:  54
Sequences (7:24) Aligned. Score:  54
Sequences (7:25) Aligned. Score:  53
Sequences (7:26) Aligned. Score:  52
Sequences (7:27) Aligned. Score:  52
Sequences (7:28) Aligned. Score:  45
Sequences (7:29) Aligned. Score:  43
Sequences (7:30) Aligned. Score:  53
Sequences (7:31) Aligned. Score:  50
Sequences (7:32) Aligned. Score:  46
Sequences (7:33) Aligned. Score:  43
Sequences (7:34) Aligned. Score:  42
Sequences (7:35) Aligned. Score:  55
Sequences (7:36) Aligned. Score:  52
Sequences (8:9) Aligned. Score:  45
Sequences (8:10) Aligned. Score:  46
Sequences (8:11) Aligned. Score:  46
Sequences (8:12) Aligned. Score:  40
Sequences (8:13) Aligned. Score:  49
Sequences (8:14) Aligned. Score:  40
Sequences (8:15) Aligned. Score:  39
Sequences (8:16) Aligned. Score:  39
Sequences (8:17) Aligned. Score:  49
Sequences (8:18) Aligned. Score:  36
Sequences (8:19) Aligned. Score:  33
Sequences (8:20) Aligned. Score:  33
Sequences (8:21) Aligned. Score:  33
Sequences (8:22) Aligned. Score:  40
Sequences (8:23) Aligned. Score:  50
Sequences (8:24) Aligned. Score:  56
Sequences (8:25) Aligned. Score:  48
Sequences (8:26) Aligned. Score:  39
Sequences (8:27) Aligned. Score:  41
Sequences (8:28) Aligned. Score:  38
Sequences (8:29) Aligned. Score:  34
Sequences (8:30) Aligned. Score:  50
Sequences (8:31) Aligned. Score:  46
Sequences (8:32) Aligned. Score:  42
Sequences (8:33) Aligned. Score:  34
Sequences (8:34) Aligned. Score:  36
Sequences (8:35) Aligned. Score:  43
Sequences (8:36) Aligned. Score:  44
Sequences (9:10) Aligned. Score:  93
Sequences (9:11) Aligned. Score:  93
Sequences (9:12) Aligned. Score:  47
Sequences (9:13) Aligned. Score:  48
Sequences (9:14) Aligned. Score:  47
Sequences (9:15) Aligned. Score:  47
Sequences (9:16) Aligned. Score:  44
Sequences (9:17) Aligned. Score:  51
Sequences (9:18) Aligned. Score:  42
Sequences (9:19) Aligned. Score:  37
Sequences (9:20) Aligned. Score:  37
Sequences (9:21) Aligned. Score:  38
Sequences (9:22) Aligned. Score:  47
Sequences (9:23) Aligned. Score:  52
Sequences (9:24) Aligned. Score:  55
Sequences (9:25) Aligned. Score:  53
Sequences (9:26) Aligned. Score:  51
Sequences (9:27) Aligned. Score:  46
Sequences (9:28) Aligned. Score:  41
Sequences (9:29) Aligned. Score:  40
Sequences (9:30) Aligned. Score:  51
Sequences (9:31) Aligned. Score:  48
Sequences (9:32) Aligned. Score:  48
Sequences (9:33) Aligned. Score:  39
Sequences (9:34) Aligned. Score:  44
Sequences (9:35) Aligned. Score:  54
Sequences (9:36) Aligned. Score:  48
Sequences (10:11) Aligned. Score:  100
Sequences (10:12) Aligned. Score:  45
Sequences (10:13) Aligned. Score:  47
Sequences (10:14) Aligned. Score:  45
Sequences (10:15) Aligned. Score:  46
Sequences (10:16) Aligned. Score:  44
Sequences (10:17) Aligned. Score:  50
Sequences (10:18) Aligned. Score:  40
Sequences (10:19) Aligned. Score:  35
Sequences (10:20) Aligned. Score:  36
Sequences (10:21) Aligned. Score:  38
Sequences (10:22) Aligned. Score:  45
Sequences (10:23) Aligned. Score:  51
Sequences (10:24) Aligned. Score:  56
Sequences (10:25) Aligned. Score:  49
Sequences (10:26) Aligned. Score:  49
Sequences (10:27) Aligned. Score:  45
Sequences (10:28) Aligned. Score:  40
Sequences (10:29) Aligned. Score:  39
Sequences (10:30) Aligned. Score:  49
Sequences (10:31) Aligned. Score:  48
Sequences (10:32) Aligned. Score:  46
Sequences (10:33) Aligned. Score:  36
Sequences (10:34) Aligned. Score:  43
Sequences (10:35) Aligned. Score:  52
Sequences (10:36) Aligned. Score:  47
Sequences (11:12) Aligned. Score:  48
Sequences (11:13) Aligned. Score:  47
Sequences (11:14) Aligned. Score:  48
Sequences (11:15) Aligned. Score:  46
Sequences (11:16) Aligned. Score:  47
Sequences (11:17) Aligned. Score:  52
Sequences (11:18) Aligned. Score:  42
Sequences (11:19) Aligned. Score:  37
Sequences (11:20) Aligned. Score:  37
Sequences (11:21) Aligned. Score:  38
Sequences (11:22) Aligned. Score:  48
Sequences (11:23) Aligned. Score:  52
Sequences (11:24) Aligned. Score:  56
Sequences (11:25) Aligned. Score:  51
Sequences (11:26) Aligned. Score:  50
Sequences (11:27) Aligned. Score:  47
Sequences (11:28) Aligned. Score:  40
Sequences (11:29) Aligned. Score:  40
Sequences (11:30) Aligned. Score:  50
Sequences (11:31) Aligned. Score:  48
Sequences (11:32) Aligned. Score:  46
Sequences (11:33) Aligned. Score:  38
Sequences (11:34) Aligned. Score:  43
Sequences (11:35) Aligned. Score:  54
Sequences (11:36) Aligned. Score:  49
Sequences (12:13) Aligned. Score:  45
Sequences (12:14) Aligned. Score:  100
Sequences (12:15) Aligned. Score:  50
Sequences (12:16) Aligned. Score:  94
Sequences (12:17) Aligned. Score:  37
Sequences (12:18) Aligned. Score:  45
Sequences (12:19) Aligned. Score:  38
Sequences (12:20) Aligned. Score:  38
Sequences (12:21) Aligned. Score:  37
Sequences (12:22) Aligned. Score:  99
Sequences (12:23) Aligned. Score:  44
Sequences (12:24) Aligned. Score:  53
Sequences (12:25) Aligned. Score:  44
Sequences (12:26) Aligned. Score:  46
Sequences (12:27) Aligned. Score:  37
Sequences (12:28) Aligned. Score:  42
Sequences (12:29) Aligned. Score:  39
Sequences (12:30) Aligned. Score:  42
Sequences (12:31) Aligned. Score:  40
Sequences (12:32) Aligned. Score:  46
Sequences (12:33) Aligned. Score:  38
Sequences (12:34) Aligned. Score:  42
Sequences (12:35) Aligned. Score:  42
Sequences (12:36) Aligned. Score:  36
Sequences (13:14) Aligned. Score:  45
Sequences (13:15) Aligned. Score:  44
Sequences (13:16) Aligned. Score:  43
Sequences (13:17) Aligned. Score:  55
Sequences (13:18) Aligned. Score:  37
Sequences (13:19) Aligned. Score:  38
Sequences (13:20) Aligned. Score:  38
Sequences (13:21) Aligned. Score:  39
Sequences (13:22) Aligned. Score:  45
Sequences (13:23) Aligned. Score:  61
Sequences (13:24) Aligned. Score:  80
Sequences (13:25) Aligned. Score:  61
Sequences (13:26) Aligned. Score:  45
Sequences (13:27) Aligned. Score:  43
Sequences (13:28) Aligned. Score:  41
Sequences (13:29) Aligned. Score:  39
Sequences (13:30) Aligned. Score:  58
Sequences (13:31) Aligned. Score:  50
Sequences (13:32) Aligned. Score:  42
Sequences (13:33) Aligned. Score:  40
Sequences (13:34) Aligned. Score:  38
Sequences (13:35) Aligned. Score:  48
Sequences (13:36) Aligned. Score:  51
Sequences (14:15) Aligned. Score:  50
Sequences (14:16) Aligned. Score:  95
Sequences (14:17) Aligned. Score:  37
Sequences (14:18) Aligned. Score:  45
Sequences (14:19) Aligned. Score:  38
Sequences (14:20) Aligned. Score:  38
Sequences (14:21) Aligned. Score:  37
Sequences (14:22) Aligned. Score:  99
Sequences (14:23) Aligned. Score:  44
Sequences (14:24) Aligned. Score:  53
Sequences (14:25) Aligned. Score:  44
Sequences (14:26) Aligned. Score:  46
Sequences (14:27) Aligned. Score:  37
Sequences (14:28) Aligned. Score:  42
Sequences (14:29) Aligned. Score:  39
Sequences (14:30) Aligned. Score:  42
Sequences (14:31) Aligned. Score:  40
Sequences (14:32) Aligned. Score:  46
Sequences (14:33) Aligned. Score:  37
Sequences (14:34) Aligned. Score:  42
Sequences (14:35) Aligned. Score:  42
Sequences (14:36) Aligned. Score:  36
Sequences (15:16) Aligned. Score:  48
Sequences (15:17) Aligned. Score:  44
Sequences (15:18) Aligned. Score:  49
Sequences (15:19) Aligned. Score:  40
Sequences (15:20) Aligned. Score:  40
Sequences (15:21) Aligned. Score:  40
Sequences (15:22) Aligned. Score:  50
Sequences (15:23) Aligned. Score:  45
Sequences (15:24) Aligned. Score:  48
Sequences (15:25) Aligned. Score:  42
Sequences (15:26) Aligned. Score:  44
Sequences (15:27) Aligned. Score:  45
Sequences (15:28) Aligned. Score:  42
Sequences (15:29) Aligned. Score:  41
Sequences (15:30) Aligned. Score:  44
Sequences (15:31) Aligned. Score:  41
Sequences (15:32) Aligned. Score:  48
Sequences (15:33) Aligned. Score:  40
Sequences (15:34) Aligned. Score:  41
Sequences (15:35) Aligned. Score:  44
Sequences (15:36) Aligned. Score:  41
Sequences (16:17) Aligned. Score:  40
Sequences (16:18) Aligned. Score:  41
Sequences (16:19) Aligned. Score:  35
Sequences (16:20) Aligned. Score:  35
Sequences (16:21) Aligned. Score:  37
Sequences (16:22) Aligned. Score:  97
Sequences (16:23) Aligned. Score:  44
Sequences (16:24) Aligned. Score:  53
Sequences (16:25) Aligned. Score:  42
Sequences (16:26) Aligned. Score:  44
Sequences (16:27) Aligned. Score:  43
Sequences (16:28) Aligned. Score:  42
Sequences (16:29) Aligned. Score:  38
Sequences (16:30) Aligned. Score:  40
Sequences (16:31) Aligned. Score:  39
Sequences (16:32) Aligned. Score:  46
Sequences (16:33) Aligned. Score:  37
Sequences (16:34) Aligned. Score:  41
Sequences (16:35) Aligned. Score:  43
Sequences (16:36) Aligned. Score:  40
Sequences (17:18) Aligned. Score:  37
Sequences (17:19) Aligned. Score:  36
Sequences (17:20) Aligned. Score:  36
Sequences (17:21) Aligned. Score:  39
Sequences (17:22) Aligned. Score:  37
Sequences (17:23) Aligned. Score:  59
Sequences (17:24) Aligned. Score:  60
Sequences (17:25) Aligned. Score:  51
Sequences (17:26) Aligned. Score:  46
Sequences (17:27) Aligned. Score:  38
Sequences (17:28) Aligned. Score:  41
Sequences (17:29) Aligned. Score:  39
Sequences (17:30) Aligned. Score:  55
Sequences (17:31) Aligned. Score:  54
Sequences (17:32) Aligned. Score:  46
Sequences (17:33) Aligned. Score:  37
Sequences (17:34) Aligned. Score:  41
Sequences (17:35) Aligned. Score:  47
Sequences (17:36) Aligned. Score:  46
Sequences (18:19) Aligned. Score:  35
Sequences (18:20) Aligned. Score:  35
Sequences (18:21) Aligned. Score:  36
Sequences (18:22) Aligned. Score:  45
Sequences (18:23) Aligned. Score:  38
Sequences (18:24) Aligned. Score:  45
Sequences (18:25) Aligned. Score:  36
Sequences (18:26) Aligned. Score:  42
Sequences (18:27) Aligned. Score:  38
Sequences (18:28) Aligned. Score:  39
Sequences (18:29) Aligned. Score:  37
Sequences (18:30) Aligned. Score:  39
Sequences (18:31) Aligned. Score:  38
Sequences (18:32) Aligned. Score:  44
Sequences (18:33) Aligned. Score:  35
Sequences (18:34) Aligned. Score:  41
Sequences (18:35) Aligned. Score:  39
Sequences (18:36) Aligned. Score:  37
Sequences (19:20) Aligned. Score:  99
Sequences (19:21) Aligned. Score:  95
Sequences (19:22) Aligned. Score:  38
Sequences (19:23) Aligned. Score:  38
Sequences (19:24) Aligned. Score:  44
Sequences (19:25) Aligned. Score:  34
Sequences (19:26) Aligned. Score:  37
Sequences (19:27) Aligned. Score:  37
Sequences (19:28) Aligned. Score:  36
Sequences (19:29) Aligned. Score:  37
Sequences (19:30) Aligned. Score:  36
Sequences (19:31) Aligned. Score:  36
Sequences (19:32) Aligned. Score:  46
Sequences (19:33) Aligned. Score:  49
Sequences (19:34) Aligned. Score:  43
Sequences (19:35) Aligned. Score:  35
Sequences (19:36) Aligned. Score:  36
Sequences (20:21) Aligned. Score:  95
Sequences (20:22) Aligned. Score:  38
Sequences (20:23) Aligned. Score:  38
Sequences (20:24) Aligned. Score:  44
Sequences (20:25) Aligned. Score:  34
Sequences (20:26) Aligned. Score:  37
Sequences (20:27) Aligned. Score:  37
Sequences (20:28) Aligned. Score:  36
Sequences (20:29) Aligned. Score:  37
Sequences (20:30) Aligned. Score:  36
Sequences (20:31) Aligned. Score:  36
Sequences (20:32) Aligned. Score:  46
Sequences (20:33) Aligned. Score:  49
Sequences (20:34) Aligned. Score:  43
Sequences (20:35) Aligned. Score:  35
Sequences (20:36) Aligned. Score:  36
Sequences (21:22) Aligned. Score:  37
Sequences (21:23) Aligned. Score:  40
Sequences (21:24) Aligned. Score:  44
Sequences (21:25) Aligned. Score:  36
Sequences (21:26) Aligned. Score:  39
Sequences (21:27) Aligned. Score:  40
Sequences (21:28) Aligned. Score:  37
Sequences (21:29) Aligned. Score:  38
Sequences (21:30) Aligned. Score:  38
Sequences (21:31) Aligned. Score:  36
Sequences (21:32) Aligned. Score:  46
Sequences (21:33) Aligned. Score:  51
Sequences (21:34) Aligned. Score:  43
Sequences (21:35) Aligned. Score:  38
Sequences (21:36) Aligned. Score:  38
Sequences (22:23) Aligned. Score:  44
Sequences (22:24) Aligned. Score:  53
Sequences (22:25) Aligned. Score:  43
Sequences (22:26) Aligned. Score:  46
Sequences (22:27) Aligned. Score:  37
Sequences (22:28) Aligned. Score:  42
Sequences (22:29) Aligned. Score:  39
Sequences (22:30) Aligned. Score:  42
Sequences (22:31) Aligned. Score:  40
Sequences (22:32) Aligned. Score:  46
Sequences (22:33) Aligned. Score:  37
Sequences (22:34) Aligned. Score:  41
Sequences (22:35) Aligned. Score:  42
Sequences (22:36) Aligned. Score:  36
Sequences (23:24) Aligned. Score:  66
Sequences (23:25) Aligned. Score:  65
Sequences (23:26) Aligned. Score:  47
Sequences (23:27) Aligned. Score:  44
Sequences (23:28) Aligned. Score:  42
Sequences (23:29) Aligned. Score:  39
Sequences (23:30) Aligned. Score:  74
Sequences (23:31) Aligned. Score:  53
Sequences (23:32) Aligned. Score:  46
Sequences (23:33) Aligned. Score:  37
Sequences (23:34) Aligned. Score:  42
Sequences (23:35) Aligned. Score:  47
Sequences (23:36) Aligned. Score:  54
Sequences (24:25) Aligned. Score:  68
Sequences (24:26) Aligned. Score:  53
Sequences (24:27) Aligned. Score:  51
Sequences (24:28) Aligned. Score:  51
Sequences (24:29) Aligned. Score:  42
Sequences (24:30) Aligned. Score:  62
Sequences (24:31) Aligned. Score:  54
Sequences (24:32) Aligned. Score:  44
Sequences (24:33) Aligned. Score:  46
Sequences (24:34) Aligned. Score:  42
Sequences (24:35) Aligned. Score:  56
Sequences (24:36) Aligned. Score:  55
Sequences (25:26) Aligned. Score:  46
Sequences (25:27) Aligned. Score:  41
Sequences (25:28) Aligned. Score:  38
Sequences (25:29) Aligned. Score:  38
Sequences (25:30) Aligned. Score:  62
Sequences (25:31) Aligned. Score:  52
Sequences (25:32) Aligned. Score:  43
Sequences (25:33) Aligned. Score:  35
Sequences (25:34) Aligned. Score:  39
Sequences (25:35) Aligned. Score:  48
Sequences (25:36) Aligned. Score:  49
Sequences (26:27) Aligned. Score:  43
Sequences (26:28) Aligned. Score:  41
Sequences (26:29) Aligned. Score:  39
Sequences (26:30) Aligned. Score:  45
Sequences (26:31) Aligned. Score:  45
Sequences (26:32) Aligned. Score:  45
Sequences (26:33) Aligned. Score:  37
Sequences (26:34) Aligned. Score:  41
Sequences (26:35) Aligned. Score:  49
Sequences (26:36) Aligned. Score:  43
Sequences (27:28) Aligned. Score:  39
Sequences (27:29) Aligned. Score:  39
Sequences (27:30) Aligned. Score:  45
Sequences (27:31) Aligned. Score:  41
Sequences (27:32) Aligned. Score:  47
Sequences (27:33) Aligned. Score:  34
Sequences (27:34) Aligned. Score:  42
Sequences (27:35) Aligned. Score:  41
Sequences (27:36) Aligned. Score:  36
Sequences (28:29) Aligned. Score:  36
Sequences (28:30) Aligned. Score:  39
Sequences (28:31) Aligned. Score:  37
Sequences (28:32) Aligned. Score:  48
Sequences (28:33) Aligned. Score:  36
Sequences (28:34) Aligned. Score:  42
Sequences (28:35) Aligned. Score:  39
Sequences (28:36) Aligned. Score:  39
Sequences (29:30) Aligned. Score:  39
Sequences (29:31) Aligned. Score:  37
Sequences (29:32) Aligned. Score:  42
Sequences (29:33) Aligned. Score:  38
Sequences (29:34) Aligned. Score:  39
Sequences (29:35) Aligned. Score:  38
Sequences (29:36) Aligned. Score:  37
Sequences (30:31) Aligned. Score:  53
Sequences (30:32) Aligned. Score:  43
Sequences (30:33) Aligned. Score:  37
Sequences (30:34) Aligned. Score:  40
Sequences (30:35) Aligned. Score:  46
Sequences (30:36) Aligned. Score:  53
Sequences (31:32) Aligned. Score:  42
Sequences (31:33) Aligned. Score:  37
Sequences (31:34) Aligned. Score:  37
Sequences (31:35) Aligned. Score:  46
Sequences (31:36) Aligned. Score:  67
Sequences (32:33) Aligned. Score:  50
Sequences (32:34) Aligned. Score:  90
Sequences (32:35) Aligned. Score:  45
Sequences (32:36) Aligned. Score:  43
Sequences (33:34) Aligned. Score:  48
Sequences (33:35) Aligned. Score:  35
Sequences (33:36) Aligned. Score:  36
Sequences (34:35) Aligned. Score:  40
Sequences (34:36) Aligned. Score:  40
Sequences (35:36) Aligned. Score:  43
Guide tree file created:   [2023-02-21-sequence_orthologs.dnd]

There are 35 groups
Start of Multiple Alignment

Aligning...
Group 1: Sequences:   2      Score:11540
Group 2: Sequences:   3      Score:9621
Group 3: Sequences:   4      Score:10180
Group 4: Sequences:   5      Score:8777
Group 5: Sequences:   6      Score:8424
Group 6: Sequences:   2      Score:8460
Group 7: Sequences:   2      Score:10340
Group 8: Sequences:   3      Score:9812
Group 9: Sequences:   5      Score:8620
Group 10: Sequences:   6      Score:8920
Group 11: Sequences:   7      Score:7577
Group 12: Sequences:   2      Score:9572
Group 13: Sequences:   9      Score:8307
Group 14: Sequences:  15      Score:7556
Group 15: Sequences:  16      Score:7948
Group 16: Sequences:  17      Score:8152
Group 17: Sequences:   2      Score:6851
Group 18: Sequences:   3      Score:7865
Group 19: Sequences:   4      Score:7093
Group 20: Sequences:   2      Score:11581
Group 21: Sequences:   2      Score:21448
Group 22: Sequences:   3      Score:21451
Group 23: Sequences:   5      Score:11546
Group 24: Sequences:   9      Score:7280
Group 25: Sequences:   2      Score:7683
Group 26: Sequences:   2      Score:11910
Group 27: Sequences:   3      Score:10976
Group 28: Sequences:   4      Score:8599
Group 29: Sequences:   2      Score:7792
Group 30: Sequences:   6      Score:6743
Group 31: Sequences:   7      Score:6962
Group 32: Sequences:   9      Score:6641
Group 33: Sequences:  18      Score:5701
Group 34: Sequences:  35      Score:5678
Group 35: Sequences:  36      Score:7482
Alignment Score 807110
firstres = 1 lastres = 1232
FASTA file created!

Fasta-Alignment file created    [2023-02-21-alignment_orthologs.fasta]


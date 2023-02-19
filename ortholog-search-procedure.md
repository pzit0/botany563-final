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

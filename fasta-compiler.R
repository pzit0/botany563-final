# Patricia Zito 
# 2023-Feb-21

# importing data
library(dplyr)
library(tidyverse)

data <- read.csv("", header = TRUE)
as_tibble(data)

# get accession names and sequences 
compiled_data <- data %>% 
  mutate(fasta_name = paste(">", protein.accession, "-", species, sep = "")) %>% # add fasta head name
  select(fasta_name, protein.sequence, cds.sequence) # select columns

# write new fasta file 
out_name1 <- paste(Sys.Date(), "protein_sequence_orthologs.fasta", sep = "-")
out_name2 <- paste(Sys.Date(), "cds_sequence_orthologs.fasta", sep = "-")
size <- dim(new_fasta)[1]

# for protein sequences 
for(i in 1:size){
  seq <- paste(new_fasta$fasta_name[i], "\n", new_fasta$protein.sequence[i], "\n", "\n")
  cat(seq)
}
sink()

# for cds sequences
for(i in 1:size){
  seq <- paste(new_fasta$fasta_name[i], "\n", new_fasta$cds.sequence[i], "\n", "\n")
  cat(seq)
}
sink()
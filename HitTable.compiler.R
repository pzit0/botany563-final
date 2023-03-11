# Patricia Zito 
# 2023-March-10

# importing data
library(dplyr)
library(tidyverse)

# compiling all HitTables
compiled <- data_frame()
files <- list.files(".")
for(i in 1:length(files)){
  if(grep("HitTable.csv", files[i])){
    blast_res <- files[i] 
    data <- read_csv(blast_res, col_names = FALSE)
    compiled <- rbind(data, compiled)
  }
}

# remove protein accession duplicates
compiled <- compiled[!duplicated(compiled$X2),]
dim(compiled)

# export
out_name <- paste(Sys.Date(), "all_protein_orthologs_HitTable.csv", sep = "-")
write.csv(compiled, file = out_name)


'''
Patricia Zito
April 6, 2023
Converts Alignment Fasta file to Nexus file 
'''
import Bio
from Bio import SeqIO

fasta = input("Name of the file: ")
out = input("Name of your output .nex file: ")
records = SeqIO.parse(fasta, "fasta")
count = SeqIO.write(records, out, "nexus")
print("Converted %i records" % count)
#! /usr/bin/env python

###We will create an alignmet with the tra-sequences in fasta format
##Directory must be Determination_of_Haplotypes_tra/Raw_Data
#we will create an multiple sequence alignment (MSA) in clustalW format

#that we can redirect the output file in a new folder
import os
from Bio.Align.Applications import ClustalwCommandline

cline = ClustalwCommandline("clustalw", infile="tra_Seq.fas", outfile="tra_seq_alig.fas")
print cline
stdout, stderr = cline()

print stdout


##IMPORTANT check path: output file will be send to the directory in the command
#first give path from current directory, then to the one where it should go 
os.rename("/home/pina/Documents/Determination_of_Haplotypes_tra/Raw_Data/tra_seq_alig.fas", "/home/pina/Documents/Determination_of_Haplotypes_tra/Step1_prepSeq/tra_seq_alig1.fas")



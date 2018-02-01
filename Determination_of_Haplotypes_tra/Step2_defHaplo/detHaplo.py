#! /usr/bin/env python
## We will create a list of haplotypes, by grouping samples with an identical sequence together

# adapted from
# "https://stackoverflow.com/questions/3675895/
# best-way-to-compare-sequence-of-letters-inside-file"
import os
from itertools import groupby
from Bio       import SeqIO

# input file were converted in web and edited in jEdit, see README.md

OutFileName= 'Tra_haplo' + ".fasta"
# open the outfile to write
OutFile=open(OutFileName,'w')

# Inputfile name "output2", without any appendix
# Name the list of the sequence from inputfile
records = list(SeqIO.parse(file('Tra_Conv_sl.fasta'),'fasta'))

# define the nucleotype in the sequences as seq_letter
def seq_letter(s): return str(s.seq)
# sort in the list of the sequence(record) basing on the sequence letters
records.sort(key=seq_letter)

# pick up the identical sequence and join the,
for seq,equal in groupby(records, seq_letter):
  # ids are the ID of the sequences
  ids = ';'.join(s.id for s in equal)
  # print ">" and IDs
  print '>%s' % ids
  # print the sequences
  print seq
  # print the ">", ID and unique sequences inside the output file
  OutFile.write('>%s' % ids + "\n" + seq +"\n")
  
OutFile.close()
os.rename("/home/pina/Documents/Determination_of_Haplotypes_tra/Step2_defHaplo/detHaplo/Tra_haplo.fasta", "/home/pina/Documents/Determination_of_Haplotypes_tra/Step3_createDict/Tra_haplo1.fas")  

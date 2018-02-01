#!/usr/bin/env python

##Create dictionary of the haplotypes by reading in the created haplotype file
##input file has to be space seperated. Sequnece will be key, then haplotypename and sample ID's 

#file=open('Tra_haplo_sd.fas','r')
with open('Tra_haplo_sd.fas', 'r') as document:
    TraHap = {}
    for line in document:
        if line.strip():  # important to have no empty lines
            key, value = line.split(None,1)  # None means 'all whitespace', the default
            TraHap[key] = value.split()

##to test if it worked
print(TraHap.get('AGCGATGAGCGTGATTATGAAGCTCGCCTGTACANNGGACGTGGTGAAGTTGCTAGACGCCGCTCCATTGCCCTATGCAGAGCCCATGCCCATTCCAGTGTACTATGATAATTTAGGGANCNATGATGATGGATCCCATGA'))






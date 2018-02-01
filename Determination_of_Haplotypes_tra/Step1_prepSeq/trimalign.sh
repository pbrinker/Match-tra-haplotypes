#! /bin/bash
#** Authors **

#Salvador Capella-Gutierrez.
#  Comparative Genomics Group. Bioinformatics and Genomics Department.
#  Centre for Genomic Regulation. Barcelona, Spain.
#  e-mail: scapella _at_ crg.es

#Toni Gabaldón.
#  Comparative Genomics Group. Bioinformatics and Genomics Department.
#  Centre for Genomic Regulation. Barcelona, Spain.
#  e-mail: tgabaldon _at_ crg.es

#** Authors (until trimAl v1.1) **
 
#!!!Change to the source directory of trimAl (here: directory ~/trimAl/source)!!!
##./ becauese the trimAl source file is no yet in the /usr/bin/bas

##-in defines the infile, here the filename and path to the file is included as we have to work out of the source folder
##-out defines the outfile name, we choosed .fas as format and redirect it to the next directory of Step 2
#also created a html file, which shows which regions were cut
## Get a summary of trimal's work in an HTML file.
## -nogaps removes all positions with gaps in the alignment.

./trimal -in /home/pina/Documents/Determination_of_Haplotypes_tra/Step1_prepSeq/trimming/tra_seq_alig1.fas -out /home/pina/Documents/Determination_of_Haplotypes_tra/Step2_defHaplo/Tra_trim.fas -htmlout trimalig.html -nogaps
 

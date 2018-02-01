#Preparation of Sequences

##Making alignment


To create an alignment we used the Submodule "Module_Clustalw" of the Package "Align" from Biopython

-> As we will pipe the output file in the directory of the next step it is important to check the supplied path information in in the script and to adjust to the path which will be used


Citations: 
Larkin MA, Blackshields G, Brown NP, Chenna R, McGettigan PA, McWilliam H, Valentin F, Wallace IM, Wilm A, Lopez R, #
Thompson JD, Gibson TJ, Higgins DG. (2007). Clustal W and Clustal X version 2.0. Bioinformatics, 23, 2947-2948.

Copyright 2008-2011 by Peter Cock. 
All rights reserved. 
This code is part of the Biopython distribution and governed by its license.  Please see the LICENSE file that should have been included as part of this package
###Preparation of Sequence
##Goal
The goal was to end with sequences which have all the same lenght and no gaps. Therefore We trimmend the sequences so that all have the same start and end point and no gaps

##Trimming

To trim we used the tool trimAl a command line based tool for automated alignment trimming.


Installation of Trimming
1. Go to the [trimAl_website] (http://trimal.cgenomics.org/downloads) and download [the program for linux](http://trimal.cgenomics.org/_media/trimal.v1.2rev59.tar.gz)

2. Follow Basic Installation displayed in the README.md file
==================

The simplest way to compile this package is:

  1. 'cd' to the directory containing the package's source code ('source').

  2. Type 'make' to compile the package.

  3. Optionally, run trimAl/readAl with the examples into the 'dataset' 
     directory to check the correct installation.

   By default, 'make' compiles the source code of trimAl and readAl in the
current directory. After that, you can either add to PATH the current
directory or move these files to '/usr/local/bin' or to '/usr/bin' using
root privileges.

Citation:
** Authors **

Salvador Capella-Gutierrez.
  Comparative Genomics Group. Bioinformatics and Genomics Department.
  Centre for Genomic Regulation. Barcelona, Spain.
  e-mail: scapella _at_ crg.es

Toni Gabaldón.
  Comparative Genomics Group. Bioinformatics and Genomics Department.
  Centre for Genomic Regulation. Barcelona, Spain.
  e-mail: tgabaldon _at_ crg.es

** Authors (until trimAl v1.1) **

Jose Ma. Silla-Martínez.
  e-mail: josilma1 _at_ gmail.com


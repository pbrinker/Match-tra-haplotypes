#Determine Haplotypes

##Convert clustalw format to fasta
First we have to bring our input file “ẗra_trim.fas” from clustal format into a fasta format

1. used [web interface](http://sequenceconversion.bugaco.com/converter/biology/sequences/clustal_to_fasta.php) for conversion

Copyright 2000-2013 bugaco.com

Output: Tra_Conv.fasta

2. Duplicate file and rename
   Bring sequences in one line in jedit
        search: ([GATC])\n([GATC])
        replace with nothing

Output: Tra_Conv_sl.fasta
       
Use created file for the determination of haplotypes

3. To determine haplotypes run the ‘detHaplo.py’ script, which groups samples together with an identical sequence


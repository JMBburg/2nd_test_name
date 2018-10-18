#!env python

"""
Python script to count the number of aminoacids per sequence in a FASTA file
Call it like so:
    python fasta_length.py sequences.fasta
    add some more code to give feedback on type of aminoacids
    do whatever else you want. 
"""

import sys

sequence_length = 0
fasta_sequence_lengths = []

# Getting the filename from the list of arguments
fasta_filename = sys.argv[1]

# Opening the file:
fastafile = open(fasta_filename, 'r')

# Iterating over all lines in the file:
for line in fastafile.readlines():
    if line.startswith('>'):
        if sequence_length:
            fasta_sequence_lengths.append(sequence_length)
        sequence_length = 0
    else:
        sequence_length += len(line.strip())
fasta_sequence_lengths.append(sequence_length)

# Closing the file:
fastafile.close()

#create a function which prints the sorted sequence length as wella s the
# maxmum and minumum sequence lenght
def results_investigation(length_list):
	print(sorted(length_list))	
	print("The minimum is {} and the maxmium is {}." .format(min(length_list), max(length_list)))

#call the function
results_investigation(fasta_sequence_lengths)

#print the maximum of sequence lengths
#print(max(fasta_sequence_lengths))

'''
Author : Bhagya Hendalage
Date : 27/12/2020
Write methods for sequence for sequence analysis
method to split multiple FASTA sequences
method to check the type of a given sequence is DNA, mRNA or amino acid sequence
method to count AT bases
'''

#method for count AT bases
def AT_counts(sequence):
    AT_count=0
    #check and select DNA
    if 'M' not in sequence:
     for i in sequence:
         if i=='A' or i=='T':
             AT_count +=1
    #if sequence is an amino acid
    else:
        AT_count = "Not a DNA sequence"
    return  AT_count

#method for split fasta file
def split_fasta_file(filename):
    #define an empty dictionary
    dict = {}
    with open(filename, 'r') as file:
        header = ''
        for line in file:
            if line != '\n':
                line = line.strip()
                # identify the headers
                if line.startswith('>'):
                    header = line
                    dict[header] = ''
                # if it is not a header, it defines as sequence
                else:
                    dict[header] += line.strip()
    print(dict)
    return (dict)

#method for find type of the molecule
def type_of_molecule(sequence):
        if 'M' in sequence:
            return "Amino acid"
        elif 'U' in sequence and 'M' not in sequence:
            return "mRNA"
        else:
            return "DNA"

#give an input to a method and output save as a variable
dic = split_fasta_file("OSDREB_sequences.fasta")
for key,value in dic.items():
    print('header : ',key)
    print('sequence : ',value)
    print('Type Of the Molecule : ',type_of_molecule(value))
    print('AT count in the sequence : ',AT_counts(value), '\n')
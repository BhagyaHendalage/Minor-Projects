#! /usr/bin/python3
# import packages
from Bio import SeqIO
# take the file
for record in SeqIO.parse("mRNA_seq.fasta", "fasta"):
    sequence=record.seq
    seq = sequence + (len(sequence)%3-1)*'N'
    amino_acids=seq.translate()
    header=str(record.id)
    header_parts=header.split("_")
    header1=str(header_parts[0])+str(header_parts[1])+"_translated\n"
file = open( "aa_seq.fasta" , 'w')
file.write(">"+str(header1)+str(amino_acids))
file.close()

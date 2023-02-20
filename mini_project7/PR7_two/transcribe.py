#! /usr/bin/python3
# import packages
from Bio import SeqIO
#get the file
for record in SeqIO.parse('cds_seq.fasta' , 'fasta'):
        # take the header part
        accession = record.id
        # take the sequence part
        seq = record.seq
        # transcribe the sequence
        sequence=seq.transcribe()
        # add the 'transcribed' part to the end of the header
        header=str(accession)+'_transcribed'
# write the mRNA_seq.fasta file
file = open( 'mRNA_seq.fasta' , 'w')
file.write('>'+str(header)+'\n'+str(sequence))
file.close()

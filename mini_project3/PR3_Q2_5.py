'''
Author : Bhagya Hendalage
Date : 31/12/2020
create objects for each FASTA record create list of values call them in different locations
'''
from s13674_PR3_Q2 import *
sequence=Sequence.fasta_Split("OSDREB_sequences.FASTA")
seq_objects = []

for key,value in sequence.items():
    if Sequence.get_Seq_Type(value[1])=="DNA":
        seq_objects.append(DNAseq(key,value[0][1],value[0][2],value[0][3],value[1]))
    elif Sequence.get_Seq_Type(value[1]) == "mRNA":
        seq_objects.append(mRNAseq(key,value[0][1], value[0][2], value[0][3],value[1]))
    else:
        seq_objects.append(Proteinseq(key,value[0][1],value[0][2],value[0][3],value[1],value[0][4],True))
for objects in seq_objects:

    if objects.seq_type == "DNA" and "DREB1A" in objects.gene_name:
        print('i')
        print("Gene ID: ",objects.gene_ID)
        print("Sequence length: ", objects.seq_length)
        print("Sequence type: ", objects.seq_type)
        print("AT content: ", objects.AT_content,'%')
        print()

    if objects.seq_type == "DNA" and "DREB1B" in objects.gene_name:
            print('ii')
            new_seq = DNAseq.transcribe_Sequence(DNAseq, objects.sequence)
            mRNA = mRNAseq(objects.gene_name, objects.gene_ID, objects.sp_name, objects.subsp_name, new_seq)
            print("Sequence length: ", mRNA.seq_len)
            print("Sequence type: ", mRNA.seq_type)
            print("AT content: ", mRNA.AT_content,'%')
            print("Sequence: ", mRNA.sequence)
            print()

            print('iii')
            prot = mRNA.Translated_sequence
            print("protein: ", prot)
            print("length: ", len(prot))
            print()

    if objects.seq_type == "Amino acid" and "DREB2A_P" in objects.gene_name:
            print('iv')
            print("Uniprot ID: ", objects.uniprot_ID)
            print("reviewed: ", "yes" if objects.reveiwed else "no")
            print("Composition: ", objects.get_Character_Count(objects.sequence))
            print("hydrophobicity: ", objects.Hydrophobicity,'%')
            print()
print('v')
print(Sequence.seq_count)
#! /usr/bin/python3
# import the packages
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

for seq_record in SeqIO.parse("aa_seq.fasta", "fasta"):
    myseq = str(seq_record.seq)

    # remove unwanted letters for make protein unambigous else it gives a error
    prot = myseq.replace('*', '')
    prot = prot.replace('X', '')
new = ProteinAnalysis(str(prot))
header = seq_record.id
weight = new.molecular_weight()
file = open("aa_stats.txt", 'w')
file.write(str(header) + "\n" + "length of amino acid:" + str(
    len(seq_record)) + "\n" + "molecular weight of amino acid:" + str(weight) + "\n" + "alanine percentage:" + str(
    new.get_amino_acids_percent()['A']) + "\n" + "glycine percentage:" + str(new.get_amino_acids_percent()['G']))
file.close()

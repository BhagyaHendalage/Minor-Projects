from Bio import SeqIO

for seq_record in SeqIO.parse("ATdreb2a.fasta.fasta", "fasta"):
    print(seq_record.id)
    print(seq_record.description)
    # print(repr(seq_record.seq))
    print(seq_record.seq)
    print(len(seq_record))

from Bio.Blast import NCBIWWW
from Bio import SeqIO
record = SeqIO.read("ATdreb2a.fasta.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)
with open("dreb2a_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
    result_handle.close()
result_handle = open("dreb2a_blast.xml")

import re
from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)
E_VALUE_THRESH = 0.05
pattern="ACGT[GT]C"
counter=0
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            string=hsp.sbjct
            mo=re.finditer(pattern,string)
            for item in mo:
                counter += 1
                print("****Alignment****")
                print("sequence:", alignment.hit_def)
                print("length:", alignment.length)
                print("e value:", hsp.expect)
                print("Score", hsp.score)
                print("Hit sequence:", hsp.sbjct)
                print(item.group())
                print(item.span())
                print("Hit sequence length:", hsp.align_length)
print("the number of blast hits with ABRE element present in the sequence",counter)
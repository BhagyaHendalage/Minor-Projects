#! /usr/bin/python3
# import the packages
from Bio import Entrez
Entrez.email = "Your.Name.Here@example.org"
# to get the accession number with version
id = input("Enter  the acccession number(with version): ")
# retrieve the fasta file from database
handle = Entrez.efetch(db="Nucleotide", id=id, rettype="fasta", retmode="text")
# write file as cds_seq.fasta
with open('cds_seq.fasta', 'w') as file:
        file.writelines(handle)
handle.close()


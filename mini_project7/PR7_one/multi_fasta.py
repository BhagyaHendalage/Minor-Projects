#! /usr/bin/python3
from Bio import Entrez
sequences = ["AAK43967.1","AED90870.1","NP_567720.1","AAK59861.1"]
Entrez.email = "Your.Name.Here@example.org"
for id in sequences:
    handle = Entrez.efetch(db="protein", id=id, rettype="fasta", retmode="text")
    file1 = str(id) + ".fasta"
    with open(file1, 'w') as file:
        file.writelines(handle)
handle.close()

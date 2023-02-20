'''
Bhagya Hendalage
2017s16415

Practical 02
Generate a peptide chain using mRNA sequence
'''
Codon_map = {}
# open codon_table and store as a variable
with open('codon_table.txt', 'r') as codon_table:
    for line in codon_table:
       # remove header and empty lines
        if '#' not in line and line != '\n':
            (codon, AminoAcid, Letter, FullName) = line.strip().split('\t')
            # fill the dictionary using codons and related amino acid name
            Codon_map[codon] = Letter
print(Codon_map)

peptide_chain = ""
sequence = ""
# open the sequence and store as a variable
with open('OSDREB1A_mRNA.fasta', 'r') as sequenceFile:
    for line in sequenceFile:
        if line != '\n':
            line = line.strip()
            # remove the header of the sequence
            if '>' not in line:
                sequence += line
print('mRNA sequence:',sequence)

base = 0
while base < len(sequence):
    # 3 bases consider as codon
    Codon = sequence[base:base+3]
    #matching with codon table and add appropiate amino acid to the peptide chain
    if Codon in Codon_map.keys():
     peptide_chain += Codon_map[Codon]
     #stop at a stop codon
    if Codon_map[Codon] == 'O':
             break
    #iterate by 3
    base +=3
print('protein sequence:'+ peptide_chain)

# write translated peptide chain
with open("Peptide_chain.fasta", 'w') as output:
    output = output.write("_Trnslated" + '\n' + peptide_chain)

#remove the stp codon has no amino acid
print('length of the protein is :',len(peptide_chain)-1)


#when considering, proteins are start from Met amino acid and stp in stop codon
for base in peptide_chain:
    base_no_M = peptide_chain.find('M')
    base_no_O = peptide_chain.find('O')
print('actual protein sequence length:',base_no_O - base_no_M)











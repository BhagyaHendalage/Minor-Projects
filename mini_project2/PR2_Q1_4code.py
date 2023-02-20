# create a dictionary
d = {}
#open fasta file
with open('OSDREB1A.fasta','r') as f:
    #read each line in file
    for line in f:
        #check whether it is a fasta header line
            if '>' in line:
                key = line.strip().replace('>','')
                d[key] = ""
            #check whether it is a sequence lines
            else:
                #check whether it is nucleotide sequence
                if 'M' not in line:
                    d[key] += line.strip().replace('T', 'U')

                else:
                    d[key] += line.strip()

    d = {key: d[key] for key in d}
    print(d)
#save a file contain only mRNA sequence
with open('OSDREB1A_mRNA.fasta','w') as file1:
#add trancribed word to the fasta header
    for item in d:
        if 'mRNA' in item:
            header = item+'_Transcribed'
            print(header)
            print(d[item])
            file1.write('>'+header+'\n')
            file1.write(d[item])
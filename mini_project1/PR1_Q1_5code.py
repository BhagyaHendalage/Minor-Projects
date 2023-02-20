'''

2017s16415
D.P.B.Hendalage
'''
sequence=''
#open sequence and store as variable
with open('sequence.fasta','r') as sequencefile:
    for line in sequencefile:
        if line != '\n':
            line = line.strip()
             #remove the fasta header
            if ('>') not in line:
                sequence = sequence+line
print (sequence)
#calculate the count
sequencelength = len(sequence)
#take output
print('the length of sequence is',sequencelength)
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
#define counter
basecounter = 0
#for each base in sequence
for base in sequence:
    #increase base counter by one
   basecounter+=1
#take output
print('the length of sequence is',basecounter)
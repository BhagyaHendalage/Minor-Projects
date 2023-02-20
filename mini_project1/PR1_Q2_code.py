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
#print the sequence
print (sequence)
#define counters
aCount = 0
cCount = 0
tCount = 0
gCount = 0
#for loop for identify different bases
for c in sequence:
    if c == 'A':
        aCount = aCount+1
    elif c == 'C':
        cCount = cCount+1
    elif c == 'T':
        tCount = tCount+1
    elif c == 'G':
        gCount = gCount+1
#print the A,T,G,C Count seperately
print('Total A count in sequence is',aCount)
print('Total C count in sequence is',cCount)
print('Total T count in sequence is',tCount)
print('Total G count in sequence is',gCount)
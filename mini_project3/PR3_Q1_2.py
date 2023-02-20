'''
Practical03
2017s16415

D.P.B.Hendalage
'''
def AT_content(sequence):
    #define counters for 'A' and 'T'
    A=0
    T=0
    for base in sequence:
        if base=='A':
            A+=1
        elif base=='T':
            T+=1
    print("A base count is:",A)
    print("T base count is:",T)
AT_content('ATATATACGCGCG')

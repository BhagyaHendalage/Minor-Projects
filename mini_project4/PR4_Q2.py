'''
Author:Bhagya Hendalage
Date:16/01/2021
input:protein_interactions_pr4.tsv and AT_stress_proteins.txt
output: degree of DREB2A
        the number of unknown proteins in the network for stress tolerance
        the ordered list of predicted the majority voting scores with unknown protein name
to predict the majority voting score of unknown proteins for a given function in a network
a list of known proteins annotated to the particular function
output the list of unknown proteins with the predicted majority voting score.
'''
import networkx as nx
proteins=[]
known_prot=[]

# Create an empty graph
g = nx.Graph()

# read interactions and store it in variable
with open ('protein_interactions_pr4.tsv' ,'r' ) as file:
    for lines in file:
        if '#' not in lines:
            lines=lines.strip().split('\t')
            proteins.append(lines[0].upper())
            proteins.append(lines[1].upper())
            g.add_edge(lines[0].upper(), lines[1].upper())

print('The degree of the ATDREB2A protein :',g.degree('DREB2A'))
#print(g.degree)
#print(proteins)

# Read the proteins and store it in variable
with open ('AT_stress_proteins.txt' ,'r' ) as file:
    for lines in file:
        lines=lines.strip().split('\t')
        known_prot.append(lines[1].upper())
#print(known_prot)

# Find the unknown proteins
unkown_prot=[]
for protein in proteins:
    # using set, find the proteins which are in the network but not know the function
    unkown_prot= list(set(proteins) - set(known_prot))
#print(unkown_prot)

#create a dictionary
# key is function unknown proteins value is how many neighbors they have amoung the function known proteins
prot_scoring = {}
key = ''
# find neighbors of unknown proteins
for un_p in unkown_prot:
    key = un_p
    neighbors_list = (list(nx.all_neighbors(g, un_p)))
    # get proteins which are function is known
    neighbors = list(set(neighbors_list) & set(known_prot))
    # count the number of items in list, asign as the value of the dictionary
    prot_scoring[key] = len(neighbors)
print('The number of unknown proteins in the network for stress tolerance :',len(prot_scoring))
#print(scoring)

import operator
# sort the dictionary key according to the descending order of the value
sorted_dict =dict(sorted(prot_scoring.items(),key=operator.itemgetter(1),reverse=True))
# convert the dictionary to a list
print('The ordered list of predicted the majority voting scores with unknown protein name :')
print(list(sorted_dict.items()))
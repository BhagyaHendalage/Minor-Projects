import networkx as nx
G = nx.Graph()

interactions = {}
base = 0
# open the codon table and store it in a variable
with open('string_interactions.tsv', 'r') as table:
    for line in table:

        #remove headers table divided into colomns
        if '#' not in line and line != '\n':
               bond = line.strip().split('\t')
               interactions[base] = bond[0:2]
        base += 1
#iterate the values in the dictionary
for key, value in interactions.items():
    G.add_edge(value[0],value[1])
print('Number of edges in the graph:',G.number_of_edges())
print('Number of nodes in the graph:',G.number_of_nodes())
print('Degree of DREB1A is: ' + str(G.degree['ERF24']))

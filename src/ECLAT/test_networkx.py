import networkx as nx
from networkx.algorithms.approximation import clique
import time
from datetime import timedelta

G = nx.read_edgelist('outfile.txt',delimiter=',')

nx.clique.find_cliques(G)




for clq in nx.clique.find_cliques(G):
    print(clq)


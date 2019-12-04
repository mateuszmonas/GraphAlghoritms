from main.dimacs import load_weighted_graph
from main.lab4.graph import Graph

path = 'graphs/maxclique/interval-rnd50'

g = Graph(load_weighted_graph(path))
print(g.find_biggest_clique())

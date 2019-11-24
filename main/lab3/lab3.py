import heapq

from main.dimacs import load_weighted_graph
from main.lab3.graph import Graph

g = Graph(load_weighted_graph('graphs-lab3/clique100'))
print(g.find_min_cut())

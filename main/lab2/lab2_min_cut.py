from main.dimacs import load_directed_weighted_graph
from main.lab2.graph import Graph

graph = Graph(load_directed_weighted_graph('graphs/connectivity/simple'))
print(str(graph.find_min_cut()))

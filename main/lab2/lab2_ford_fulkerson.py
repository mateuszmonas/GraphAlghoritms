from main.dimacs import load_directed_weighted_graph
from main.lab2.graph import Graph

graph = Graph(load_directed_weighted_graph('graphs/flow/worstcase'))
print(str(graph.find_max_flow()))

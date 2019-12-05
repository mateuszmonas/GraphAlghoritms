from main.dimacs import load_weighted_graph
from main.lab4.graph import Graph

path = 'graphs/vcover/nonplanar-ex1'

g = Graph(load_weighted_graph(path))
print(g.find_min_vertex_cover())


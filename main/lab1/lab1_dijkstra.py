from main.dimacs import load_weighted_graph
from main.lab1.graph import Graph

g = load_weighted_graph('graphs-lab1/rand1000_100000')
graph = Graph(g)
weights = graph.dijkstra_max_current(1)
print(weights[2])

from main.dimacs import load_weighted_graph
from main.lab4.graph import Graph

path = 'graphs/chordal/house'

g = Graph(load_weighted_graph(path))
order = g.lex_bfs(1)
print(order)
print(g.check_peo())


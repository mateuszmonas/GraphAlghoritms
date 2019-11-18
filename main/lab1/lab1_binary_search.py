from main.dimacs import load_weighted_graph
from main.lab1.graph import Graph


def min_weight_binary_search(graph: Graph, start: int, end: int, min_weight: int, max_weight: int):
    curr_weight = 0
    while min_weight <= max_weight:
        curr_weight = int((min_weight + max_weight) / 2)
        if graph.dfs_min_weight(start, end, curr_weight):
            min_weight = curr_weight + 1
        else:
            max_weight = curr_weight - 1
    if graph.dfs_min_weight(start, end, curr_weight):
        return curr_weight
    return curr_weight - 1


g = load_weighted_graph('graphs-lab1/rand1000_100000')
graph = Graph(g)
max_weight = max(g[1], key=lambda x: x[2])[2]
print(min_weight_binary_search(graph, 1, 2, 0, max_weight))

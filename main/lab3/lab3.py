from queue import PriorityQueue

from main.lab3.dimacs import load_weighted_graph


def adj_list(g):
    graph = {}
    for e in g[1]:
        if e[0] - 1 not in graph:
            graph[e[0] - 1] = {}
        if e[1] - 1 not in graph:
            graph[e[1] - 1] = {}
        add_edge(graph, e[0] - 1, e[1] - 1, e[2])
    return graph


def add_edge(graph, node_a, node_b, weight):
    graph[node_a][node_b] = weight
    graph[node_b][node_a] = weight


def remove_edge(graph, node_a, node_b):
    graph[node_a].pop(node_b)
    graph[node_b].pop(node_a)


def merge_vertices(graph, node_a, node_b):
    cpy = graph[node_a].copy()
    for k, v in cpy.items():
        if k == node_b:
            remove_edge(graph, node_a, k)
            continue
        if k in graph[node_b]:
            graph[node_b][k] += v
        else:
            graph[node_b][k] = v
        remove_edge(graph, node_a, k)


def print_graph(graph):
    for k, v in graph.items():
        print(k, v)


def minimum_cut_phase(graph):
    a = 0
    S = {a}
    heap = []


class Node:
    def __init__(self):
        self.edges = {}

    def add_edge(self, to, weight):
        self.edges[to]=weight

    def remove_edge(self, to):
        self.edges.pop(to)


def main():
    g = adj_list(load_weighted_graph('graphs-lab3/clique5'))
    merge_vertices(g, 0, 1)




main()

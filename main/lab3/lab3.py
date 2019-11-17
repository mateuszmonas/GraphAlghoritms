import heapq
from queue import PriorityQueue

from main.lab3.dimacs import load_weighted_graph


def adj_list(g):
    graph = {}
    for e in g[1]:
        if e[0] - 1 not in graph:
            graph[e[0] - 1] = Node(e[0] - 1)
        if e[1] - 1 not in graph:
            graph[e[1] - 1] = Node(e[1] - 1)
        add_edge(graph, e[0] - 1, e[1] - 1, e[2])
    return graph


def add_edge(graph, node_a, node_b, weight):
    graph[node_a].add_edge(node_b, weight)
    graph[node_b].add_edge(node_a, weight)


def remove_edge(graph, node_a, node_b):
    graph[node_a].remove_edge(node_b)
    graph[node_b].remove_edge(node_a)



def print_graph(graph):
    for k, v in graph.items():
        print(v.label, v.edges)


def minimum_cut_phase(graph):
    a = 0
    S = {a}
    heap = []
    for k, v in graph.items():
        if len(v.edges) == 0:
            continue
        if k != a:
            v.count_weights_to_nodes(S)
            heap.append(v)

    heapq.heapify(heap)
    last_two = []
    while heap:
        node = heapq.heappop(heap).key
        S.add(node)
        if len(heap) < 2:
            last_two.append(node)
        for k, v in graph.items():
            v.remove_weight(node)
        heapq.heapify(heap)


    if len(last_two) < 2:
        result = graph[last_two[0]].count_all_weights()
        merge_vertices(graph, 0, last_two[0])
    else:
        result = graph[last_two[1]].count_all_weights()
        merge_vertices(graph, last_two[0], last_two[1])
    return result

class Node:

    def __init__(self, key):
        self.edges = {}
        self.weight = 0
        self.key = key
        self.label = str(key)

    def count_all_weights(self):
        weight = 0
        for k, v in self.edges.items():
            weight+=v
        return weight

    def count_weights_to_nodes(self, S):
        for k in S:
            self.weight += self.edges.get(k, 0)

    def remove_weight(self, to):
        self.weight -= self.edges.get(to, 0)

    def add_edge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight

    def remove_edge(self, to):
        del self.edges[to]

    def __gt__(self, other):
        return self.weight < other.weight

    def __ge__(self, other):
        return self.weight <= other.weight

    def __le__(self, other):
        return self.weight >= other.weight

    def __lt__(self, other):
        return self.weight > other.weight


def merge_vertices(graph, node_a, node_b):
    graph[node_b].label += graph[node_a].label
    cpy = graph[node_a].edges.copy()
    for k, v in cpy.items():
        if k == node_b:
            remove_edge(graph, node_a, k)
            continue
        add_edge(graph, node_b, k, v)
        remove_edge(graph, node_a, k)


def main():
    g = adj_list(load_weighted_graph('graphs-lab1-lab3/geo100_2a'))
    result = 10000000000
    for i in range(0, len(g)-1):
        potential_result = minimum_cut_phase(g)
        if(potential_result<result):
            result=potential_result
    print(result)


main()

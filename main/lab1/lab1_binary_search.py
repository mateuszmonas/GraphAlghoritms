from queue import Queue, LifoQueue
from typing import List, Dict, Set

from main.lab1.load_weighted_graph import load_weighted_graph


class Node:

    def __init__(self, key):
        self.edges: Dict[int, int] = {}
        self.weight = 0
        self.key = key

    def add_edge(self, to: int, weight: int):
        self.edges[to] = self.edges.get(to, 0) + weight

    def remove_edge(self, to: int):
        del self.edges[to]

    def __gt__(self, other):
        return self.weight < other.weight

    def __ge__(self, other):
        return self.weight <= other.weight

    def __le__(self, other):
        return self.weight >= other.weight

    def __lt__(self, other):
        return self.weight > other.weight


class Graph:

    def __init__(self, g) -> None:
        super().__init__()
        self.nodes: Dict[int, Node] = {}
        self.generate_graph(g)

    def generate_graph(self, g):
        for e in g[1]:
            self.add_edge(e[0], e[1], e[2])

    def dfs_min_weight(self, start, end, min_weight) -> bool:
        vertices = LifoQueue()
        visited: Set[int] = set()
        visited.add(start)
        vertices.put(start)
        while not vertices.empty():
            curr = vertices.get()
            for k, v in self.nodes[curr].edges.items():
                if k not in visited and v >= min_weight:
                    if k == end:
                        return True
                    visited.add(k)
                    vertices.put(k)
        return False

    def bfs(self, start: int):
        self.search(start, Queue())

    def dfs(self, start: int):
        self.search(start, LifoQueue())

    def search(self, start, vertices):
        visited: Set[int] = set()
        visited.add(start)
        vertices.put(start)
        while not vertices.empty():
            curr = vertices.get()
            print(curr)
            for k in self.nodes[curr].edges.keys():
                if k not in visited:
                    visited.add(k)
                    vertices.put(k)

    def add_edge(self, node_a: int, node_b: int, weight: int):
        if node_a not in self.nodes:
            self.nodes[node_a] = Node(node_a)
        if node_b not in self.nodes:
            self.nodes[node_b] = Node(node_b)
        self.nodes[node_a].add_edge(node_b, weight)
        self.nodes[node_b].add_edge(node_a, weight)

    def remove_edge(self, node_a: int, node_b: int):
        self.nodes[node_a].remove_edge(node_b)
        self.nodes[node_b].remove_edge(node_a)


def min_weight_binary_search(graph: Graph, start: int, end: int, min_weight: int, max_weight: int):
    while min_weight <= max_weight:
        curr_weight = int((min_weight + max_weight) / 2)
        if graph.dfs_min_weight(start, end, curr_weight):
            min_weight = curr_weight + 1
        else:
            max_weight = curr_weight - 1
    if graph.dfs_min_weight(start, end, curr_weight):
        return curr_weight
    return curr_weight - 1


g = load_weighted_graph('graphs-lab1/pp1000')
graph = Graph(g)
max_weight = max(g[1], key=lambda x: x[2])[2]
print(min_weight_binary_search(graph, 1, 2, 0, max_weight))

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

    def __init__(self) -> None:
        super().__init__()
        self.nodes: Dict[int, Node] = {}

    def dfs(self):
        self.search(Queue())

    def bfs(self):
        self.search(LifoQueue())

    def search(self, vertices):
        visited: Set[int] = set()
        first = next(iter(self.nodes))
        visited.add(first)
        vertices.put(first)
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


def dfs(graph, visited, path, i, j):
    i = i - 1
    j = j - 1
    visited[i] = True
    for e in graph[i]:
        if e[0] == j:
            path.append(e)
            return True
        if visited[e[0]]:
            continue
        path.append(e)
        if dfs(graph, visited, path, e[0] + 1, j + 1):
            return True
        path.pop()


def adj_list(g):
    graph = Graph()
    for e in g[1]:
        graph.add_edge(e[0], e[1], e[2])
    return graph


graph = adj_list(load_weighted_graph('graphs-lab1/clique5'))
graph.dfs()
graph.bfs()

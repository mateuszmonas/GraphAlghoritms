import sys
from queue import Queue, LifoQueue, PriorityQueue
from typing import List, Dict, Set


def load_weighted_graph(name):
    V = 0
    L = []

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if len(s) < 1:
            continue
        if s[0] == "c":
            continue
        elif s[0] == "p":
            V = int(s[2])
        elif s[0] == "e":
            (a, b, c) = (int(s[1]), int(s[2]), int(s[3]))
            (x, y, c) = (min(a, b), max(a, b), c)
            L.append((x, y, c))

    f.close()
    return (V, L)


class Node:

    def __init__(self, key):
        self.edges: Dict[int, int] = {}
        self.key = key

    def add_edge(self, to: int, weight: int):
        self.edges[to] = self.edges.get(to, 0) + weight

    def remove_edge(self, to: int):
        del self.edges[to]


class Graph:

    def __init__(self, g) -> None:
        super().__init__()
        self.nodes: Dict[int, Node] = {}
        self.generate_graph(g)

    def generate_graph(self, g):
        for e in g[1]:
            self.add_edge(e[0], e[1], e[2])

    def dijkstra(self, start: int):
        weights: Dict[int, int] = {}
        for k in self.nodes.keys():
            if k == start:
                weights[k] = 0
            else:
                weights[k] = sys.maxsize
        queue = PriorityQueue()
        queue.put((0, start))
        while not queue.empty():
            curr = queue.get()
            curr_weight = curr[0]
            curr_key = curr[1]
            for k, v in self.nodes[curr_key].edges.items():
                if curr_weight + v < weights[k]:
                    weights[k] = curr_weight + v
                    queue.put((curr_weight + v, k))
        return weights


    def dijkstra_max_current(self, start: int):
        weights: Dict[int, int] = {}
        for k in self.nodes.keys():
            weights[k] = 0
        queue = PriorityQueue()
        queue.put((-sys.maxsize, start))
        while not queue.empty():
            curr = queue.get()
            curr_weight = -curr[0]
            curr_key = curr[1]
            for k, v in self.nodes[curr_key].edges.items():
                if min(curr_weight, v) > weights[k]:
                    weights[k] = min(curr_weight, v)
                    queue.put((-min(curr_weight, v), k))
        return weights

    def dfs_min_weight(self, start: int, end: int, min_weight: int) -> bool:
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

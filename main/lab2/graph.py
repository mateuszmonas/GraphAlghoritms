import sys
from queue import Queue, LifoQueue
from typing import Dict, Set

from main.GraphTemplate import GraphTemplate, NodeTemplate


class Edge:

    def __init__(self, weight) -> None:
        super().__init__()
        self.weight = weight
        self.flow = 0

    def __str__(self):
        return str(self.flow) + '/' + str(self.weight)


class Node:

    def __init__(self, key):
        self.edges: Dict[int, Edge] = {}
        self.key = key

    def add_edge(self, to: int, weight: int):
        self.edges[to] = Edge(weight)

    def sum_flow(self):
        result = 0
        for k, v in self.edges.items():
            result += v.flow
        return result

    def __str__(self):
        result = str(self.key) + ': '
        for k, v in (self.edges.items()):
            result += '(' + str(k) + ', ' + str(v) + '), '
        return result


class Graph(GraphTemplate):

    def __init__(self, g) -> None:
        super().__init__(g, Node)

    def add_edge(self, node_a: int, node_b: int, weight: int):
        if node_a not in self.nodes:
            self.nodes[node_a] = self.node_type(node_a)
        if node_b not in self.nodes:
            self.nodes[node_b] = self.node_type(node_b)
        self.nodes[node_a].add_edge(node_b, weight)
        self.nodes[node_b].add_edge(node_a, 0)

    def remove_edge(self, node_a: int, node_b: int):
        self.nodes[node_a].remove_edge(node_b)

    def dfs(self, curr: int, end: int, visited=None, flow: int = sys.maxsize):
        if visited is None:
            visited = set()
        visited.add(curr)
        if curr == end:
            return flow

        for k, v in self.nodes[curr].edges.items():
            if k not in visited and v.weight - v.flow > 0:
                temp_weight = self.dfs(k, end, visited, min(v.weight - v.flow, flow))
                if temp_weight is not None:
                    self.nodes[curr].edges[k].flow += temp_weight
                    self.nodes[k].edges[curr].flow -= temp_weight
                    return temp_weight

        return None

    def find_max_flow(self):
        while True:
            if self.dfs(1, len(self.nodes)) is None:
                break
        return -self.nodes[len(self.nodes)].sum_flow()

    # nie dziala
    def find_min_cut(self):
        minimal_cut = sys.maxsize
        for i in range(0, len(self.nodes)-1):
            for j in range(i+1, len(self.nodes)):
                while True:
                    if self.dfs(i+1, j+1) is None:
                        current_cut = -self.nodes[j+1].sum_flow()
                        if current_cut < minimal_cut:
                            minimal_cut = current_cut
                        break

        return minimal_cut

    def __str__(self):
        result = ''
        for k, v in self.nodes.items():
            result += str(v) + '\n'
        return result

from typing import List, Dict, Set

from main.GraphTemplate import GraphTemplate, NodeTemplate


class Node(NodeTemplate):

    def __init__(self, key):
        super().__init__(key)
        self.label = str(key)
        self.weights_sum = 0

    def count_weights_sum_to(self, S: Set[int]):
        for e in S:
            self.weights_sum += self.edges.get(e, 0)

    def remove_weight(self, e):
        self.weights_sum -= self.edges.get(e, 0)


class Graph(GraphTemplate):

    def __init__(self, g) -> None:
        self.nodes: Dict[int, Node] = {}
        super().__init__(g, Node)

    def merge_vertices(self, node_a, node_b):
        self.nodes[node_a].label += self.nodes[node_b].label
        self.remove_edge(node_a, node_b)
        cpy = self.nodes[node_b].edges.copy()
        for k, v in cpy.items():
            self.add_edge(node_a, k, v)
            self.remove_edge(node_b, k)

    def __str__(self):
        result = ''
        for k, v in self.nodes.items():
            result += v.label + ' ' + str(v.edges) + '\n'
        return result

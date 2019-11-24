from typing import Dict

class NodeTemplate:

    def __init__(self, key):
        super().__init__()
        self.edges: Dict[int, int] = {}
        self.key = key

    def add_edge(self, to: int, weight: int):
        self.edges[to] = weight

    def remove_edge(self, to: int):
        if to in self.edges.keys():
            del self.edges[to]

    def __str__(self):
        result = str(self.key)+ ': '
        for k, v in self.edges.items():
            result += '(' + str(k) + ', ' + str(v) + '), '
        return result

class GraphTemplate:

    def __init__(self, g, node_type=NodeTemplate) -> None:
        super().__init__()
        self.node_type = node_type
        self.nodes: Dict[int, node_type] = {}
        self.generate_graph(g)

    def generate_graph(self, g):
        for e in g[1]:
            self.add_edge(e[0], e[1], e[2])

    def add_edge(self, node_a: int, node_b: int, weight: int):
        if node_a not in self.nodes:
            self.nodes[node_a] = self.node_type(node_a)
        if node_b not in self.nodes:
            self.nodes[node_b] = self.node_type(node_b)
        self.nodes[node_a].add_edge(node_b, weight)
        self.nodes[node_b].add_edge(node_a, weight)

    def remove_edge(self, node_a: int, node_b: int):
        self.nodes[node_a].remove_edge(node_b)
        self.nodes[node_b].remove_edge(node_a)

    def __str__(self):
        result = ''
        for k, v in self.nodes.items():
            result += str(v) + '\n'
        return result

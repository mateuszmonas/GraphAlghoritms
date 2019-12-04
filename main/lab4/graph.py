import heapq
import sys
from queue import PriorityQueue, Queue
from typing import List, Dict, Set

from main.GraphTemplate import GraphTemplate, NodeTemplate


class Node(NodeTemplate):

    def __init__(self, key):
        super().__init__(key)

    def __str__(self):
        return str(self.key)


class Graph(GraphTemplate):

    def __init__(self, g) -> None:
        super().__init__(g, Node)

    def get_rn(self, order: List[int], key):
        curr_node = self.nodes[key]
        rn = set()
        for i in range(0, key):
            if order[i] in curr_node.edges.keys():
                rn.add(order[i])
        return rn

    def get_parent(self, order: List[int], key):
        curr_node = self.nodes[key]
        for i in reversed(range(0, key)):
            if order[i] in curr_node.edges.keys():
                return order[i]
        return None

    def check_peo(self):
        order = self.lex_bfs(1)
        rns: Dict[int, set] = {}
        for key in order:
            rns[key] = self.get_rn(order, key)
        for key in order:
            parent = self.get_parent(order, key)
            if parent is not None and not rns[key].difference({parent}).issubset(rns[parent]):
                return False
        return True

    def lex_bfs(self, start: int):
        vertices: PriorityQueue[Node] = PriorityQueue()

        vertices.put(self.nodes[start])
        vertices_sets = [set(self.nodes.keys())]

        visit_order = []

        while vertices_sets:
            curr = vertices_sets[-1].pop()
            visit_order.append(curr)

            new_vertices_set = []
            for nodes in vertices_sets:
                nodes_subset = set()
                for node in nodes:
                    if node in self.nodes[curr].edges:
                        nodes_subset.add(node)
                nodes = nodes.difference(nodes_subset)
                if len(nodes) >0:
                    new_vertices_set.append(nodes)
                if len(nodes_subset)>0:
                    new_vertices_set.append(nodes_subset)
            vertices_sets = new_vertices_set
        return visit_order

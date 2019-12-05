import heapq
import sys
from queue import PriorityQueue, Queue
from typing import List, Dict, Set

from main.GraphTemplate import GraphTemplate, NodeTemplate


class Node(NodeTemplate):

    def __init__(self, key):
        super().__init__(key)
        self.color = None

    def __str__(self):
        return str(self.key)


class Graph(GraphTemplate):

    def __init__(self, g) -> None:
        super().__init__(g, Node)

    def find_min_coloring(self):
        order = self.lex_bfs(1)
        chromatic_number = 0
        for key in order:
            used = set()
            curr_node = self.nodes[key]
            for n in curr_node.edges:
                used.add(self.nodes[n].color)
            for i in range(len(order)):
                if i not in used:
                    if i > chromatic_number:
                        chromatic_number = i
                    curr_node.color = i
                    break
        return chromatic_number+1

    def find_min_vertex_cover(self):
        order = self.lex_bfs(1)
        independent_set = set()
        for key in reversed(order):
            curr_node = self.nodes[key]
            if curr_node.edges.keys().isdisjoint(independent_set):
                independent_set.add(key)
        vertex_cover = set()
        for key in self.nodes:
            if key not in independent_set:
                vertex_cover.add(key)
        return len(vertex_cover)


    def get_rn(self, order: List[int], key):
        curr_node = self.nodes[key]
        rn = set()
        for i in range(0, order.index(key)):
            if order[i] in curr_node.edges.keys():
                rn.add(order[i])
        return rn

    def get_parent(self, order: List[int], key):
        curr_node = self.nodes[key]
        for i in reversed(range(0, order.index(key))):
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

    def find_biggest_clique(self):
        order = self.lex_bfs(1)
        max_size = 0
        for key in order:
            size = len(self.get_rn(order, key))
            if size > max_size:
                max_size = size
        return max_size + 1

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
                if len(nodes) > 0:
                    new_vertices_set.append(nodes)
                if len(nodes_subset) > 0:
                    new_vertices_set.append(nodes_subset)
            vertices_sets = new_vertices_set
        return visit_order

import heapq
import sys
from queue import PriorityQueue
from typing import List, Dict, Set

from main.GraphTemplate import GraphTemplate, NodeTemplate


class Node(NodeTemplate):

    def __init__(self, key):
        super().__init__(key)
        self.active = True
        self.label = str(key)
        self.weights_sum = 0

    def sum_weights_to(self, S: Set[int]):
        self.weights_sum = 0
        for e in S:
            self.add_weight(e)

    def add_weight(self, e: int):
        self.weights_sum += self.edges.get(e, 0)

    def sum_weights_not_to(self, S: Set[int]):
        result = 0
        for k, v in self.edges.items():
            if k not in S:
                result += v
        return result

    def sum_all_weights(self):
        result  = 0
        for k, v in self.edges.items():
            result+=v
        return result

    def __str__(self):
        return self.label

    def __gt__(self, other):
        return isinstance(other, Node) and self.weights_sum < other.weights_sum

    def __ge__(self, other):
        return isinstance(other, Node) and self.weights_sum <= other.weights_sum

    def __le__(self, other):
        return isinstance(other, Node) and self.weights_sum >= other.weights_sum

    def __lt__(self, other):
        return isinstance(other, Node) and self.weights_sum > other.weights_sum


class Graph(GraphTemplate):

    def __init__(self, g) -> None:
        self.nodes: Dict[int, Node] = {}
        super().__init__(g, Node)

    def merge_vertices(self, node_a, node_b):
        self.nodes[node_b].active=False
        self.nodes[node_a].label += self.nodes[node_b].label
        self.remove_edge(node_a, node_b)
        cpy = self.nodes[node_b].edges.copy()
        for k, v in cpy.items():
            self.add_edge(node_a, k, v)
            self.remove_edge(node_b, k)

    def min_cut_phase(self):
        a = next(iter(self.nodes.keys()))
        S = {a}
        queue = []
        # count all nodes weights
        for k, v in self.nodes.items():
            if v.active:
                v.sum_weights_to(S)
                heapq.heappush(queue, v)

        last_two = []
        while queue:
            node = heapq.heappop(queue)
            key = node.key
            if key in S:
                continue
            for n in queue:
                n.add_weight(key)
            heapq.heapify(queue)

            S.add(key)
            if len(queue) < 2:
                last_two.append(key)

        if len(last_two) >= 2:
            s = last_two[1]
            t = last_two[0]
            result = self.nodes[s].sum_all_weights()
            self.merge_vertices(t, s)
            return result
        s = last_two[0]
        result = self.nodes[s].sum_all_weights()
        self.merge_vertices(a, s)
        return result

    def find_min_cut(self):
        result = sys.maxsize
        for i in range(0, len(self.nodes)-1):
            temp_result = self.min_cut_phase()
            if temp_result < result:
                result = temp_result
        return result

    def __str__(self):
        result = ''
        for k, v in self.nodes.items():
            result += v.label + ' ' + str(v.edges) + '\n'
        return result

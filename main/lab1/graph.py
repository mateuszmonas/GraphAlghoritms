import sys
from queue import Queue, LifoQueue, PriorityQueue
from typing import List, Dict, Set

from main.GraphTemplate import GraphTemplate, NodeTemplate


class Graph(GraphTemplate):

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

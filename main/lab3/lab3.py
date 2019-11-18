import heapq

from main.dimacs import load_weighted_graph
from main.lab3.graph import Graph


def main():
    g = Graph(load_weighted_graph('graphs-lab3/clique5'))
    print(str(g))


main()

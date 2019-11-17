from main.lab1.graph import load_weighted_graph


def union(vertices, edge):
    i = find(vertices, edge[0] - 1)
    j = find(vertices, edge[1] - 1)
    vertices[j] = (i, vertices[j][1])


def find(vertices, i):
    if vertices[i][0] == i:
        return i
    else:
        j = find(vertices, vertices[i][0])
        vertices[i] = (j, vertices[i][1])
        return j


def zad(g, i, j):
    vertices = [(i, i + 1) for i in range(g[0])]
    edges = g[1]
    for e in edges:
        union(vertices, e)
        if find(vertices, i) == find(vertices, j):
            return e[2]


def main():
    g = load_weighted_graph('graphs-lab1/clique5')
    g[1].sort(key=lambda x: x[2], reverse=True)
    print(zad(g, 0, 1))
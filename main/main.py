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


def dfs(graph, visited, path, i, j):
    i = i - 1
    j = j - 1
    visited[i] = True
    for e in graph[i]:
        if e[0] == j:
            path.append(e)
            return True
        if visited[e[0]]:
            continue
        path.append(e)
        if dfs(graph, visited, path, e[0] + 1, j + 1):
            return True
        path.pop()


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


def adj_list(g):
    graph = [[] for i in range(g[0])]
    for e in g[1]:
        graph[e[0] - 1].append((e[1] - 1, e[2]))
        graph[e[1] - 1].append((e[0] - 1, e[2]))
    return graph


def adj_list(g, min_weight):
    graph = [[] for i in range(g[0])]
    for e in g[1]:
        if e[2] < min_weight:
            continue
        graph[e[0] - 1].append((e[1] - 1, e[2]))
        graph[e[1] - 1].append((e[0] - 1, e[2]))
    return graph


def main():
    g = load_weighted_graph('graphs/clique1000')
    g[1].sort(key=lambda x: x[2], reverse=True)
    min_weight = zad(g, 0, 1)
    path = []
    dfs(adj_list(g, min_weight), [False for i in range(g[0])], path, 1, 2)
    for a in path:
        print(a)


main()

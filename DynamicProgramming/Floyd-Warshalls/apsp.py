import copy
INP_FILE = "input.dat"


def floyd_warshalls(graph, vertices_count):
    for k in range(vertices_count):
        next_graph = copy.deepcopy(graph)
        for i in range(vertices_count):
            for j in range(vertices_count):
                dist_via = None
                if graph[i][k] is not None and graph[k][j] is not None:
                    dist_via = graph[i][k] + graph[k][j]
                
                if graph[i][j] is None:
                    next_graph[i][j] = dist_via
                elif dist_via is None:
                    next_graph[i][j] = graph[i][j]
                else:
                    next_graph[i][j] = min(graph[i][j], dist_via)
        graph = next_graph

    for i in range(vertices_count):
        print(graph[i])


if __name__ == "__main__":
    fin = open(INP_FILE, "r")
    vertices_count = int(fin.readline().split()[0])

    graph = []
    for i in range(vertices_count):
        r = [None] * vertices_count
        row = fin.readline().split()
        pairs = int(row[0])
        row = row[1:]

        for j in range(pairs):
            neighbour = int(row[j*2]) - 1
            weight = int(row[j*2 + 1])
            r[neighbour] = weight

        r[i] = 0
        graph.append(r)

    fin.close()
    floyd_warshalls(graph, vertices_count)

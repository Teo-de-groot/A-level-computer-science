import math 
infinity = float('inf')
def create_adjacency_matrix(vertices, edges):
    matrix = [[infinity for _ in range(vertices)] for _ in range(vertices)]
    for i in range(vertices):
        matrix[i][i] = 0
    for u, v, w in edges:
        matrix[u][v] = w
        matrix[v][u] = w  # For undirected graph
    return matrix   

def dijkstra(adj_matrix, start):
    num_vertices = len(adj_matrix)
    visited = [False] * num_vertices
    distances = [infinity] * num_vertices
    distances[start] = 0

    for _ in range(num_vertices):
        min_distance = infinity
        min_index = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v

        visited[min_index] = True

        for v in range(num_vertices):
            if (adj_matrix[min_index][v] != infinity and
                    not visited[v] and
                    distances[min_index] + adj_matrix[min_index][v] < distances[v]):
                distances[v] = distances[min_index] + adj_matrix[min_index][v]

    return distances

def test():
    vertices = 5
    edges = [
        (0, 1, 10),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 1, 4),
        (2, 3, 8),
        (2, 4, 2),
        (3, 4, 7),
        (4, 3, 9)
    ]
    adj_matrix = create_adjacency_matrix(vertices, edges)
    start_vertex = 0
    distances = dijkstra(adj_matrix, start_vertex)
    print(f"Shortest distances from vertex {start_vertex}: {distances}")
test()
    
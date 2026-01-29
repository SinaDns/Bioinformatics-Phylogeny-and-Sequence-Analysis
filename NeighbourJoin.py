import numpy as np

dim = int(input())

matrix = [list(map(int, input().split())) for i in range(dim)]


def run_neighbor_joining(matrix, dim):
    matrix = np.array(matrix, dtype=float)
    clusters = list(range(dim))
    adj = [[] for _ in range(dim)]

    if dim <= 1:
        return adj

    while dim > 2:
        total_dist = np.sum(matrix, axis=0)
        D1 = (dim - 2) * matrix - total_dist - total_dist[:, None]
        np.fill_diagonal(D1, 0)

        min_idx = np.argmin(D1)
        i, j = divmod(min_idx, dim)

        delta = (total_dist[i] - total_dist[j]) / (dim - 2)
        li = (matrix[i, j] + delta) / 2
        lj = (matrix[i, j] - delta) / 2
        new_dist = (matrix[i, :] + matrix[j, :] - matrix[i, j]) / 2

        matrix = np.vstack((matrix, new_dist))
        matrix = np.hstack((matrix, np.append(new_dist, 0)[:, None]))
        matrix = np.delete(matrix, [i, j], axis=0)
        matrix = np.delete(matrix, [i, j], axis=1)

        new_cluster_idx = len(adj)
        adj.append([])
        adj[new_cluster_idx].append((clusters[i], li))
        adj[clusters[i]].append((new_cluster_idx, li))
        adj[new_cluster_idx].append((clusters[j], lj))
        adj[clusters[j]].append((new_cluster_idx, lj))

        clusters.pop(max(i, j))
        clusters.pop(min(i, j))
        clusters.append(new_cluster_idx)
        dim -= 1

    adj[clusters[0]].append((clusters[1], matrix[0, 1]))
    adj[clusters[1]].append((clusters[0], matrix[0, 1]))

    return adj


def print_graph(adj):
    for i, nodes in enumerate(adj):
        for neighbor, weight in nodes:
            print(f"{i}->{neighbor}:{weight:.3f}")


adj_list = run_neighbor_joining(matrix, dim)
print_graph(adj_list)
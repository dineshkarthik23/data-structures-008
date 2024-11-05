import math
import heapq
import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(matrix, vertices, mst_edges, title):
    G = nx.Graph()
    
    for i in range(vertices):
        for j in range(vertices):
            if matrix[i][j] != math.inf and matrix[i][j] != 0:
                G.add_edge(i, j, weight=matrix[i][j])

    layout = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    
    nx.draw_networkx_nodes(G, layout, node_size=700, node_color='lightblue')
    nx.draw_networkx_edges(G, layout, edgelist=G.edges(), width=2, edge_color='black')
    nx.draw_networkx_edge_labels(G, layout, edge_labels={(u, v): f'{G[u][v]["weight"]}' for u, v in G.edges()}, font_color='red')
    nx.draw_networkx_labels(G, layout, font_size=20, font_color="orange")
    nx.draw_networkx_edges(G, layout, edgelist=mst_edges, width=4, edge_color='red')

    plt.title(title)
    plt.show()

def prim_algo(matrix, vertices, start):
    mst_tree = []
    visited = set([start])
    graph_edges = [(matrix[start][i], start, i) for i in range(vertices) if matrix[start][i] != math.inf]
    heapq.heapify(graph_edges)

    while graph_edges:
        weight, node_from, node_to = heapq.heappop(graph_edges)
        if node_to not in visited:
            visited.add(node_to)
            mst_tree.append((node_from, node_to))

            for next_node in range(vertices):
                if matrix[node_to][next_node] != math.inf and next_node not in visited:
                    heapq.heappush(graph_edges, (matrix[node_to][next_node], node_to, next_node))

    return mst_tree

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find_root(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find_root(self.parent[element])
        return self.parent[element]

    def union_sets(self, set1, set2):
        root1 = self.find_root(set1)
        root2 = self.find_root(set2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_algo(matrix, vertices):
    graph_edges = []
    for i in range(vertices):
        for j in range(i + 1, vertices):
            if matrix[i][j] != math.inf:
                graph_edges.append((matrix[i][j], i, j))
    
    graph_edges.sort()

    disjoint_set = DisjointSet(vertices)
    mst_tree = []
    
    for weight, node_from, node_to in graph_edges:
        if disjoint_set.find_root(node_from) != disjoint_set.find_root(node_to):
            disjoint_set.union_sets(node_from, node_to)
            mst_tree.append((node_from, node_to))
            if len(mst_tree) == vertices - 1:
                break
    return mst_tree

def main_program():
    vertices = int(input("Enter the number of vertices: "))
    matrix = [[math.inf for _ in range(vertices)] for _ in range(vertices)]

    print("Provide the adjacency matrix values (use '0' for unreachable edges):")
    for i in range(vertices):
        for j in range(vertices):
            edge_val = int(input(f"Edge value from {i} to {j}: "))
            matrix[i][j] = edge_val if edge_val != 0 else math.inf

    while True:
        algo_choice = input("Choose algorithm (prim/kruskal) or type 'exit' to stop: ").lower()
        if algo_choice == 'exit':
            break
        
        if algo_choice == 'prim':
            start_vertex = int(input(f"Enter the starting vertex (0 to {vertices - 1}): "))
            mst_result_prim = prim_algo(matrix, vertices, start_vertex)
            print("MST (Prim's Algorithm):", mst_result_prim)
            draw_graph(matrix, vertices, mst_result_prim, "Prim's MST Visualization")

        elif algo_choice == 'kruskal':
            mst_result_kruskal = kruskal_algo(matrix, vertices)
            print("MST (Kruskal's Algorithm):", mst_result_kruskal)
            draw_graph(matrix, vertices, mst_result_kruskal, "Kruskal's MST Visualization")

        else:
            print("Invalid choice. Please enter 'prim' or 'kruskal'.")

if __name__ == "__main__":
    main_program()


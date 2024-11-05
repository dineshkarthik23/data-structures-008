import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(adj_matrix, start_node, total_nodes):
    visited = [False] * total_nodes
    nodes_queue = deque([start_node])
    visited[start_node] = True

    print("\nBFS Walk from vertex", start_node, ": ", end="")

    while nodes_queue:
        current_node = nodes_queue.popleft()
        print(current_node, end=" ")

        for neighbor in range(total_nodes):
            if adj_matrix[current_node][neighbor] != 0 and not visited[neighbor]:
                nodes_queue.append(neighbor)
                visited[neighbor] = True
    print()

def dfs_recursive(adj_matrix, node, visited, total_nodes):
    visited[node] = True
    print(node, end=" ")

    for adjacent in range(total_nodes):
        if adj_matrix[node][adjacent] != 0 and not visited[adjacent]:
            dfs_recursive(adj_matrix, adjacent, visited, total_nodes)

def dfs(adj_matrix, start_node, total_nodes):
    visited = [False] * total_nodes
    print("\nDFS Walk from vertex", start_node, ": ", end="")
    dfs_recursive(adj_matrix, start_node, visited, total_nodes)
    print()

def draw_directed_graph(adj_matrix, total_nodes):
    graph = nx.DiGraph()
    for i in range(total_nodes):
        for j in range(total_nodes):
            if adj_matrix[i][j] != 0:
                graph.add_edge(i, j, weight=adj_matrix[i][j])

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold', arrows=True)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Directed Graph Display")
    plt.show()

node_count = int(input("Enter the number of vertices: "))
adj_matrix = [[0 for _ in range(node_count)] for _ in range(node_count)]

print("Enter the adjacency matrix values:")
for i in range(node_count):
    for j in range(node_count):
        adj_matrix[i][j] = int(input(f"Edge from {i} to {j}: "))

while True:
    start_node = input("Enter the source vertex (or type 'exit' to stop): ").lower()
    if start_node == 'exit':
        break
    try:
        start_node = int(start_node)
        if 0 <= start_node < node_count:
            bfs(adj_matrix, start_node, node_count)
            dfs(adj_matrix, start_node, node_count)
            draw_directed_graph(adj_matrix, node_count)
        else:
            print(f"Invalid vertex. Please enter a value between 0 and {node_count - 1}.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit' to stop.")

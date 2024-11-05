import math
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def calculate_shortest_paths(matrix, num_vertices, target_vertex):
    distances = [math.inf] * num_vertices
    distances[target_vertex] = 0  
    priority_queue = [(0, target_vertex)]  

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)
        if current_distance > distances[node]:
            continue

        for neighbor in range(num_vertices):
            edge_weight = matrix[neighbor][node]
            if edge_weight != math.inf and distances[neighbor] > current_distance + edge_weight:
                distances[neighbor] = current_distance + edge_weight
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))

    return distances

def visualize_original_graph(matrix, num_vertices):
    G = nx.DiGraph()  

    for src in range(num_vertices):
        for dest in range(num_vertices):
            if matrix[src][dest] != 0 and matrix[src][dest] != math.inf:
                G.add_edge(src, dest, weight=matrix[src][dest])

    labels = {(src, dest): matrix[src][dest] for src in range(num_vertices) for dest in range(num_vertices) 
              if matrix[src][dest] != 0 and matrix[src][dest] != math.inf}

    layout = nx.spring_layout(G)  
    nx.draw(G, layout, with_labels=True, node_color='skyblue', node_size=2500, font_size=10, 
            font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, layout, edge_labels=labels)
    
    plt.title("Graph Representation")
    plt.show()

def visualize_shortest_paths(matrix, num_vertices, target_vertex, distances):
    G = nx.DiGraph()

    for src in range(num_vertices):
        for dest in range(num_vertices):
            if matrix[src][dest] != 0 and matrix[src][dest] != math.inf:
                G.add_edge(src, dest, weight=matrix[src][dest])

    labels = {(src, dest): matrix[src][dest] for src in range(num_vertices) for dest in range(num_vertices) 
              if matrix[src][dest] != 0 and matrix[src][dest] != math.inf}

    layout = nx.spring_layout(G)
    nx.draw(G, layout, with_labels=True, node_color='lightgreen', node_size=2500, font_size=10, 
            font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, layout, edge_labels=labels)

    for src in range(num_vertices):
        if distances[src] != math.inf and src != target_vertex:
            for dest in range(num_vertices):
                # Corrected: Checking if the edge is part of the shortest path
                if matrix[dest][src] != 0 and matrix[dest][src] != math.inf and distances[dest] + matrix[dest][src] == distances[src]:
                    nx.draw_networkx_edges(G, layout, edgelist=[(dest, src)], edge_color='red', width=2)

    plt.title(f"Shortest Paths to Vertex {target_vertex}")
    plt.show()

# Input section
num_vertices = int(input("Enter the number of vertices: "))
adj_matrix = [[math.inf for _ in range(num_vertices)] for _ in range(num_vertices)]

print("Provide the adjacency matrix values (use '0' for unreachable edges):")
for i in range(num_vertices):
    for j in range(num_vertices):
        edge_value = int(input(f"Edge value from {i} to {j}: "))
        adj_matrix[i][j] = edge_value if edge_value != 0 else math.inf

visualize_original_graph(adj_matrix, num_vertices)

while True:
    target_input = input("Enter the destination vertex (or type 'exit' to stop): ").lower()
    if target_input == 'exit':
        break

    try:
        target_vertex = int(target_input)
        if 0 <= target_vertex < num_vertices:
            shortest_distances = calculate_shortest_paths(adj_matrix, num_vertices, target_vertex)

            print(f"\nShortest paths to vertex {target_vertex}:")
            for vertex in range(num_vertices):
                if shortest_distances[vertex] != math.inf:
                    print(f"From vertex {vertex} to {target_vertex}: Distance = {shortest_distances[vertex]}")
                else:
                    print(f"From vertex {vertex} to {target_vertex}: No reachable path")

            visualize_shortest_paths(adj_matrix, num_vertices, target_vertex, shortest_distances)
        else:
            print(f"Invalid vertex. Please enter a valid vertex index between 0 and {num_vertices - 1}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit' to stop.")

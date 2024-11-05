import sys
import matplotlib.pyplot as plt
import numpy as np

def min_dance(distances, s_set, V):
    min_value = sys.maxsize
    min_index = -1
    for v in range(V):
        if distances[v] < min_value and not s_set[v]:
            min_value = distances[v]
            min_index = v
    return min_index

def dijkstra(graph, src, V):
    distances = [sys.maxsize] * V
    distances[src] = 0
    s_set = [False] * V
    for _ in range(V):
        u = min_dance(distances, s_set, V)
        s_set[u] = True

        for v in range(V):
            if (graph[u][v] and not s_set[v] and distances[u] != sys.maxsize and
                distances[u] + graph[u][v] < distances[v]):
                distances[v] = distances[u] + graph[u][v]

    print("\nVertex \t Distance from Source")
    for i in range(V):
        print(i, "\t", distances[i])

def visualize_graph_matplotlib(graph, V):
    fig, ax = plt.subplots()
    ax.set_title("Graph Visualization")

    angles = np.linspace(0, 2 * np.pi, V, endpoint=False).tolist()
    node_positions = {i: (np.cos(angle), np.sin(angle)) for i, angle in enumerate(angles)}

    for i, (x, y) in node_positions.items():
        ax.plot(x, y, 'o', color='lightblue', markersize=20)
        ax.text(x, y, str(i), color='black', fontsize=12, ha='center', va='center')

    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                start = node_positions[i]
                end = node_positions[j]
                ax.annotate("",
                            xy=end, xycoords='data',
                            xytext=start, textcoords='data',
                            arrowprops=dict(arrowstyle="->", lw=1.5, color="gray"))
                weight_position = (0.5 * (start[0] + end[0]), 0.5 * (start[1] + end[1]))
                ax.text(weight_position[0], weight_position[1], str(graph[i][j]),
                        color='red', fontsize=10)

    ax.set_axis_off()
    plt.show()

n = int(input("Enter the number of vertices (n): "))
graph = [[0 for _ in range(n)] for _ in range(n)]
print("Enter the adjacency matrix values:")
for i in range(n):
    for j in range(n):
        graph[i][j] = int(input(f"Enter value for edge from {i} to {j}: "))

visualize_graph_matplotlib(graph, n)

while True:
    src_input = input("Enter the source vertex (type 'exit' to exit): ")
    if src_input.lower() == 'exit':
        break
    try:
        src = int(src_input)
        if 0 <= src < n:
            dijkstra(graph, src, n)
        else:
            print(f"Invalid source vertex. Please enter a valid vertex between 0 and {n-1}.")
    except ValueError:
        print("Invalid input. Please enter a valid vertex number or 'exit' to exit.")

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:43:31 2024

@author: dheen
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def floyd(graph, V):

    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    print("\nShortest distances between every pair of vertices:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == math.inf:
                print("INF", end=" ")
            else:
                print(f"{dist[i][j]:3}", end=" ")
        print()

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
            if graph[i][j] != 0 and graph[i][j] != math.inf:
                start = node_positions[i]
                end = node_positions[j]
                ax.annotate("",
                            xy=end, xycoords='data',
                            xytext=start, textcoords='data',
                            arrowprops=dict(arrowstyle="->", lw=1.5, color="gray"))
                weight_position = (0.5 * (start[0] + end[0]), 0.5 * (start[1] + end[1]))
                ax.text(weight_position[0], weight_position[1], str(graph[i][j]), color='red', fontsize=10)

    ax.set_axis_off()
    plt.show()

n = int(input("Enter the number of vertices (n): "))
graph = [[0 for _ in range(n)] for _ in range(n)]
print("Enter the adjacency matrix values (use 0 for non-reachable edges):")
for i in range(n):
    for j in range(n):
        value = int(input(f"Enter value for edge from {i} to {j}: "))
        if i != j and value == 0:
            graph[i][j] = math.inf  # No path from i to j
        else:
            graph[i][j] = value

visualize_graph_matplotlib(graph, n)

floyd(graph, n)

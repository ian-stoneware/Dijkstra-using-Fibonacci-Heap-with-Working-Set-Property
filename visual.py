import matplotlib.pyplot as plt
import networkx as nx


# Dijkstra with Labels implementation
def dijkstra_with_labels(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    distance[start] = 0
    used = [False] * n
    predecessor = [-1] * n  # Track predecessors

    for _ in range(n):
        v = None
        for j in range(n):
            if not used[j] and (v is None or distance[j] < distance[v]):
                v = j
        if distance[v] == float('inf'):
            break
        used[v] = True

        for edge, weight in graph[v]:
            if distance[v] + weight < distance[edge]:
                distance[edge] = distance[v] + weight
                predecessor[edge] = v

    return distance, predecessor


# Visualization function
def visualize_graph_to_file(graph, shortest_path=None, file_name="graph.png"):
    '''
    Visualizes the graph and saves it as an image file.

    Parameters:
    - graph: dict representation of the graph
    - shortest_path: List of nodes in the shortest path (optional)
    - file_name: Name of the file to save the image
    '''
    # Create a NetworkX graph
    G = nx.Graph()
    for u, neighbors in graph.items():
        for v, weight in neighbors.items():
            G.add_edge(u, v, weight=weight)

    # Position nodes using spring layout
    pos = nx.spring_layout(G, seed=42)

    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Highlight shortest path
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='orange', node_size=800)

    # Save the plot as an image
    plt.title("Graph Visualization with Shortest Path Highlighted")
    plt.savefig(file_name, format="png")
    plt.close()
    print(f"Graph saved as {file_name}")


# Main example
if __name__ == "__main__":
    # Define the graph in adjacency list format
    example_graph = [
        [(1, 4), (2, 2)],  # Node 0 connects to Node 1 (weight 4), Node 2 (weight 2)
        [(2, 5), (3, 10)],  # Node 1 connects to Node 2 (weight 5), Node 3 (weight 10)
        [(4, 3)],  # Node 2 connects to Node 4 (weight 3)
        [(5, 11)],  # Node 3 connects to Node 5 (weight 11)
        [(3, 4), (5, 8)],  # Node 4 connects to Node 3 (weight 4), Node 5 (weight 8)
        []  # Node 5 has no outgoing edges
    ]

    # Convert example_graph to dict for visualization
    graph_dict = {i: {neighbor: weight for neighbor, weight in neighbors} for i, neighbors in enumerate(example_graph)}

    # Run Dijkstra's algorithm
    source = 0
    distances_labels, predecessors = dijkstra_with_labels(example_graph, source)

    print("Shortest distances (Labels):", distances_labels)

    # Reconstruct shortest path to a specific destination (e.g., Node 5)
    destination = 5
    shortest_path = []
    while destination != -1:
        shortest_path.append(destination)
        destination = predecessors[destination]
    shortest_path.reverse()

    print("Shortest path from Node 0 to Node 5:", shortest_path)

    # Visualize and save the graph
    visualize_graph_to_file(graph_dict, shortest_path=shortest_path, file_name="shortest_path_graph.png")

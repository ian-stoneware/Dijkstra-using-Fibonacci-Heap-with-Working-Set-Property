import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Generate a simple weighted graph
def get_random_simple_Gnp_graph(n, seed=42):
    edge_p = 1 / 2  # Probability of an edge between vertices
    g = nx.random_graphs.fast_gnp_random_graph(n, edge_p, seed)
    return nx.convert.to_dict_of_lists(g)


def generate_graph(number_of_vertex, max_weight=10, min_weight=1):
    graph_without_weights = get_random_simple_Gnp_graph(number_of_vertex)
    weighted_graph = {}

    for node in graph_without_weights:
        for neighbor in graph_without_weights[node]:
            if node < neighbor:  # Avoid duplicate edges
                weight = random.randint(min_weight, max_weight)
                weighted_graph.setdefault(node, []).append((neighbor, weight))
                weighted_graph.setdefault(neighbor, []).append((node, weight))

    return weighted_graph


# Dijkstra's Algorithm (Labels)
def dijkstra_with_labels(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    distance[start] = 0
    used = [False] * n
    steps = []

    for _ in range(n):
        v = None
        for j in range(n):
            if not used[j] and (v is None or distance[j] < distance[v]):
                v = j

        if v is None or distance[v] == float('inf'):
            break

        used[v] = True
        steps.append((v, distance[:]))  # Save the state (node, distances)

        for neighbor, weight in graph[v]:
            if distance[v] + weight < distance[neighbor]:
                distance[neighbor] = distance[v] + weight

    return distance, steps


# Animate the process of Dijkstra's algorithm
def update(step, graph, pos, ax, nx_graph):
    ax.clear()  # Clear the previous frame
    nx.draw(nx_graph, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, ax=ax)

    # Add edge labels (weights) to the graph
    edge_labels = {}
    for u in range(len(graph)):
        for v, weight in graph[u]:
            edge_labels[(u, v)] = weight

    # Draw the edge labels (weights)
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_size=8, ax=ax)

    current_distances = step[1]

    # Highlight the shortest path edges in red
    for u in range(len(current_distances)):
        if current_distances[u] < float('inf'):
            for v, weight in graph[u]:
                if current_distances[u] + weight == current_distances[v]:
                    nx.draw_networkx_edges(nx_graph, pos, edgelist=[(u, v)], edge_color='red', width=2, ax=ax)

    # Highlight the current node in orange
    v, _ = step
    nx.draw_networkx_nodes(nx_graph, pos, nodelist=[v], node_color='orange', node_size=800, ax=ax)


def animate_dijkstra(graph_dict, steps, file_name="dijkstra_animation.gif"):
    # Convert the graph dictionary to a NetworkX graph
    G = nx.Graph()
    for node in graph_dict:
        for neighbor, weight in graph_dict[node]:
            G.add_edge(node, neighbor, weight=weight)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Positioning the nodes

    ani = animation.FuncAnimation(fig, update, frames=steps, fargs=(graph_dict, pos, ax, G), repeat=False, interval=1000)
    ani.save(file_name, writer='pillow', fps=1)


# Main script execution
example_graph = generate_graph(6)  # Generate a graph with 6 nodes

# Print the generated graph for debugging
print("Generated Graph:", example_graph)

# Run Dijkstra's Algorithm
source = 0
distances_labels, steps = dijkstra_with_labels(example_graph, source)

# Print shortest distances
print("Shortest distances (Labels):", distances_labels)

# Visualize the animation
animate_dijkstra(example_graph, steps, file_name="dijkstra_animation.gif")

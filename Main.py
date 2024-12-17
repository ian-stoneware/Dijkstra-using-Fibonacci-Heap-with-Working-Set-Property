import pandas as pd
import time

from src.Dijkstra import dijkstra_with_labels, dijkstra_fibonacci_heap, dijkstra_working_set_heap
from src.Graph import generate_graph
from src.Statistic import collect_statistics, plot_results

# Update this line to handle all three results
labels_result, heap_result, working_set_result = collect_statistics(100, 1000, 100, 10)
plot_results(labels_result, heap_result, working_set_result)
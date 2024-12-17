import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from src.Dijkstra import dijkstra_with_labels, dijkstra_fibonacci_heap, dijkstra_working_set_heap
from src.Graph import generate_graph

sns.set_theme()


def collect_statistics(start_nodes, end_nodes, step, retry=1):
    '''The function runs two variation of Dijkstra algoritms and returns statistic of runs'''
    columns = ['Nodes', 'Time']

    labels_result = pd.DataFrame(columns=columns)
    heap_result = pd.DataFrame(columns=columns)
    working_set_result = pd.DataFrame(columns=columns)

    for _ in range(retry):
        for n in range(start_nodes, end_nodes, step):
            g = generate_graph(n)

            labels_start = time.time()
            labels = dijkstra_with_labels(g, 0)
            labels_res = (time.time() - labels_start)

            heap_start = time.time()
            fib_heap = dijkstra_fibonacci_heap(g, 0)
            heap_res = (time.time() - heap_start)

            # Run Dijkstra with Working Set Heap
            working_set_start = time.time()
            working_set_heap = dijkstra_working_set_heap(g, 0)  # Assuming this function is implemented
            working_set_res = time.time() - working_set_start

            if labels != fib_heap:
                assert AssertionError(
                    "The results of the algorithms do not match"
                )

            labels_result.loc[len(labels_result.index)] = [n, labels_res]
            heap_result.loc[len(heap_result.index)] = [n, heap_res]
            working_set_result.loc[len(working_set_result)] = [n, working_set_res]

    labels_result = labels_result.groupby(by=columns[0]).mean().reset_index()
    heap_result = heap_result.groupby(by=columns[0]).mean().reset_index()
    working_set_result = working_set_result.groupby(by=columns[0]).mean().reset_index()

    return labels_result, heap_result, working_set_result


def plot_results(data1, data2, data3, legend=['Naive', 'Fibonnacci heap', 'WorkingSet Heap'], xlabel='Number of nodes', ylabel='Time'):

    plt.plot(data1[data1.columns[0]],
             data1[data1.columns[1]], 'r')

    plt.plot(data2[data2.columns[0]],
             data2[data2.columns[1]], 'b')

    plt.plot(data3[data3.columns[0]],
             data3[data3.columns[1]], 'g')

    plt.legend(legend)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

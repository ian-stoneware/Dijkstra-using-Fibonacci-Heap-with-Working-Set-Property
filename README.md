# Dijkstra using Fibonacci Heap with Working Set Property

## Description
This project implements Dijkstra's algorithm for finding the shortest path in a weighted graph. It includes both the naive approach, an optimized version using a Fibonacci heap and another optimized version using a Fibonacci heap with Working Set Property.
Dijkstra’s Algorithm:
- 1.	Naïve Implementation: A simple array-based approach.
- 2.	Fibonacci Heap Optimization: An advanced implementation using a Fibonacci Heap to improve efficiency.
- 3.	Fibonacci Heap with Working Set Property: A further optimization leveraging the locality of reference.


## Installation
To use this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ian-stoneware/Dijkstra-using-Fibonacci-Heap-with-Working-Set-Property.git
   
   cd dijkstra-algorithm
   
2. Run main.py to get the time comsuming comparison:
   ```bash
   python main.py

4. Run animation.py to get the animation of how a Dijkstra Algorithm to get the shortest path:
   ```bash
   python animation.py

6. Run visual.py to get the result of how a Dijkstra Algorithm to get the shortest path:
   ```bash
   python visual.py

## Results
The performance comparisons are make with nodes numbers range from 100 to 1000 and 500 to 5000.
<img src="https://github.com/ian-stoneware/Dijkstra-using-Fibonacci-Heap-with-Working-Set-Property/blob/main/comparison.jpg" width="800">
<img src="https://github.com/ian-stoneware/Dijkstra-using-Fibonacci-Heap-with-Working-Set-Property/blob/main/comparison5000.jpg" width="800">

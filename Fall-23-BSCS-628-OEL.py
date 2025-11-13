# ---------------------------------------------------------------
# Smart Campus Path Finder
# Author: Agent
# Date: Auto-recorded (program runtime)
# ---------------------------------------------------------------
# This program helps find paths between locations in a campus
# using BFS, DFS, and Uniform Cost Search algorithms.
# ---------------------------------------------------------------

import heapq
import time
from datetime import datetime

# ---------------------------------------------------------------
# Graph class - represents the campus as a graph
# ---------------------------------------------------------------
class Graph:
    def __init__(self):  # ✅ fixed (was _init_)
        self.graph = {}  # Dictionary to store adjacency list

    def add_location(self, location):
        """Add a new location (node) to the campus graph"""
        if location not in self.graph:
            self.graph[location] = {}

    def add_path(self, src, dest, cost):
        """Add a path (edge) between two locations with given cost"""
        self.add_location(src)
        self.add_location(dest)
        self.graph[src][dest] = cost
        self.graph[dest][src] = cost  # Undirected graph

    def get_neighbors(self, node):
        """Return all connected locations"""
        return self.graph.get(node, {})

# ---------------------------------------------------------------
# Breadth-First Search (BFS)
# ---------------------------------------------------------------
def bfs(graph, start, goal, depth_limit=None):
    visited = []
    queue = [(start, [start])]
    expanded_count = 0
    while queue:
        (vertex, path) = queue.pop(0)
        expanded_count += 1

        if vertex not in visited:
            visited.append(vertex)
            if vertex == goal:
                return expanded_count, visited, path
            
            if depth_limit and len(path) > depth_limit:
                continue
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return expanded_count, visited, []

# ---------------------------------------------------------------
# Depth-First Search (DFS)
# ---------------------------------------------------------------
def dfs(graph, start, goal, depth_limit=None):
    visited = []
    stack = [(start, [start])]
    expanded_count = 0
    while stack:
        (vertex, path) = stack.pop()
        expanded_count += 1

        if vertex not in visited:
            visited.append(vertex)
            if vertex == goal:
                return expanded_count, visited, path
            
            if depth_limit and len(path) > depth_limit:
                continue
            
            for neighbor in sorted(graph.get_neighbors(vertex), reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return expanded_count, visited, []

# ---------------------------------------------------------------
# Uniform Cost Search (UCS)
# ---------------------------------------------------------------
def ucs(graph, start, goal, cost_limit=None):
    visited = []
    queue = [(0, start, [start])]
    heapq.heapify(queue)
    expanded_count = 0
    while queue:
        (cost, vertex, path) = heapq.heappop(queue)
        expanded_count += 1

        if vertex not in visited:
            visited.append(vertex)
            if vertex == goal:
                return expanded_count, visited, path, cost
            
            if cost_limit and cost > cost_limit:
                continue
            
            for neighbor, edge_cost in graph.get_neighbors(vertex).items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))
    return expanded_count, visited, [], float('inf')

# ---------------------------------------------------------------
# Save traversal history to a text file
# ---------------------------------------------------------------
def save_history(username, algorithm, visited, path, cost, expanded_count):
    with open("path_history.txt", "a") as file:
        file.write(f"\nUser: {username}\n")
        file.write(f"Date/Time: {datetime.now()}\n")
        file.write(f"Algorithm: {algorithm}\n")
        file.write(f"Expanded Nodes: {expanded_count}\n")
        file.write(f"Visited Nodes: {visited}\n")
        file.write(f"Shortest Path: {path}\n")
        file.write(f"Total Cost: {cost}\n")
        file.write("-" * 50 + "\n")

# ---------------------------------------------------------------
# Compare Algorithms by Time and Cost
# ---------------------------------------------------------------
def compare_algorithms(graph, start, goal):
    print("\n=== Algorithm Comparison ===")

    start_time = time.time()
    bfs_expanded, bfs_visited, bfs_path = bfs(graph, start, goal)
    bfs_time = time.time() - start_time
    print(f"BFS -> Path: {bfs_path}, Time: {bfs_time:.6f}s, Expanded Nodes: {bfs_expanded}")

    start_time = time.time()
    dfs_expanded, dfs_visited, dfs_path = dfs(graph, start, goal)
    dfs_time = time.time() - start_time
    print(f"DFS -> Path: {dfs_path}, Time: {dfs_time:.6f}s, Expanded Nodes: {dfs_expanded}")

    start_time = time.time()
    ucs_expanded, ucs_visited, ucs_path, ucs_cost = ucs(graph, start, goal)
    ucs_time = time.time() - start_time
    print(f"UCS -> Path: {ucs_path}, Cost: {ucs_cost}, Time: {ucs_time:.6f}s, Expanded Nodes: {ucs_expanded}")

    print("\n--- Summary of Expanded Nodes ---")
    print(f"BFS expanded: {bfs_expanded} nodes")
    print(f"DFS expanded: {dfs_expanded} nodes")
    print(f"UCS expanded: {ucs_expanded} nodes")

# ---------------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------------
def main():
    g = Graph()
    username = input("Enter your name: ")

    g.add_path("Gate", "Library", 2)
    g.add_path("Gate", "Cafeteria", 4)
    g.add_path("Library", "Lab", 3)
    g.add_path("Lab", "Admin", 6)
    g.add_path("Cafeteria", "Admin", 5)
    g.add_path("Library", "Admin", 10)

    while True:
        print("\n--- Smart Campus Path Finder ---")
        print("1. Add Location/Path")
        print("2. Find Path (BFS / DFS / UCS)")
        print("3. Compare Algorithms")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            src = input("Enter source location: ")
            dest = input("Enter destination location: ")
            try:
                cost = int(input("Enter cost/distance: "))
                g.add_path(src, dest, cost)
                print("Path added successfully!")
            except ValueError:
                print("Invalid cost. Must be a number.")

        elif choice == "2":
            start = input("Enter start location: ")
            goal = input("Enter destination: ")
            algo = input("Choose algorithm (bfs/dfs/ucs): ").lower()

            if algo == "bfs":
                expanded_count, visited, path = bfs(g, start, goal)
                print("Visited order:", visited)
                print("Path found:", path)
                print("Nodes expanded:", expanded_count)
                save_history(username, "BFS", visited, path, "N/A", expanded_count)

            elif algo == "dfs":
                expanded_count, visited, path = dfs(g, start, goal)
                print("Visited order:", visited)
                print("Path found:", path)
                print("Nodes expanded:", expanded_count)
                save_history(username, "DFS", visited, path, "N/A", expanded_count)

            elif algo == "ucs":
                expanded_count, visited, path, cost = ucs(g, start, goal)
                print("Visited order:", visited)
                print("Path found:", path)
                print("Total cost:", cost)
                print("Nodes expanded:", expanded_count)
                save_history(username, "UCS", visited, path, cost, expanded_count)

            else:
                print("Invalid algorithm choice!")

        elif choice == "3":
            start = input("Enter start location: ")
            goal = input("Enter destination: ")
            compare_algorithms(g, start, goal)

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

# ---------------------------------------------------------------
if __name__ == "__main__":  # ✅ fixed (was _name_ and _main_)
    main()

# ═══════════════════════════════════════════════════════════════════════════
# 🏫 SMART CAMPUS PATH FINDER
# ═══════════════════════════════════════════════════════════════════════════
# A comprehensive path-finding system for smart campus navigation using
# BFS, DFS, and UCS algorithms with performance comparison and history logging.
# ═══════════════════════════════════════════════════════════════════════════

from collections import deque
import heapq
import time
from datetime import datetime


# ═══════════════════════════════════════════════════════════════════════════
# GRAPH DATA STRUCTURE CLASS
# ═══════════════════════════════════════════════════════════════════════════

class CampusGraph:
    """
    Represents the campus as a weighted graph using adjacency list.
    Nodes represent locations and edges represent paths with weights (distances/costs).
    """
    
    def __init__(self):
        """Initialize an empty graph using dictionary for adjacency list."""
        self.graph = {}
    
    def add_location(self, location):
        """
        Add a new location (node) to the campus graph.
        
        Args:
            location (str): Name of the location to add
        
        Returns:
            str: Success or error message
        """
        if location in self.graph:
            return f"❌ Location '{location}' already exists!"
        self.graph[location] = {}
        return f"✅ Location '{location}' added successfully!"
    
    def remove_location(self, location):
        """
        Remove a location (node) from the campus graph.
        Also removes all edges connected to this location.
        
        Args:
            location (str): Name of the location to remove
        
        Returns:
            str: Success or error message
        """
        if location not in self.graph:
            return f"❌ Location '{location}' does not exist!"
        
        # Remove the location itself
        del self.graph[location]
        
        # Remove all edges pointing to this location
        for loc in self.graph:
            if location in self.graph[loc]:
                del self.graph[loc][location]
        
        return f"✅ Location '{location}' removed successfully!"
    
    def add_connection(self, from_loc, to_loc, weight):
        """
        Add a bidirectional connection (edge) between two locations with a weight.
        
        Args:
            from_loc (str): Starting location
            to_loc (str): Destination location
            weight (int/float): Cost/distance of the path
        
        Returns:
            str: Success or error message
        """
        if from_loc not in self.graph:
            return f"❌ Location '{from_loc}' does not exist!"
        if to_loc not in self.graph:
            return f"❌ Location '{to_loc}' does not exist!"
        
        # Add bidirectional edge
        self.graph[from_loc][to_loc] = weight
        self.graph[to_loc][from_loc] = weight
        
        return f"✅ Connection added: {from_loc} ↔ {to_loc} (Cost: {weight})"
    
    def remove_connection(self, from_loc, to_loc):
        """
        Remove a bidirectional connection (edge) between two locations.
        
        Args:
            from_loc (str): First location
            to_loc (str): Second location
        
        Returns:
            str: Success or error message
        """
        if from_loc not in self.graph or to_loc not in self.graph:
            return f"❌ One or both locations do not exist!"
        
        if to_loc not in self.graph[from_loc]:
            return f"❌ No connection exists between '{from_loc}' and '{to_loc}'!"
        
        # Remove bidirectional edge
        del self.graph[from_loc][to_loc]
        del self.graph[to_loc][from_loc]
        
        return f"✅ Connection removed: {from_loc} ↔ {to_loc}"
    
    def display_graph(self):
        """
        Display the entire campus graph with all locations and connections.
        """
        if not self.graph:
            print("📍 Campus map is empty!")
            return
        
        print("\n" + "=" * 60)
        print("🗺️  CAMPUS MAP - All Locations and Connections")
        print("=" * 60)
        
        for location in sorted(self.graph.keys()):
            connections = self.graph[location]
            if connections:
                print(f"\n📍 {location}:")
                for neighbor, weight in sorted(connections.items()):
                    print(f"   → {neighbor} (Cost: {weight})")
            else:
                print(f"\n📍 {location}: (No connections)")
        print("=" * 60)


# ═══════════════════════════════════════════════════════════════════════════
# BREADTH-FIRST SEARCH (BFS) ALGORITHM
# ═══════════════════════════════════════════════════════════════════════════

def bfs_search(graph, start, goal):
    """
    Breadth-First Search: Explores nodes level by level using a queue.
    Guarantees shortest path in terms of number of edges (unweighted).
    
    Args:
        graph (dict): The campus graph
        start (str): Starting location
        goal (str): Destination location
    
    Returns:
        tuple: (path, visited_nodes, nodes_visited_count)
    """
    # Check if start and goal exist
    if start not in graph:
        return None, [], 0
    if goal not in graph:
        return None, [], 0
    
    # Initialize queue with starting path and visited set
    queue = deque([[start]])
    visited = set()
    visited_order = []  # Track order of visits
    nodes_visited = 0
    
    # BFS main loop
    while queue:
        # Dequeue the first path
        path = queue.popleft()
        node = path[-1]
        
        # Check if we reached the goal
        if node == goal:
            return path, visited_order, nodes_visited
        
        # Process node if not visited
        if node not in visited:
            visited.add(node)
            visited_order.append(node)
            nodes_visited += 1
            
            # Add all neighbors to queue
            for neighbor in sorted(graph[node].keys()):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append(new_path)
    
    # No path found
    return None, visited_order, nodes_visited


# ═══════════════════════════════════════════════════════════════════════════
# DEPTH-FIRST SEARCH (DFS) ALGORITHM WITH DEPTH CONSTRAINT
# ═══════════════════════════════════════════════════════════════════════════

def dfs_search(graph, start, goal, max_depth=None):
    """
    Depth-First Search: Explores as far as possible along each branch using a stack.
    Includes optional depth constraint for limited exploration.
    
    Args:
        graph (dict): The campus graph
        start (str): Starting location
        goal (str): Destination location
        max_depth (int, optional): Maximum depth to explore
    
    Returns:
        tuple: (path, visited_nodes, nodes_visited_count)
    """
    # Check if start and goal exist
    if start not in graph:
        return None, [], 0
    if goal not in graph:
        return None, [], 0
    
    # Initialize stack with starting path and visited set
    stack = [[start]]
    visited = set()
    visited_order = []  # Track order of visits
    nodes_visited = 0
    
    # DFS main loop
    while stack:
        # Pop the last path (LIFO - stack behavior)
        path = stack.pop()
        node = path[-1]
        
        # Check depth constraint
        if max_depth is not None and len(path) > max_depth:
            continue
        
        # Check if we reached the goal
        if node == goal:
            return path, visited_order, nodes_visited
        
        # Process node if not visited
        if node not in visited:
            visited.add(node)
            visited_order.append(node)
            nodes_visited += 1
            
            # Add all neighbors to stack (in reverse order for consistent behavior)
            for neighbor in sorted(graph[node].keys(), reverse=True):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append(new_path)
    
    # No path found
    return None, visited_order, nodes_visited


# ═══════════════════════════════════════════════════════════════════════════
# UNIFORM COST SEARCH (UCS) ALGORITHM WITH COST CONSTRAINT
# ═══════════════════════════════════════════════════════════════════════════

def ucs_search(graph, start, goal, max_cost=None):
    """
    Uniform Cost Search: Explores nodes based on lowest cumulative cost using priority queue.
    Guarantees shortest path in terms of total edge weights (weighted).
    
    Args:
        graph (dict): The campus graph
        start (str): Starting location
        goal (str): Destination location
        max_cost (int/float, optional): Maximum cost limit
    
    Returns:
        tuple: (path, total_cost, visited_nodes, nodes_visited_count)
    """
    # Check if start and goal exist
    if start not in graph:
        return None, float('inf'), [], 0
    if goal not in graph:
        return None, float('inf'), [], 0
    
    # Initialize priority queue with (cost, path)
    # heapq maintains min-heap property
    pq = [(0, [start])]
    visited = set()
    visited_order = []  # Track order of visits
    nodes_visited = 0
    
    # UCS main loop
    while pq:
        # Pop path with lowest cost
        cost, path = heapq.heappop(pq)
        node = path[-1]
        
        # Check cost constraint
        if max_cost is not None and cost > max_cost:
            continue
        
        # Check if we reached the goal
        if node == goal:
            return path, cost, visited_order, nodes_visited
        
        # Process node if not visited
        if node not in visited:
            visited.add(node)
            visited_order.append(node)
            nodes_visited += 1
            
            # Add all neighbors to priority queue with updated cost
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    new_cost = cost + weight
                    # Only add if within cost constraint
                    if max_cost is None or new_cost <= max_cost:
                        new_path = path + [neighbor]
                        heapq.heappush(pq, (new_cost, new_path))
    
    # No path found
    return None, float('inf'), visited_order, nodes_visited


# ═══════════════════════════════════════════════════════════════════════════
# HISTORY LOGGING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def save_traversal_history(user_name, algorithm, start, goal, path, cost, visited, time_taken, nodes_visited):
    """
    Save traversal results to a text file for record keeping.
    
    Args:
        user_name (str): Name of the user
        algorithm (str): Algorithm used (BFS/DFS/UCS)
        start (str): Starting location
        goal (str): Destination location
        path (list): Path found
        cost (float): Total cost (for UCS)
        visited (list): Order of nodes visited
        time_taken (float): Execution time in seconds
        nodes_visited (int): Number of nodes visited
    """
    try:
        with open("traversal_history.txt", "a") as file:
            file.write("\n" + "=" * 80 + "\n")
            file.write(f"📅 Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"👤 User: {user_name}\n")
            file.write(f"🔍 Algorithm: {algorithm}\n")
            file.write(f"🎯 Route: {start} → {goal}\n")
            file.write(f"📊 Nodes Visited: {nodes_visited}\n")
            file.write(f"🗺️  Traversal Order: {' → '.join(visited) if visited else 'N/A'}\n")
            
            if path:
                file.write(f"✅ Path Found: {' → '.join(path)}\n")
                if algorithm == "UCS":
                    file.write(f"💰 Total Cost: {cost}\n")
            else:
                file.write(f"❌ No Path Found\n")
            
            file.write(f"⏱️  Execution Time: {time_taken:.6f} seconds\n")
            file.write("=" * 80 + "\n")
    except Exception as e:
        print(f"⚠️  Error saving history: {e}")


# ═══════════════════════════════════════════════════════════════════════════
# PATH FINDING AND COMPARISON
# ═══════════════════════════════════════════════════════════════════════════

def find_and_compare_paths(campus, start, goal, user_name, dfs_depth=None, ucs_cost_limit=None):
    """
    Run all three algorithms (BFS, DFS, UCS) and compare their performance.
    
    Args:
        campus (CampusGraph): The campus graph object
        start (str): Starting location
        goal (str): Destination location
        user_name (str): Name of the user
        dfs_depth (int, optional): Depth limit for DFS
        ucs_cost_limit (float, optional): Cost limit for UCS
    """
    print("\n" + "═" * 80)
    print("🔍 RUNNING PATH FINDING ALGORITHMS")
    print("═" * 80)
    print(f"Start: {start} | Goal: {goal}")
    if dfs_depth:
        print(f"DFS Depth Constraint: {dfs_depth}")
    if ucs_cost_limit:
        print(f"UCS Cost Constraint: {ucs_cost_limit}")
    print("═" * 80)
    
    results = []
    
    # ─────────────────────────────────────────────────────────────────────────
    # BFS (Breadth-First Search)
    # ─────────────────────────────────────────────────────────────────────────
    print("\n📌 Running BFS (Breadth-First Search)...")
    start_time = time.time()
    bfs_path, bfs_visited, bfs_nodes = bfs_search(campus.graph, start, goal)
    bfs_time = time.time() - start_time
    
    print(f"   ⏱️  Time: {bfs_time:.6f} seconds")
    print(f"   📊 Nodes Visited: {bfs_nodes}")
    print(f"   🗺️  Traversal Order: {' → '.join(bfs_visited) if bfs_visited else 'N/A'}")
    
    if bfs_path:
        print(f"   ✅ Path Found: {' → '.join(bfs_path)}")
        print(f"   📏 Path Length: {len(bfs_path) - 1} edges")
    else:
        print(f"   ❌ No path found!")
    
    # Save to history
    save_traversal_history(user_name, "BFS", start, goal, bfs_path, 0, bfs_visited, bfs_time, bfs_nodes)
    results.append(("BFS", bfs_time, bfs_nodes, bfs_path))
    
    # ─────────────────────────────────────────────────────────────────────────
    # DFS (Depth-First Search)
    # ─────────────────────────────────────────────────────────────────────────
    print("\n📌 Running DFS (Depth-First Search)...")
    start_time = time.time()
    dfs_path, dfs_visited, dfs_nodes = dfs_search(campus.graph, start, goal, dfs_depth)
    dfs_time = time.time() - start_time
    
    print(f"   ⏱️  Time: {dfs_time:.6f} seconds")
    print(f"   📊 Nodes Visited: {dfs_nodes}")
    print(f"   🗺️  Traversal Order: {' → '.join(dfs_visited) if dfs_visited else 'N/A'}")
    
    if dfs_path:
        print(f"   ✅ Path Found: {' → '.join(dfs_path)}")
        print(f"   📏 Path Length: {len(dfs_path) - 1} edges")
    else:
        print(f"   ❌ No path found!")
    
    # Save to history
    save_traversal_history(user_name, f"DFS (Depth: {dfs_depth if dfs_depth else 'None'})", 
                          start, goal, dfs_path, 0, dfs_visited, dfs_time, dfs_nodes)
    results.append(("DFS", dfs_time, dfs_nodes, dfs_path))
    
    # ─────────────────────────────────────────────────────────────────────────
    # UCS (Uniform Cost Search)
    # ─────────────────────────────────────────────────────────────────────────
    print("\n📌 Running UCS (Uniform Cost Search)...")
    start_time = time.time()
    ucs_path, ucs_cost, ucs_visited, ucs_nodes = ucs_search(campus.graph, start, goal, ucs_cost_limit)
    ucs_time = time.time() - start_time
    
    print(f"   ⏱️  Time: {ucs_time:.6f} seconds")
    print(f"   📊 Nodes Visited: {ucs_nodes}")
    print(f"   🗺️  Traversal Order: {' → '.join(ucs_visited) if ucs_visited else 'N/A'}")
    
    if ucs_path:
        print(f"   ✅ Path Found: {' → '.join(ucs_path)}")
        print(f"   💰 Total Cost: {ucs_cost}")
        print(f"   📏 Path Length: {len(ucs_path) - 1} edges")
    else:
        print(f"   ❌ No path found!")
    
    # Save to history
    save_traversal_history(user_name, f"UCS (Cost Limit: {ucs_cost_limit if ucs_cost_limit else 'None'})", 
                          start, goal, ucs_path, ucs_cost, ucs_visited, ucs_time, ucs_nodes)
    results.append(("UCS", ucs_time, ucs_nodes, ucs_path))
    
    # ─────────────────────────────────────────────────────────────────────────
    # Performance Comparison
    # ─────────────────────────────────────────────────────────────────────────
    print("\n" + "═" * 80)
    print("📊 PERFORMANCE COMPARISON")
    print("═" * 80)
    print(f"{'Algorithm':<15} {'Time (sec)':<15} {'Nodes Visited':<15} {'Path Found':<10}")
    print("-" * 80)
    
    for algo, exec_time, nodes, path in results:
        path_status = "Yes" if path else "No"
        print(f"{algo:<15} {exec_time:<15.6f} {nodes:<15} {path_status:<10}")
    
    # Find fastest algorithm
    fastest = min(results, key=lambda x: x[1])
    print("-" * 80)
    print(f"🏆 Fastest Algorithm: {fastest[0]} ({fastest[1]:.6f} seconds)")
    print("═" * 80)


# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def initialize_sample_campus():
    """
    Create a sample campus with predefined locations and connections for testing.
    
    Returns:
        CampusGraph: A campus graph with sample data
    """
    campus = CampusGraph()
    
    # Add locations
    locations = ['A', 'B', 'C', 'D', 'E']
    for loc in locations:
        campus.add_location(loc)
    
    # Add connections (bidirectional with weights)
    campus.add_connection('A', 'B', 2)
    campus.add_connection('A', 'C', 4)
    campus.add_connection('B', 'D', 3)
    campus.add_connection('C', 'E', 1)
    campus.add_connection('D', 'E', 5)
    
    return campus


def display_menu():
    """Display the main menu options."""
    print("\n" + "╔" + "═" * 78 + "╗")
    print("║" + "🏫 SMART CAMPUS PATH FINDER - MAIN MENU".center(78) + "║")
    print("╚" + "═" * 78 + "╝")
    print("  1️⃣  Display Campus Map")
    print("  2️⃣  Add Location")
    print("  3️⃣  Remove Location")
    print("  4️⃣  Add Connection")
    print("  5️⃣  Remove Connection")
    print("  6️⃣  Find Path (Run All Algorithms)")
    print("  7️⃣  View Traversal History")
    print("  8️⃣  Load Sample Campus")
    print("  9️⃣  Exit")
    print("─" * 80)


# ═══════════════════════════════════════════════════════════════════════════
# MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """
    Main function to run the Smart Campus Path Finder application.
    Provides an interactive menu-driven interface for users.
    """
    print("\n" + "╔" + "═" * 78 + "╗")
    print("║" + "🏫 WELCOME TO SMART CAMPUS PATH FINDER".center(78) + "║")
    print("╚" + "═" * 78 + "╝")
    
    # Initialize empty campus
    campus = CampusGraph()
    user_name = input("\n👤 Enter your name: ").strip() or "Anonymous"
    
    print(f"\n✅ Welcome, {user_name}!")
    print("💡 Tip: Use option 8 to load a sample campus, or build your own!")
    
    # Main program loop
    while True:
        display_menu()
        choice = input("👉 Enter your choice (1-9): ").strip()
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 1: Display Campus Map
        # ─────────────────────────────────────────────────────────────────────
        if choice == '1':
            campus.display_graph()
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 2: Add Location
        # ─────────────────────────────────────────────────────────────────────
        elif choice == '2':
            location = input("📍 Enter location name: ").strip().upper()
            if location:
                print(campus.add_location(location))
            else:
                print("❌ Location name cannot be empty!")
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 3: Remove Location
        # ─────────────────────────────────────────────────────────────────────
        elif choice == '3':
            location = input("📍 Enter location name to remove: ").strip().upper()
            if location:
                print(campus.remove_location(location))
            else:
                print("❌ Location name cannot be empty!")
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 4: Add Connection
        # ─────────────────────────────────────────────────────────────────────
        elif choice == '4':
            from_loc = input("📍 Enter first location: ").strip().upper()
            to_loc = input("📍 Enter second location: ").strip().upper()
            try:
                weight = float(input("💰 Enter connection cost/distance: "))
                if weight <= 0:
                    print("❌ Cost must be positive!")
                else:
                    print(campus.add_connection(from_loc, to_loc, weight))
            except ValueError:
                print("❌ Invalid cost value!")
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 5: Remove Connection
        # ─────────────────────────────────────────────────────────────────────
        elif choice == '5':
            from_loc = input("📍 Enter first location: ").strip().upper()
            to_loc = input("📍 Enter second location: ").strip().upper()
            print(campus.remove_connection(from_loc, to_loc))
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 6: Find Path (Run All Algorithms)
        # ─────────────────────────────────────────────────────────────────────
        elif choice == '6':
            if not campus.graph:
                print("❌ Campus map is empty! Add locations and connections first.")
                continue
            
            start = input("🎯 Enter start location: ").strip().upper()
            goal = input("🎯 Enter goal location: ").strip().upper()
            
            if start not in campus.graph:
                print(f"❌ Start location '{start}' does not exist!")
                continue
            if goal not in campus.graph:
                print(f"❌ Goal location '{goal}' does not exist!")
                continue
            
            # Optional constraints
            print("\n⚙️  Optional Constraints (press Enter to skip):")
            dfs_depth_input = input("   DFS maximum depth: ").strip()
            ucs_cost_input = input("   UCS maximum cost: ").strip()
            
            dfs_depth = int(dfs_depth_input) if dfs_depth_input else None
            ucs_cost = float(ucs_cost_input) if ucs_cost_input else None
            
            # Run all algorithms and compare
            find_and_compare_paths(campus, start, goal, user_name, dfs_depth, ucs_cost)
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 7: View Traversal History
        # ─────────────────────────────────────────────────────────────────────
        elif choice == '7':
            try:
                with open("traversal_history.txt", "r") as file:
                    content = file.read()
                    if content:
                        print("\n" + "═" * 80)
                        print("📜 TRAVERSAL HISTORY")
                        print("═" * 80)
                        print(content)
                    else:
                        print("\n📭 No traversal history yet!")
            except FileNotFoundError:
                print("\n📭 No traversal history file found!")
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 8: Load Sample Campus
        # ─────────────────────────────────────────────────────────────────────
        elif choice == '8':
            campus = initialize_sample_campus()
            print("\n✅ Sample campus loaded successfully!")
            print("📍 Locations: A, B, C, D, E")
            print("🔗 Connections: A-B(2), A-C(4), B-D(3), C-E(1), D-E(5)")
            campus.display_graph()
        
        # ─────────────────────────────────────────────────────────────────────
        # Option 9: Exit
        # ─────────────────────────────────────────────────────────────────────
        elif choice == '9':
            print("\n" + "═" * 80)
            print("👋 Thank you for using Smart Campus Path Finder!")
            print(f"   User: {user_name}")
            print(f"   Session ended: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("═" * 80)
            break
        
        # ─────────────────────────────────────────────────────────────────────
        # Invalid Choice
        # ─────────────────────────────────────────────────────────────────────
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 9.")


# ═══════════════════════════════════════════════════════════════════════════
# PROGRAM ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()

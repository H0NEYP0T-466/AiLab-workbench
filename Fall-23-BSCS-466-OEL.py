"""
Smart Campus Path Finder
A comprehensive path-finding system using BFS, DFS, and UCS algorithms
to navigate through campus locations with performance comparison.
"""

import time
from collections import deque, defaultdict
import heapq
from datetime import datetime

class CampusGraph:
    """
    Represents the campus as a weighted graph structure.
    Nodes = Locations, Edges = Paths with weights (distances/costs)
    """
    
    def __init__(self):
        """Initialize an empty graph using adjacency list representation"""
        # Dictionary to store graph: {node: [(neighbor, weight), ...]}
        self.graph = defaultdict(list)
        # Set to keep track of all nodes in the graph
        self.nodes = set()
    
    def add_location(self, location):
        """
        Add a new location (node) to the campus graph.
        
        Args:
            location (str): Name of the location to add
        """
        if location not in self.nodes:
            self.nodes.add(location)
            print(f"✅ Location '{location}' added successfully!")
        else:
            print(f"⚠️  Location '{location}' already exists!")
    
    def remove_location(self, location):
        """
        Remove a location (node) and all its connections from the graph.
        
        Args:
            location (str): Name of the location to remove
        """
        if location not in self.nodes:
            print(f"❌ Location '{location}' does not exist!")
            return
        
        # Remove the node from the nodes set
        self.nodes.remove(location)
        
        # Remove all edges connected to this node
        if location in self.graph:
            del self.graph[location]
        
        # Remove this node from other nodes' adjacency lists
        for node in self.graph:
            self.graph[node] = [(neighbor, weight) for neighbor, weight in self.graph[node] 
                                if neighbor != location]
        
        print(f"✅ Location '{location}' removed successfully!")
    
    def add_path(self, location1, location2, weight):
        """
        Add a bidirectional path (edge) between two locations with a given weight.
        
        Args:
            location1 (str): First location
            location2 (str): Second location
            weight (float): Distance/cost of the path
        """
        # Ensure both locations exist in the graph
        if location1 not in self.nodes:
            self.add_location(location1)
        if location2 not in self.nodes:
            self.add_location(location2)
        
        # Add bidirectional edges (undirected graph)
        self.graph[location1].append((location2, weight))
        self.graph[location2].append((location1, weight))
        
        print(f"✅ Path added: {location1} ↔ {location2} (Cost: {weight})")
    
    def remove_path(self, location1, location2):
        """
        Remove a path (edge) between two locations.
        
        Args:
            location1 (str): First location
            location2 (str): Second location
        """
        if location1 not in self.nodes or location2 not in self.nodes:
            print(f"❌ One or both locations do not exist!")
            return
        
        # Remove edges in both directions
        self.graph[location1] = [(neighbor, weight) for neighbor, weight in self.graph[location1] 
                                  if neighbor != location2]
        self.graph[location2] = [(neighbor, weight) for neighbor, weight in self.graph[location2] 
                                  if neighbor != location1]
        
        print(f"✅ Path removed: {location1} ↔ {location2}")
    
    def display_graph(self):
        """Display the entire campus graph structure"""
        if not self.nodes:
            print("📍 Campus is empty. No locations added yet.")
            return
        
        print("\n" + "="*60)
        print("🗺️  CAMPUS MAP")
        print("="*60)
        for node in sorted(self.nodes):
            if node in self.graph and self.graph[node]:
                connections = ", ".join([f"{neighbor}({weight})" 
                                        for neighbor, weight in self.graph[node]])
                print(f"📍 {node} → {connections}")
            else:
                print(f"📍 {node} → (No connections)")
        print("="*60 + "\n")


class PathFinder:
    """
    Implements path-finding algorithms: BFS, DFS, and UCS
    """
    
    def __init__(self, graph):
        """
        Initialize the PathFinder with a campus graph.
        
        Args:
            graph (CampusGraph): The campus graph to search
        """
        self.graph = graph
    
    def bfs(self, start, goal):
        """
        Breadth-First Search: Explores nodes level by level.
        Guarantees shortest path in terms of number of edges (not cost).
        
        Args:
            start (str): Starting location
            goal (str): Goal location
            
        Returns:
            tuple: (path, visited_nodes, total_cost, nodes_visited_count)
        """
        if start not in self.graph.nodes or goal not in self.graph.nodes:
            return None, [], 0, 0
        
        # Queue stores tuples: (current_node, path_so_far, cost_so_far)
        queue = deque([(start, [start], 0)])
        visited = set([start])
        visited_order = [start]  # Track order of node visits
        
        while queue:
            current, path, cost = queue.popleft()
            
            # Goal found!
            if current == goal:
                return path, visited_order, cost, len(visited_order)
            
            # Explore neighbors
            for neighbor, weight in self.graph.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    visited_order.append(neighbor)
                    queue.append((neighbor, path + [neighbor], cost + weight))
        
        # No path found
        return None, visited_order, 0, len(visited_order)
    
    def dfs(self, start, goal, max_depth=float('inf')):
        """
        Depth-First Search: Explores as deep as possible before backtracking.
        Can use depth constraint to limit search.
        
        Args:
            start (str): Starting location
            goal (str): Goal location
            max_depth (int): Maximum depth to search (constraint)
            
        Returns:
            tuple: (path, visited_nodes, total_cost, nodes_visited_count)
        """
        if start not in self.graph.nodes or goal not in self.graph.nodes:
            return None, [], 0, 0
        
        # Stack stores tuples: (current_node, path_so_far, cost_so_far, depth)
        stack = [(start, [start], 0, 0)]
        visited = set()
        visited_order = []
        
        while stack:
            current, path, cost, depth = stack.pop()
            
            # Skip if already visited or exceeds depth limit
            if current in visited or depth > max_depth:
                continue
            
            visited.add(current)
            visited_order.append(current)
            
            # Goal found!
            if current == goal:
                return path, visited_order, cost, len(visited_order)
            
            # Explore neighbors (reversed to maintain left-to-right order)
            for neighbor, weight in reversed(self.graph.graph[current]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + weight, depth + 1))
        
        # No path found
        return None, visited_order, 0, len(visited_order)
    
    def ucs(self, start, goal, cost_limit=float('inf')):
        """
        Uniform Cost Search: Explores nodes in order of lowest cumulative cost.
        Guarantees optimal path based on edge weights.
        Uses priority queue (min-heap) for efficiency.
        
        Args:
            start (str): Starting location
            goal (str): Goal location
            cost_limit (float): Maximum cost allowed (constraint)
            
        Returns:
            tuple: (path, visited_nodes, total_cost, nodes_visited_count)
        """
        if start not in self.graph.nodes or goal not in self.graph.nodes:
            return None, [], 0, 0
        
        # Priority queue stores tuples: (cost, current_node, path_so_far)
        # heapq uses first element (cost) for priority
        pq = [(0, start, [start])]
        visited = set()
        visited_order = []
        
        while pq:
            cost, current, path = heapq.heappop(pq)
            
            # Skip if already visited or exceeds cost limit
            if current in visited or cost > cost_limit:
                continue
            
            visited.add(current)
            visited_order.append(current)
            
            # Goal found!
            if current == goal:
                return path, visited_order, cost, len(visited_order)
            
            # Explore neighbors
            for neighbor, weight in self.graph.graph[current]:
                if neighbor not in visited:
                    new_cost = cost + weight
                    heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
        
        # No path found
        return None, visited_order, 0, len(visited_order)


def save_to_history(username, start, goal, algorithm, path, visited, cost, execution_time):
    """
    Save search results to a text file for historical tracking.
    
    Args:
        username (str): Name of the user
        start (str): Starting location
        goal (str): Goal location
        algorithm (str): Algorithm used (BFS/DFS/UCS)
        path (list): Final path found
        visited (list): Nodes visited during search
        cost (float): Total cost of the path
        execution_time (float): Time taken for execution
    """
    try:
        with open("traversal_history.txt", "a", encoding="utf-8") as file:
            file.write("=" * 70 + "\n")
            file.write(f"📅 Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"👤 User: {username}\n")
            file.write(f"🔍 Algorithm: {algorithm}\n")
            file.write(f"🚀 Start: {start} → 🎯 Goal: {goal}\n")
            file.write(f"👣 Visited Nodes: {' → '.join(visited)}\n")
            
            if path:
                file.write(f"✅ Path Found: {' → '.join(path)}\n")
                file.write(f"💰 Total Cost: {cost}\n")
            else:
                file.write(f"❌ No path found\n")
            
            file.write(f"⏱️  Execution Time: {execution_time:.6f} seconds\n")
            file.write("=" * 70 + "\n\n")
        
        print("💾 Results saved to 'traversal_history.txt'")
    except Exception as e:
        print(f"⚠️  Error saving to file: {e}")


def display_results(algorithm, path, visited, cost, nodes_count, exec_time):
    """
    Display formatted search results for an algorithm.
    
    Args:
        algorithm (str): Name of the algorithm
        path (list): Path found
        visited (list): Nodes visited
        cost (float): Total cost
        nodes_count (int): Number of nodes visited
        exec_time (float): Execution time
    """
    print(f"\n{'='*70}")
    print(f"🔍 {algorithm} RESULTS")
    print(f"{'='*70}")
    print(f"👣 Traversal Order: {' → '.join(visited)}")
    print(f"📊 Nodes Visited: {nodes_count}")
    
    if path:
        print(f"✅ Path Found: {' → '.join(path)}")
        print(f"💰 Total Cost: {cost}")
    else:
        print(f"❌ No path found")
    
    print(f"⏱️  Execution Time: {exec_time:.6f} seconds")
    print(f"{'='*70}\n")


def compare_algorithms(results):
    """
    Compare performance of all three algorithms side by side.
    
    Args:
        results (dict): Dictionary containing results from all algorithms
    """
    print("\n" + "="*70)
    print("📊 ALGORITHM COMPARISON")
    print("="*70)
    print(f"{'Algorithm':<15} {'Nodes Visited':<15} {'Path Cost':<15} {'Time (sec)':<15}")
    print("-"*70)
    
    for algo, data in results.items():
        nodes = data['nodes_count']
        cost = data['cost'] if data['path'] else "N/A"
        time_taken = f"{data['time']:.6f}"
        print(f"{algo:<15} {nodes:<15} {str(cost):<15} {time_taken:<15}")
    
    print("="*70)
    
    # Find the fastest algorithm
    fastest = min(results.items(), key=lambda x: x[1]['time'])
    print(f"🏆 Fastest Algorithm: {fastest[0]} ({fastest[1]['time']:.6f} seconds)")
    
    # Find algorithm with shortest path cost (if paths exist)
    valid_paths = {k: v for k, v in results.items() if v['path']}
    if valid_paths:
        cheapest = min(valid_paths.items(), key=lambda x: x[1]['cost'])
        print(f"💎 Lowest Cost Path: {cheapest[0]} (Cost: {cheapest[1]['cost']})")
    
    print("="*70 + "\n")


def create_sample_campus(graph):
    """
    Create a sample campus with predefined locations and paths for testing.
    
    Args:
        graph (CampusGraph): The graph to populate
    """
    # Add locations
    locations = ['Library', 'Cafeteria', 'Lab', 'Dormitory', 'Stadium', 'Gate']
    for loc in locations:
        graph.add_location(loc)
    
    # Add paths with weights (distances)
    paths = [
        ('Library', 'Cafeteria', 2),
        ('Library', 'Lab', 4),
        ('Cafeteria', 'Dormitory', 3),
        ('Lab', 'Stadium', 1),
        ('Dormitory', 'Stadium', 5),
        ('Stadium', 'Gate', 2),
        ('Lab', 'Gate', 6)
    ]
    
    for loc1, loc2, weight in paths:
        graph.add_path(loc1, loc2, weight)
    
    print("✅ Sample campus created with 6 locations and 7 paths!")


def main_menu():
    """
    Main interactive menu for the Smart Campus Path Finder system.
    Provides options for all required functionalities.
    """
    # Initialize campus graph and path finder
    campus = CampusGraph()
    finder = PathFinder(campus)
    
    # Get username for history tracking
    print("\n" + "="*70)
    print("🏫 WELCOME TO SMART CAMPUS PATH FINDER")
    print("="*70)
    username = input("👤 Enter your name: ").strip() or "Guest"
    
    while True:
        print("\n" + "="*70)
        print("📋 MAIN MENU")
        print("="*70)
        print("1️⃣  Add Location")
        print("2️⃣  Remove Location")
        print("3️⃣  Add Path (Connection)")
        print("4️⃣  Remove Path")
        print("5️⃣  Display Campus Map")
        print("6️⃣  Find Path (Run Algorithms)")
        print("7️⃣  Create Sample Campus")
        print("8️⃣  View Traversal History")
        print("9️⃣  Exit")
        print("="*70)
        
        choice = input("➡️  Enter your choice (1-9): ").strip()
        
        if choice == '1':
            # Add a new location
            location = input("📍 Enter location name: ").strip()
            if location:
                campus.add_location(location)
            else:
                print("❌ Invalid location name!")
        
        elif choice == '2':
            # Remove a location
            location = input("📍 Enter location to remove: ").strip()
            if location:
                campus.remove_location(location)
            else:
                print("❌ Invalid location name!")
        
        elif choice == '3':
            # Add a path between two locations
            loc1 = input("📍 Enter first location: ").strip()
            loc2 = input("📍 Enter second location: ").strip()
            try:
                weight = float(input("💰 Enter path cost/distance: ").strip())
                if loc1 and loc2 and weight > 0:
                    campus.add_path(loc1, loc2, weight)
                else:
                    print("❌ Invalid input! Cost must be positive.")
            except ValueError:
                print("❌ Invalid cost! Please enter a number.")
        
        elif choice == '4':
            # Remove a path
            loc1 = input("📍 Enter first location: ").strip()
            loc2 = input("📍 Enter second location: ").strip()
            if loc1 and loc2:
                campus.remove_path(loc1, loc2)
            else:
                print("❌ Invalid location names!")
        
        elif choice == '5':
            # Display the campus map
            campus.display_graph()
        
        elif choice == '6':
            # Find path using algorithms
            if not campus.nodes:
                print("❌ Campus is empty! Add locations first.")
                continue
            
            print("\n📍 Available locations:", ", ".join(sorted(campus.nodes)))
            start = input("🚀 Enter start location: ").strip()
            goal = input("🎯 Enter goal location: ").strip()
            
            if start not in campus.nodes or goal not in campus.nodes:
                print("❌ Invalid locations! Please check and try again.")
                continue
            
            # Ask for constraints
            print("\n⚙️  Optional Constraints:")
            try:
                max_depth = input("   Max depth for DFS (press Enter for unlimited): ").strip()
                max_depth = int(max_depth) if max_depth else float('inf')
                
                cost_limit = input("   Max cost for UCS (press Enter for unlimited): ").strip()
                cost_limit = float(cost_limit) if cost_limit else float('inf')
            except ValueError:
                print("⚠️  Invalid constraint values. Using unlimited.")
                max_depth = float('inf')
                cost_limit = float('inf')
            
            # Dictionary to store results
            results = {}
            
            # Run BFS
            print("\n🔄 Running BFS...")
            start_time = time.time()
            path, visited, cost, nodes_count = finder.bfs(start, goal)
            exec_time = time.time() - start_time
            display_results("Breadth-First Search (BFS)", path, visited, cost, nodes_count, exec_time)
            save_to_history(username, start, goal, "BFS", path, visited, cost, exec_time)
            results['BFS'] = {'path': path, 'cost': cost, 'nodes_count': nodes_count, 'time': exec_time}
            
            # Run DFS
            print("🔄 Running DFS...")
            start_time = time.time()
            path, visited, cost, nodes_count = finder.dfs(start, goal, max_depth)
            exec_time = time.time() - start_time
            constraint_info = f" (Max Depth: {max_depth})" if max_depth != float('inf') else ""
            display_results(f"Depth-First Search (DFS){constraint_info}", path, visited, cost, nodes_count, exec_time)
            save_to_history(username, start, goal, f"DFS{constraint_info}", path, visited, cost, exec_time)
            results['DFS'] = {'path': path, 'cost': cost, 'nodes_count': nodes_count, 'time': exec_time}
            
            # Run UCS
            print("🔄 Running UCS...")
            start_time = time.time()
            path, visited, cost, nodes_count = finder.ucs(start, goal, cost_limit)
            exec_time = time.time() - start_time
            constraint_info = f" (Max Cost: {cost_limit})" if cost_limit != float('inf') else ""
            display_results(f"Uniform Cost Search (UCS){constraint_info}", path, visited, cost, nodes_count, exec_time)
            save_to_history(username, start, goal, f"UCS{constraint_info}", path, visited, cost, exec_time)
            results['UCS'] = {'path': path, 'cost': cost, 'nodes_count': nodes_count, 'time': exec_time}
            
            # Compare algorithms
            compare_algorithms(results)
        
        elif choice == '7':
            # Create sample campus for testing
            confirm = input("⚠️  This will reset the campus. Continue? (y/n): ").strip().lower()
            if confirm == 'y':
                campus = CampusGraph()
                finder = PathFinder(campus)
                create_sample_campus(campus)
                campus.display_graph()
        
        elif choice == '8':
            # View traversal history
            try:
                with open("traversal_history.txt", "r", encoding="utf-8") as file:
                    content = file.read()
                    if content:
                        print("\n" + "="*70)
                        print("📜 TRAVERSAL HISTORY")
                        print("="*70)
                        print(content)
                    else:
                        print("📜 No history available yet.")
            except FileNotFoundError:
                print("📜 No history file found. Run some searches first!")
        
        elif choice == '9':
            # Exit the program
            print("\n" + "="*70)
            print("👋 Thank you for using Smart Campus Path Finder!")
            print("="*70)
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 9.")


# Program entry point
if __name__ == "__main__":
    main_menu()
from collections import deque
import queue
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

graph2 = {
    'A': ['B', 'C'],
    'B': ['D' , 'E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}


def bfs(graph, start, goal):
    queue = deque([[start]])  
    visited = set()           

    while queue:
        path = queue.popleft()   
        node = path[-1]          

        if node == goal:
            return path  
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  



start_node = 'A'  
goal_node = 'G'

print("BFS Search (Shortest Path)")
bfs_path = bfs(graph2, start_node, goal_node)
print("Path Found by BFS:", bfs_path)


def dfs(graph, start, goal):
    stack = [[start]]  
    visited = set()           
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None 

print("DFS Search (Shortest Path)")
dfs_path = dfs(graph2, start_node, goal_node)
print("Path Found by DFS:", dfs_path)

graph_ucs = {
    'A': {'B': 13, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 1},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

start_node = 'A'
goal_node = 'G'

def ucs(graph, start, goal):
    pq = queue.PriorityQueue()
    pq.put((0, [start]))  
    visited = set()           

    while pq:
        cost, path = pq.get()   
        node = path[-1]         

        if node == goal:
            return path, cost  
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                    new_path = list(path)
                    new_path.append(neighbor)
                    pq.put((cost + weight, new_path))  

    return None, float('inf')



print("UCS Search (Lowest Cost Path)")
ucs_path, ucs_cost = ucs(graph_ucs, start_node, goal_node)
print("Path Found by UCS:", ucs_path)
print("Cost of Path Found by UCS:", ucs_cost)
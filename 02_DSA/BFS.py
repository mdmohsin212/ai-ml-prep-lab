from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
        
    return visited


my_graph = {
    'A': {'B', 'D'},
    'B': {'A', 'C', 'E'},
    'C': {'B'},
    'D': {'A', 'E'},
    'E': {'B', 'D'}
}

result = bfs(my_graph, 'A')
print(f"Visited : {result}")
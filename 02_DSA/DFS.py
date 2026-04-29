def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(start)
    for vertex in graph[start] - visited:
        dfs(graph, vertex, visited)
    
    return visited


my_graph = {
    'A': {'B', 'D'},
    'B': {'A', 'C', 'E'},
    'C': {'B'},
    'D': {'A', 'E'},
    'E': {'B', 'D'}
}

result = dfs(my_graph, 'A')
print(f"Visited : {result}")
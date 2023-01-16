graph = {
    'A': ['B'],
    'B': ['A', 'H', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def dfs_recursive(graph, node, visited=[]):
    visited.append(node)
    for near_node in graph[node]:
        if near_node not in visited:
            print(visited)
            dfs_recursive(graph, near_node, visited)
    return visited

dfs_recursive(graph, 'A')
'''
    ['A']
    ['A', 'B']
    ['A', 'B', 'H']
    ['A', 'B', 'H', 'I']
    ['A', 'B', 'H', 'I', 'J']
    ['A', 'B', 'H', 'I', 'J', 'K']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C', 'D']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C', 'D', 'E']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C', 'D', 'E', 'F']
    ['A', 'B', 'H', 'I', 'J', 'K', 'L', 'M', 'C', 'D', 'E', 'F', 'G']
'''
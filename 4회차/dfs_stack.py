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

def dfs_stack(graph, node):
    visited = []
    stack=[]

    stack.append(node)

    while stack:                                # 스택에 남은것이 없을 때까지 반복
        node = stack.pop()
        if node not in visited:                 # 방문한 노드인지를 확인. 노드가 아닐 경우에만 근접 노드를 stack에 추가
            visited.append(node)
            stack.extend(graph[node])

    return visited       
    
dfs_stack(graph, "A")
'''
    A ['A'] ['B']
    B ['A', 'B'] ['A', 'H', 'C']
    C ['A', 'B', 'C'] ['A', 'H', 'B', 'D']
    D ['A', 'B', 'C', 'D'] ['A', 'H', 'B', 'C', 'E', 'G']
    G ['A', 'B', 'C', 'D', 'G'] ['A', 'H', 'B', 'C', 'E', 'D']
    E ['A', 'B', 'C', 'D', 'G', 'E'] ['A', 'H', 'B', 'C', 'D', 'F']
    F ['A', 'B', 'C', 'D', 'G', 'E', 'F'] ['A', 'H', 'B', 'C', 'D', 'E']
    H ['A', 'B', 'C', 'D', 'G', 'E', 'F', 'H'] ['A', 'B', 'I', 'J', 'M']
    M ['A', 'B', 'C', 'D', 'G', 'E', 'F', 'H', 'M'] ['A', 'B', 'I', 'J', 'H']
    J ['A', 'B', 'C', 'D', 'G', 'E', 'F', 'H', 'M', 'J'] ['A', 'B', 'I', 'H', 'K']
    K ['A', 'B', 'C', 'D', 'G', 'E', 'F', 'H', 'M', 'J', 'K'] ['A', 'B', 'I', 'H', 'J', 'L']
    L ['A', 'B', 'C', 'D', 'G', 'E', 'F', 'H', 'M', 'J', 'K', 'L'] ['A', 'B', 'I', 'H', 'J', 'K']
    I ['A', 'B', 'C', 'D', 'G', 'E', 'F', 'H', 'M', 'J', 'K', 'L', 'I'] ['A', 'B', 'H']
'''
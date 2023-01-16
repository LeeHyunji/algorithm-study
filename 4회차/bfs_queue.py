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
from collections import deque

def bfs_queue(graph, node):
    visited = []
    queue=deque()

    queue.appendleft(node)

    while queue:                                # 큐에 남은것이 없을 때까지 반복
        node = queue.pop()
        if node not in visited:                 # 방문한 노드인지를 확인. 노드가 아닐 경우에만 근접 노드를 Queue에 추가
            visited.append(node)
            print(node, visited, queue)
            queue.extendleft(graph[node])

    return visited       
    
bfs_queue(graph, "A")
'''
    A ['A'] deque([])
    B ['A', 'B'] deque([])
    H ['A', 'B', 'H'] deque(['C'])
    C ['A', 'B', 'H', 'C'] deque(['M', 'J', 'I', 'B'])
    I ['A', 'B', 'H', 'C', 'I'] deque(['D', 'B', 'M', 'J'])
    J ['A', 'B', 'H', 'C', 'I', 'J'] deque(['H', 'D', 'B', 'M'])
    M ['A', 'B', 'H', 'C', 'I', 'J', 'M'] deque(['K', 'H', 'H', 'D', 'B'])
    D ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D'] deque(['H', 'K', 'H', 'H'])
    K ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K'] deque(['G', 'E', 'C', 'H'])
    E ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K', 'E'] deque(['L', 'J', 'G'])
    G ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K', 'E', 'G'] deque(['F', 'D', 'L', 'J'])
    L ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K', 'E', 'G', 'L'] deque(['D', 'F', 'D'])
    F ['A', 'B', 'H', 'C', 'I', 'J', 'M', 'D', 'K', 'E', 'G', 'L', 'F'] deque(['K', 'D'])
'''
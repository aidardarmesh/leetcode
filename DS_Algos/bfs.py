def bfs(graph, s):
    visited = {s}
    parent = {s: ''}
    dist = {s: 0}

    from collections import deque
    deq = deque()
    deq.append(s)

    while deq:
        v = deq.popleft()

        for to in graph[v]:
            if not to in visited:
                deq.append(to)
                visited.add(to)
                parent[to] = v
                dist[to] = dist[v] + 1
    
    print(parent)
    print(dist)

graph = {
    'a': ['s', 'z'],
    'z': ['a'],
    's': ['a', 'x'],
    'x': ['s', 'd', 'c'],
    'c': ['x', 'd', 'v'],
    'd': ['x', 'c', 'f'],
    'f': ['f', 'c', 'v'],
    'v': ['c', 'f'],
}

bfs(graph, 's')

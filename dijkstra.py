def shortest_paths(graph, start):
    import heapq

    path_weight = {i: float('inf') for i in graph}
    previous = {i: -1 for i in graph}
    path_weight[start] = 0
    remaining = [(0, start)]
    visited = set()

    while remaining:
        _, a = heapq.heappop(remaining)

        if a in visited:
            continue

        visited.add(a)

        for b, weight in graph[a]:
            if path_weight[a] + weight < path_weight[b]:
                path_weight[b] = path_weight[a] + weight
                previous[b] = a
                heapq.heappush(remaining, (path_weight[b], b))
    
    return previous


def path_to(previous, end):
    path = []

    while end != -1:
        path.append(end)
        end = previous[end]
    
    while path:
        print(path.pop(), end=' ')


graph = {
    'a': [('b', 5), ('c', 3), ('e', 2)],
    'b': [('d', 2)],
    'c': [('b', 1), ('d', 1)],
    'd': [('a', 1), ('g', 2), ('h', 1)],
    'e': [('a', 1), ('h', 4), ('i', 7)],
    'f': [('b', 3), ('g', 1)],
    'g': [('c', 3), ('i', 2)],
    'h': [('c', 2), ('g', 2)],
    'i': []
}
START = 'a'
END = 'i'
path_to(shortest_paths(graph, START), END)

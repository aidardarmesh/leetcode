graph = {
    'a': ['s', 'z'],
    'z': ['a'],
    's': ['a', 'x'],
    'x': ['s', 'd'],
    'c': ['v'],
    'd': ['x', 'f'],
    'f': ['d', 'v'],
    'v': ['f', 'c'],
}

# with cycle
# graph = {
#     'a': ['s', 'z'],
#     'z': ['a'],
#     's': ['a', 'x'],
#     'x': ['s', 'c', 'd'],
#     'c': ['x', 'd', 'v'],
#     'd': ['x', 'c', 'f'],
#     'f': ['d', 'c', 'v'],
#     'v': ['f', 'c'],
# }

visited = {c: False for c in graph}

def dfs(v, parent):
    visited[v] = True

    for to in graph[v]:
        if not visited[to]:
            if dfs(to, v):
                return True
        elif parent != to:
            return True
    
    return False

for v in graph:
    if not visited[v]:
        if dfs(v, -1):
            print('cycle')
            break

graph = {
    'a': ['z'],
    'z': [],
    's': ['a', 'x'],
    'x': ['d', 'c'],
    'd': ['c', 'f'],
    'c': [],
    'f': ['v'],
    'v': ['c'],
}

# graph with cycle
# graph = {
#     'a': ['z'],
#     'z': [],
#     's': ['a', 'x'],
#     'x': ['d', 'c'],
#     'd': ['c', 'f'],
#     'c': ['f'],
#     'f': ['v'],
#     'v': ['c'],
# }

colors = {c: 0 for c in graph}
parent = {c: -1 for c in graph}
cycle = {'start': 0, 'end': 0}

ans = []
top_sort = []

def dfs(v):
    if colors[v] == 2:
        return
    
    colors[v] = 1

    for to in graph[v]:
        if colors[to] == 0:
            parent[to] = v
            
            if dfs(to):
                return True
        elif colors[to] == 1:
            cycle['start'] = to
            cycle['end'] = v
            return True
    
    colors[v] = 2
    top_sort.append(v)
    return False

for v in graph:
    if dfs(v):
        break

while cycle['end'] != cycle['start']:
    ans.append(cycle['end'])
    cycle['end'] = parent[cycle['end']]

ans.append(cycle['start'])

print(ans[::-1])
print(top_sort[::-1])

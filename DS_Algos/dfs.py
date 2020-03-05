from typing import *

def dfs(graph):
    visited = set()

    def dfs_visit(s):
        if not s in visited:
            visited.add(s)
            print(s, end=' ')

            for to in graph[s]:
                dfs_visit(to)
    
    for v in graph:
        dfs_visit(v)

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

dfs(graph)

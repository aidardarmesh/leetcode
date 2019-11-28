from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        visited[node] = Node(node.val, [])
        queue = [node]

        while queue:
            n = queue.pop(0)

            for neighbor in n.neighbors:
                if not neighbor in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                visited[n].neighbors.append(visited[neighbor])
        
        return visited[node]

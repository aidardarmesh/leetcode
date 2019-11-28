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
        input_node = node
        queue = [input_node]
        new_nodes = {}
        visited = set()
        
        # creating new nodes
        while queue:
            node = queue.pop(0)
            visited.add(node.val)
            new_nodes[node.val] = Node(node.val, [])
            
            for neighbor in node.neighbors:
                if not neighbor.val in visited:
                    queue.append(neighbor)
        
        # adjusting neighbors
        queue = [input_node]
        visited = set()
        
        while queue:
            node = queue.pop(0)
            visited.add(node.val)
            
            for neighbor in node.neighbors:
                if not new_nodes[neighbor.val] in new_nodes[node.val].neighbors:
                    new_nodes[node.val].neighbors.append(new_nodes[neighbor.val])
                
                if not neighbor.val in visited:
                    queue.append(neighbor)
        
        return new_nodes[input_node.val]

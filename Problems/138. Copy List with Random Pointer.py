from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map_ = {}
        node = head
        
        while node:
            map_[node] = Node(node.val)
            node = node.next
        
        node = head
        
        while node:
            new_node = map_[node]
            new_node.next = map_.get(node.next, None)
            new_node.random = map_.get(node.random, None)
            node = node.next
        
        return map_.get(head, None)

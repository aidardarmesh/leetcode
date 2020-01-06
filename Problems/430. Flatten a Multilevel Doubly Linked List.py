from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        
        while node:
            if node.child:
                child = self.flatten(node.child)
                node.child = None
                next_ = node.next
                
                child.prev = node
                node.next = child
                
                while child and child.next:
                    child = child.next
                
                if next_:
                    child.next = next_
                    next_.prev = child
                
                node = child
            
            node = node.next
        
        return head

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
        if not head:
            return head
        
        node = head
        stack = []
        
        while node:
            if node.child:
                if node.next:
                    stack.append(node.next)
                
                node.next = node.child
                node.child.prev = node
                node.child = None
            
            if not node.next and stack:
                next_ = stack.pop()
                node.next = next_
                next_.prev = node
            
            node = node.next
        
        return head

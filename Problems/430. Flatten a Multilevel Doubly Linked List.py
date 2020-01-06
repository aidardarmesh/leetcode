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
        
        pseudo_head = Node(None, None, head, None)
        prev = pseudo_head
        stack = [head]

        while stack:
            node = stack.pop()

            prev.next = node
            node.prev = prev

            if node.next:
                stack.append(node.next)
            
            if node.child:
                stack.append(node.child)
                node.child = None

            prev = node
        
        pseudo_head.next.prev = None

        return pseudo_head.next

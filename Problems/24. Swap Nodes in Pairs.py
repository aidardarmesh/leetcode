from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(node):
            if not node:
                return
            
            if not node.next:
                return node
            
            next_ = node.next
            node.next = swap(node.next.next)
            next_.next = node
            
            return next_
        
        return swap(head)
        

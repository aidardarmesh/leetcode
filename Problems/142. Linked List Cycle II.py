from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        while head:
            try:
                if head.seen:
                    return head
            except:
                head.seen = 1
                head = head.next
        
        return None

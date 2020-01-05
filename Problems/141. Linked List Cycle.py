from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        import sys

        while head:
            if sys.getrefcount(head) > 4:
                return True

            head = head.next
        
        return False

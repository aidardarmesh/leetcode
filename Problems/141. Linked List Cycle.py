from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        sent = ListNode(-1)
        slow, fast = sent, head

        while fast and fast.next:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
        
        return False

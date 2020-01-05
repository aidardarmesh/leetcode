from typing import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        sent = ListNode(0)
        sent.next = head

        fast = sent

        for _ in range(n):
            fast = fast.next
        
        slow = sent

        for fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return sent.next

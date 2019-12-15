from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = []
        val = 0
        
        while head:
            val = (val << 1) ^ head.val
            head = head.next
        
        return val

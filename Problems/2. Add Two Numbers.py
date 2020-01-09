from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sent = ListNode(-1)
        prev = sent
        factor = 0
        
        while l1 or l2:
            sum_ = factor
            
            if l1:
                sum_ += l1.val
                l1 = l1.next
            
            if l2:
                sum_ += l2.val
                l2 = l2.next
            
            prev.next = ListNode(sum_ % 10)
            prev = prev.next
            factor = sum_ // 10
        
        if factor:
            prev.next = ListNode(factor)
        
        return sent.next

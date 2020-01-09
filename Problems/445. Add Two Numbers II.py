from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2, stack = [], [], []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        factor = 0
        
        while stack1 and stack2:
            sum_ = stack1.pop() + stack2.pop() + factor
            stack.append(sum_ % 10)
            factor = sum_ // 10
        
        while stack1:
            sum_ = stack1.pop() + factor
            stack.append(sum_ % 10)
            factor = sum_ // 10
        
        while stack2:
            sum_ = stack2.pop() + factor
            stack.append(sum_ % 10)
            factor = sum_ // 10
        
        if factor:
            stack.append(factor)
        
        sent = ListNode(-1)
        prev = sent
        
        while stack:
            node = ListNode(stack.pop())
            prev.next = node
            prev = prev.next
        
        return sent.next

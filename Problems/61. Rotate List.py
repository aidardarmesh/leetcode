from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        n = 0
        node = head
        
        while node and node.next:
            n += 1
            node = node.next
        
        n += 1
        k = k % n
        node.next = head
        
        for _ in range(n-k):
            node = head
            head = head.next
        
        node.next = None
        
        return head

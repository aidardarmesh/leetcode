from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sent = ListNode(-1)
        sent.next = head
        prev = cur = sent
        
        for _ in range(m):
            prev = cur
            cur = cur.next
        
        cur_head = cur
        
        for _ in range(n-m):
            next_ = cur.next
            cur.next = next_.next
            next_.next = cur_head
            cur_head = next_
        
        prev.next = cur_head
        
        return sent.next

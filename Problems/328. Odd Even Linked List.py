from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        sent = ListNode(0)
        sent.next = head
        prev = sent
        cur = head
        cnt = 1
        
        while cur and cur.next:
            prev.next = cur.next
            prev = cur
            cur = cur.next
            cnt += 1

        prev.next = cur.next
        
        if cnt % 2 == 0:
            prev.next = sent.next
        else:
            cur.next = sent.next
        
        return head

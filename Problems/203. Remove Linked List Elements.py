from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # https://leetcode.com/articles/remove-linked-list-elements/
        sent = ListNode(0)
        sent.next = head

        prev, cur = sent, head

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            
            cur = cur.next
        
        return sent.next

from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        sent_odd = ListNode(0)
        sent_even = ListNode(0)
        odd = sent_odd
        even = sent_even
        is_odd = True
        
        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            
            is_odd = not is_odd
            head = head.next
        
        even.next = None
        odd.next = sent_even.next
        
        return sent_odd.next

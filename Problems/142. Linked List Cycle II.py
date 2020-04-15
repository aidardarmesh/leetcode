from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def get_intersection(slow, fast):
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
                if slow == fast:
                    return slow
            
            return None
        
        intersection = get_intersection(head, head)
        
        if not intersection:
            return None
        
        ptr1 = head
        ptr2 = intersection
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1

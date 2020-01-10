from typing import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

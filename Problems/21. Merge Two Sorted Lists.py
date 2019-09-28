from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummy = ListNode(-1)

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                dummy.next = l1
                dummy = l1
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = l2
                l2 = l2.next

        if l1 != None:
            dummy.next = l1

        if l2 != None:
            dummy.next = l2

        return head.next

    def print(self, l: ListNode):
        while l != None:
            print(l.val, end=" ")
            l = l.next

# [1,2,4]
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(4)
nodeA.next = nodeB
nodeB.next = nodeC

# [1,3,4]
nodeD = ListNode(1)
nodeE = ListNode(3)
nodeF = ListNode(4)
nodeD.next = nodeE
nodeE.next = nodeF

# [1,1,2,3,4,4]
s = Solution()
s.print(s.mergeTwoLists(nodeA, nodeD))
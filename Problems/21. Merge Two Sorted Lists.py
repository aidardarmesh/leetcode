from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

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
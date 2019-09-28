from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # get head as close to different than val value
        while head != None and head.val == val:
            head = head.next

        cur = head

        # algorithm is similar to removing duplicates problem
        while cur != None and cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            
        return head

    def print(self, head: ListNode):
        while head != None:
            print(head.val, end=" ")
            head = head.next

s = Solution()

# 1->2->6->3->4->5->6, val = 6
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(6)
nodeD = ListNode(3)
nodeE = ListNode(4)
nodeF = ListNode(5)
nodeG = ListNode(6)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG

s.print(s.removeElements(nodeA, 6))
print()

# 1, val = 1
nodeA = ListNode(1)

s.print(s.removeElements(nodeA, 1))
print()

nodeA = ListNode(1)
nodeB = ListNode(2)
nodeA.next = nodeB

s.print(s.removeElements(nodeA, 1))
print()

s.print(s.removeElements(None, 1))
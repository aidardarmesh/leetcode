from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur != None:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next

        return prev

    def print(self, head: ListNode):
        cur = head

        while cur != None:
            print(cur.val, end=" ")
            cur = cur.next
        
        print()

s = Solution()

nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)
nodeE = ListNode(5)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

s.print(s.reverseList(nodeA))
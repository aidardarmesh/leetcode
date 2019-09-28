from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        previous = current = head

        while current != None:
            if previous.val != current.val:
                previous.next = current
                previous = current

            current = current.next
            previous.next = None

        return head

    def print(self, l: ListNode):
        while l:
            print(l.val, end=" ")
            l = l.next

s = Solution()

# [1,1,1,1,1,1,1]
# nodeD = ListNode(1)
# nodeE = ListNode(1)
# nodeF = ListNode(1)
# nodeG = ListNode(1)
# nodeH = ListNode(1)
# nodeI = ListNode(1)
# nodeJ = ListNode(1)
# nodeD.next = nodeE
# nodeE.next = nodeF
# nodeF.next = nodeG
# nodeG.next = nodeH
# nodeH.next = nodeI
# nodeI.next = nodeJ

# s.print(s.deleteDuplicates(nodeD))

# [1,1,2]
# nodeA = ListNode(1)
# nodeB = ListNode(1)
# nodeC = ListNode(2)
# nodeA.next = nodeB
# nodeB.next = nodeC

# s.print(s.deleteDuplicates(nodeA))

# [1,1,1,2,3,3,3]
# nodeD = ListNode(1)
# nodeE = ListNode(1)
# nodeF = ListNode(1)
# nodeG = ListNode(2)
# nodeH = ListNode(3)
# nodeI = ListNode(3)
# nodeJ = ListNode(3)
# nodeD.next = nodeE
# nodeE.next = nodeF
# nodeF.next = nodeG
# nodeG.next = nodeH
# nodeH.next = nodeI
# nodeI.next = nodeJ

# s.print(s.deleteDuplicates(nodeD))
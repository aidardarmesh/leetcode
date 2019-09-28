from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = []

        while head != None:
            if head in visited:
                return True
            else:
                visited.append(head)
            
            head = head.next

        return False

s = Solution()

# [3,2,0,-4]
# nodeA = ListNode(3)
# nodeB = ListNode(2)
# nodeC = ListNode(0)
# nodeD = ListNode(-4)
# nodeA.next = nodeB
# nodeB.next = nodeC
# nodeC.next = nodeD
# nodeD.next = nodeB

# print(s.hasCycle(nodeA))

# [1,2]
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeA.next = nodeB
nodeB.next = nodeA

print(s.hasCycle(nodeA))
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        queue = []

        while head != None:
            stack.append(head.val)
            queue.append(head.val)

            head = head.next
        
        while len(stack) > 0:
            if stack.pop() != queue.pop(0):
                return False

        return True
    
s = Solution()

# 1->2
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeA.next = nodeB

print(s.isPalindrome(nodeA))

# 1->2->2->1
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(2)
nodeD = ListNode(1)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD

print(s.isPalindrome(nodeA))
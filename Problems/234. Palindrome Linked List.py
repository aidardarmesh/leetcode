from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        n, node = 0, head
        
        while node:
            n += 1
            node = node.next
        
        node = head
        half = n//2
        
        for _ in range(half-1):
            next_ = node.next
            node.next = next_.next
            next_.next = head
            head = next_
        
        fast = head
        half = half+1 if n%2 == 1 else half
        
        for _ in range(half):
            fast = fast.next
        
        slow = head
        half = half-1 if n%2 == 1 else half
        
        for _ in range(half):
            if slow.val != fast.val:
                return False
            
            slow = slow.next
            fast = fast.next
        
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
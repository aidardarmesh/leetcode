from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        node = head

        while node and node.next:
            next_ = node.next
            node.next = next_.next
            next_.next = head
            head = next_
        
        return head

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

node = s.reverseList(nodeA)
print(node.val)
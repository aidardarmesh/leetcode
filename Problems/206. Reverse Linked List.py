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
        
        def helper(node):
            if not node.next:
                return node, node
            
            next_, new_head = helper(node.next)
            next_.next = node
            node.next = None
            
            return node, new_head
        
        head, new_head = helper(head)
        
        return new_head

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
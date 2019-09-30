from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummy = ListNode(-1)
        int_ = 0
        sum_ = 0

        while l1 != None and l2 != None:
            sum_ = l1.val + l2.val + int_
            rem = sum_ % 10
            int_ = sum_ // 10
            dummy.next = ListNode(rem)
            dummy = dummy.next

            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            sum_ = l1.val + int_
            rem = sum_ % 10
            int_ = sum_ // 10
            dummy.next = ListNode(rem)
            dummy = dummy.next

            l1 = l1.next
        
        while l2 != None:
            sum_ = l2.val + int_
            rem = sum_ % 10
            int_ = sum_ // 10
            dummy.next = ListNode(rem)
            dummy = dummy.next

            l2 = l2.next

        if int_ != 0:
            dummy.next = ListNode(int_)
            dummy = dummy.next
        
        return head.next

    def print(self, head: ListNode):
        while head != None:
            print(head.val, end=" ")
            head = head.next
        
        print()

s = Solution()

nodeA_0 = ListNode(0)

nodeB_0 = ListNode(0)
nodeB_1 = ListNode(1)
nodeB_0.next = nodeB_1

s.print(s.addTwoNumbers(nodeA_0, nodeB_0))

# nodeA_2 = ListNode(2)
# nodeA_4 = ListNode(4)
# nodeA_2.next = nodeA_4

# nodeB_8 = ListNode(8)
# nodeB_5 = ListNode(5)
# nodeB_8.next = nodeB_5

# s.print(s.addTwoNumbers(nodeA_2, nodeB_8))

# nodeA_2 = ListNode(2)
# nodeA_4 = ListNode(4)
# nodeA_3 = ListNode(3)
# nodeA_2.next = nodeA_4
# nodeA_4.next = nodeA_3

# nodeB_5 = ListNode(5)
# nodeB_6 = ListNode(6)
# nodeB_4 = ListNode(4)
# nodeB_5.next = nodeB_6
# nodeB_6.next = nodeB_4

# s.print(s.addTwoNumbers(nodeA_2, nodeB_5))
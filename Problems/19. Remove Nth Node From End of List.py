from typing import *

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head

        while n > 0:
            fast = fast.next
            n -= 1

        if fast == None:
            head = head.next
            return head
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head

    def print(self, head):
        while head != None:
            print(head.val, end=" ")
            head = head.next
        
        print()

s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s.print(s.removeNthFromEnd(node1, 5))
from typing import *
import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        n = len(lists)
        dummy = head = ListNode(-1)

        for i in range(n):
            sub_head = lists[i]

            while sub_head:
                heapq.heappush(heap, sub_head.val)
                sub_head = sub_head.next

        while heap:
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next
        
        return head.next

    def print(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        
        print()

s = Solution()

nodeA_1 = ListNode(1)
nodeA_4 = ListNode(4)
nodeA_5 = ListNode(5)
nodeA_1.next = nodeA_4
nodeA_4.next = nodeA_5

nodeB_1 = ListNode(1)
nodeB_3 = ListNode(3)
nodeB_4 = ListNode(4)
nodeB_1.next = nodeB_3
nodeB_3.next = nodeB_4

nodeC_2 = ListNode(2)
nodeC_6 = ListNode(6)
nodeC_2.next = nodeC_6

s.print(s.mergeKLists([nodeA_1, nodeB_1, nodeC_2]))
from typing import *

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA

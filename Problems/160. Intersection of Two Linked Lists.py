from typing import *

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nA, nB, curA, curB = 0, 0, headA, headB
        
        while curA:
            curA = curA.next
            nA += 1
        
        while curB:
            curB = curB.next
            nB += 1
        
        curA, curB = headA, headB
        
        if nA < nB:
            for _ in range(nB-nA):
                curB = curB.next
        elif nA > nB:
            for _ in range(nA-nB):
                curA = curA.next
        
        while curA and curB:
            if curA == curB:
                return curA

            curA = curA.next
            curB = curB.next
        
        return None

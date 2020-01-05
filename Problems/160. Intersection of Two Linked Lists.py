from typing import *

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        
        while curA:
            while curB:
                if curA == curB:
                    return curA
                
                curB = curB.next
            
            curA = curA.next
            curB = headB
        
        return None

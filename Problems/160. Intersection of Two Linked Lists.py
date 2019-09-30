# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seen = set()
        curA = headA
        curB = headB

        while curA != None:
            seen.add(curA)
            curA = curA.next
        
        while curB != None:
            if curB in seen:
                return curB
            curB = curB.next
        
        return None

# nodeA_2 = ListNode(2)
# nodeA_6 = ListNode(6)
# nodeA_4 = ListNode(4)
# nodeA_2.next = nodeA_6
# nodeA_6.next = nodeA_4

# nodeB_1 = ListNode(1)
# nodeB_5 = ListNode(5)
# nodeB_1.next = nodeB_5

# s = Solution()

# intersection = s.getIntersectionNode(nodeA_2, nodeB_1)
# print(intersection.val)

# nodeC_8 = ListNode(8)
# nodeC_4 = ListNode(4)
# nodeC_5 = ListNode(5)
# nodeC_8.next = nodeC_4
# nodeC_4.next = nodeC_5

# nodeA_4 = ListNode(4)
# nodeA_1 = ListNode(1)
# nodeA_4.next = nodeA_1
# nodeA_1.next = nodeC_8

# nodeB_5 = ListNode(5)
# nodeB_0 = ListNode(0)
# nodeB_1 = ListNode(1)
# nodeB_5.next = nodeB_0
# nodeB_0.next = nodeB_1
# nodeB_1.next = nodeC_8

# s = Solution()

# intersection = s.getIntersectionNode(nodeA_4, nodeB_5)
# print(intersection.val)
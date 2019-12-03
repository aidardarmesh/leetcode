from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def insert(root, val):
            if not root:
                return TreeNode(val)
            
            node = root
            
            if node.val < val:
                node.right = insert(node.right, val)
            else:
                node.left = insert(node.left, val)
            
            return root
        
        def bin_helper(arr):
            if arr:
                l, r = 0, len(arr)-1
                m = (l+r)//2
                self.root = insert(self.root, arr[m])
                
                bin_helper(arr[:m])
                bin_helper(arr[m+1:])
        
        self.root = None
        dummy = head
        arr = []
        
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next
        
        bin_helper(arr)
        
        return self.root

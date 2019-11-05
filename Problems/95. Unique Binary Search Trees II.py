from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def perms(lst):
            if not lst:
                return []
            
            if len(lst) == 1:
                return [lst]
            
            l = []
            
            for i in range(len(lst)):
                m = lst[i]
                rem = lst[:i] + lst[i+1:]
                
                for perm in perms(rem):
                    l.append([m]+perm)
            
            return l
        
        all_perms = perms([i for i in range(1, n+1)])
        
        def insert(root, val):
            if not root:
                return TreeNode(val)
            
            if root.val > val:
                root.left = insert(root.left, val)
            elif root.val < val:
                root.right = insert(root.right, val)
            
            return root
        
        def serialize(root):
            queue = [root]
            res = []
            
            while any(queue):
                node = queue.pop(0)
                
                if node:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append(None)
            
            return res
        
        uniques = []
        ans = []
        
        for perm in all_perms:
            bst = None
            
            for val in perm:
                bst = insert(bst, val)
            
            bst_lst = serialize(bst)
            
            if not bst_lst in uniques:
                uniques.append(bst_lst)
                ans.append(bst)
        
        return ans

from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        cnt = collections.defaultdict(int)
        ans = []
        
        def collect(root):
            if not root:
                return '#,'
            
            serial = str(root.val) + ',' + collect(root.left) + collect(root.right)
            
            cnt[serial] += 1
            
            if cnt[serial] == 2:
                ans.append(root)
            
            return serial
        
        collect(root)
        
        return ans

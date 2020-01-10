from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def serialize(root):
            if not root:
                return 'None,'
            
            return str(root.val) + ',' + serialize(root.left) + serialize(root.right)
        
        serial_cnt = {}
        serial_node = {}
        
        def find(root):
            if not root:
                return None
            
            root_serial = serialize(root)
            
            serial_cnt[root_serial] = serial_cnt.get(root_serial, 0) + 1
            serial_node[root_serial] = root
            
            find(root.left)
            find(root.right)
        
        find(root)
        
        return [serial_node[serial] for serial, cnt in serial_cnt.items() if cnt > 1]

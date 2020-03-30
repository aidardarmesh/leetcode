from typing import *

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        if not root:
            return 'None,'
        
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
        
    def deserialize(self, data):
        from collections import deque
        
        def helper(data):
            val = data.popleft()
            
            if val == 'None':
                return None
            
            node = TreeNode(val)
            node.left = helper(data)
            node.right = helper(data)
            
            return node
        
        return helper(deque(data.split(',')))
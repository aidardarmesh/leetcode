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
        def helper(data):
            val = data.pop(0)
            
            if val == 'None':
                return None
            
            node = TreeNode(val)
            node.left = helper(data)
            node.right = helper(data)
            
            return node
        
        return helper(data.split(','))

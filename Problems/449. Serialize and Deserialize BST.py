from typing import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        res = []
        
        while any(queue):
            node = queue.pop(0)
            
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split()
        
        if not lst:
            return None
        
        root_val = lst.pop(0)
        root = TreeNode(int(root_val))
        queue = [root]
        
        while lst:
            node = queue.pop(0)
            
            if lst:
                val = lst.pop(0)
                
                if val != 'None':
                    left = TreeNode(int(val))
                    node.left = left
                    queue.append(left)
            
            if lst:
                val = lst.pop(0)
                
                if val != 'None':
                    right = TreeNode(int(val))
                    node.right = right
                    queue.append(right)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
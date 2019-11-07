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
        # making pre-order
        if not root:
            return ''
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            res.append(str(node.val))
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # inserting each val from lst and returning root of tree
        def insert(root, val):
            if not root:
                return TreeNode(val)
            
            if root.val > val:
                root.left = insert(root.left, val)
            elif root.val < val:
                root.right = insert(root.right, val)
            
            return root
        
        lst = list(map(lambda x: int(x), data.split()))
        root = None
        
        for num in lst:
            root = insert(root, num)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
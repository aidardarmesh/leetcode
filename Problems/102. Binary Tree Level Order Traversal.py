from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = []
        queue.append((root, 0))

        while queue:
            node, level = queue.pop(0)
            
            if node.left:
                queue.append((node.left, level+1))
            
            if node.right:
                queue.append((node.right, level+1))
            
            if level < len(result):
                result[level].append(node.val)
            else:
                result.append([node.val])
        
        return result

s = Solution()

node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

print(s.levelOrder(node3))
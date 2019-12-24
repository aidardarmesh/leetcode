from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # level-order traversal to add parent link
        root.parent = None
        queue = [root]
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                
                if node.left:
                    node.left.parent = node
                    queue.append(node.left)
                
                if node.right:
                    node.right.parent = node
                    queue.append(node.right)
        
        # BFS from target with K distance
        level = 0
        visited = {target}
        queue = [target]
        
        while queue:
            if level == K:
                break
            
            level += 1
            size = len(queue)
            
            for _ in range(size):
                node = queue.pop(0)
                
                if node.parent and not node.parent in visited:
                    visited.add(node.parent)
                    queue.append(node.parent)
                
                if node.left and not node.left in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                
                if node.right and not node.right in visited:
                    visited.add(node.right)
                    queue.append(node.right)
        
        return [node.val for node in queue]

from typing import *

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        deq = deque()
        deq.append(root)
        res = []
        
        while deq:
            size = len(deq)
            level = []
            
            for _ in range(size):
                node = deq.popleft()
                level.append(node.val)
                
                for child in node.children:
                    deq.append(child)
            
            res.append(level)
        
        return res

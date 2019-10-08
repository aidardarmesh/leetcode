from typing import *

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        
        pre = root
        current = None

        while pre.left:
            current = pre

            while current:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left
                
                current = current.next
            
            pre = pre.left
        
        return root
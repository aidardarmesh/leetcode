from typing import *


class TrieNode:
    
    def __init__(self):
        self.val = 0
        self.children = {}

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        
        for c in key:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.val = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        
        for c in prefix:
            if not c in cur.children:
                return 0
            cur = cur.children[c]
        
        def sum_rec(root):
            if root is None:
                return 0
            
            sum = root.val
            
            for c in root.children:
                sum += sum_rec(root.children[c])
            
            return sum
        
        return sum_rec(cur)

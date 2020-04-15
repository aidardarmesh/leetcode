from typing import *

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None
        self.ints = {}
    
    def _insert(self, root, val):
        if not root or root.val == val:
            return Node(val)
        
        if root.val < val:
            root.right = self._insert(root.right, val)
        else:
            root.left = self._insert(root.left, val)
        
        return root
    
    def _search(self, root, val):
        if not root or root.val == val:
            return root
        
        if root.val < val:
            return self._search(root.right, val)
        
        return self._search(root.left, val)
    
    def _successor(self, root):
        root = root.right
        
        while root and root.left:
            root = root.left
        
        return root
    
    def _predecessor(self, root):
        root = root.left
        
        while root and root.right:
            root = root.right
        
        return root
    
    def _delete(self, root, val):
        if not root:
            return root
        
        if root.val < val:
            root.right = self._delete(root.right, val)
        elif root.val > val:
            root.left = self._delete(root.left, val)
        else:
            if not root.left and not root.right:
                return None
            elif root.left:
                p = self._predecessor(root)
                root.val = p.val
                root.left = self._delete(root.left, p.val)
            else:
                s = self._successor(root)
                root.val = s.val
                root.right = self._delete(root.right, s.val)
        
        return root
    
    def lower_key(self, root, val):
        if not root:
            return root
        
        while root and root.val > val:
            root = root.left
        
        while root and root.right and root.right.val < val:
            root = root.right
        
        return root
    
    def higher_key(self, root, val):
        if not root:
            return root
        
        while root and root.val < val:
            root = root.right
        
        while root and root.left and root.left.val > val:
            root = root.left
        
        return root

    def addNum(self, val: int) -> None:
        if self._search(self.root, val):
            return
        
        lower = self.lower_key(self.root, val)
        lower = lower.val if lower else None
        higher = self.higher_key(self.root, val)
        higher = higher.val if higher else None
        
        if lower and higher and self.ints[lower] + 1 == val and val + 1 == higher:
            self.ints[lower] = self.ints[higher]
            self.root = self._delete(self.root, higher)
            del self.ints[higher]
        elif lower and self.ints[lower] + 1 >= val:
            self.ints[lower] = max(self.ints[lower], val)
        elif higher and val + 1 == higher:
            self.ints[val] = self.ints[higher]
            self.root = self._delete(self.root, higher)
            del self.ints[higher]
        else:
            self.root = self._insert(self.root, val)
            self.ints[val] = val

    def getIntervals(self) -> List[List[int]]:
        return [[start, self.ints[start]] for start in self.ints]


obj = SummaryRanges()
obj.addNum(1)
print(obj.getIntervals())
obj.addNum(3)
print(obj.getIntervals())
obj.addNum(7)
print(obj.getIntervals())
obj.addNum(2)
print(obj.getIntervals())
obj.addNum(6)
print(obj.getIntervals())

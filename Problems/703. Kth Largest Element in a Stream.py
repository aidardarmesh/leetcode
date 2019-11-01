from typing import *


class TreeNode:
    def __init__(self, val: int, cnt: int):
        self.val = val
        self.cnt = cnt
        self.left = None
        self.right = None


class KthLargest:
    class KthLargest:
    def insert(self, root, val):
        if root == None:
            return TreeNode(val, 1)
        
        if root.val < val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        
        root.cnt += 1
        
        return root
    
    def search(self, root, k):
        '''m is size of right subtree'''
        m = root.right.cnt if root.right else 0
        
        '''root is m+1 largest in BST'''
        if k == m+1:
            return root.val
        
        if k <= m:
            '''find klargest in right subtree'''
            return self.search(root.right, k)
        else:
            '''find (k-m-1)th largest in left subtree'''
            return self.search(root.left, k-m-1)
    
    def __init__(self, k, nums):
        self.k = k
        self.root = None
        
        for num in nums:
            self.root = self.insert(self.root, num)
    
    def add(self, val):
        self.root = self.insert(self.root, val)
        
        return self.search(self.root, self.k)


kthLargest = KthLargest(3, [4,5,8,2])
assert kthLargest.add(3) == 4
assert kthLargest.add(5) == 5
assert kthLargest.add(5) == 5
assert kthLargest.add(10) == 5
assert kthLargest.add(9) == 8
assert kthLargest.add(4) == 8
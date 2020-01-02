from typing import *

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.size = 0
    
    def height(self, root):
        if not root:
            return 0
        
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        
        return self.height(root.left) - self.height(root.right)
    
    def rotate_left(self, z):
        y = z.right
        T = y.left
        
        # rotation
        y.left = z
        z.right = T
        
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        return y
    
    def rotate_right(self, z):
        y = z.left
        T = y.right
        
        # rotation
        y.right = z
        z.left = T
        
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        return y
    
    def insert(self, root, val):
        if not root:
            self.size += 1
            return TreeNode(val)
        
        if val <= root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        
        balance = self.get_balance(root)
        
        # left left
        if balance > 1 and val <= root.left.val:
            root = self.rotate_right(root)
        # left right
        elif balance > 1 and val > root.left.val:
            root.left = self.rotate_left(root.left)
            root = self.rotate_right(root)
        # right right
        elif balance < -1 and val > root.right.val:
            root = self.rotate_left(root)
        # right left
        elif balance < -1 and val <= root.right.val:
            root.right = self.rotate_right(root.right)
            root = self.rotate_left(root)
        
        return root
    
    def successor(self, root):
        while root and root.left:
            root = root.left
        
        return root
    
    def predecessor(self, root):
        while root and root.right:
            root = root.right
        
        return root
    
    def delete(self, root, val):
        if not root:
            return root
        
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if not root.left and not root.right:
                self.size -= 1
                root = None
            elif root.right:
                s = self.successor(root.right)
                root.val = s.val
                root.right = self.delete(root.right, s.val)
            else:
                p = self.predecessor(root.left)
                root.val = p.val
                root.left = self.delete(root.left, p.val)
        
        balance = self.get_balance(root)
        
        # left left
        if balance > 1 and self.get_balance(root.left) >= 0:
            root = self.rotate_right(root)
        # left right
        elif balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            root = self.rotate_right(root)
        # right right
        elif balance < -1 and self.get_balance(root.right) < 0:
            root = self.rotate_left(root)
        # right left
        elif balance < -1 and self.get_balance(root.right) >= 0:
            root = self.rotate_right(root.right)
            root = self.rotate_left(root)
        
        return root
    
    def larger(self, root, target):
        if not root:
            return root
        
        if root.val == target:
            return root
        elif root.val < target:
            return self.larger(root.right, target)
        else:
            left_res = self.larger(root.left, target)
            return left_res if left_res else root
    
    def less(self, root, target):
        if not root:
            return root
        
        if root.val == target:
            return root
        elif root.val > target:
            return self.less(root.left, target)
        else:
            right_res = self.less(root.right, target)
            return right_res if right_res else root

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        avl = AVLTree()
        root = None
        n = len(nums)
        
        for i in range(n):
            s = avl.larger(root, nums[i])
            
            if s and abs(s.val-nums[i]) <= t:
                return True
            
            p = avl.less(root, nums[i])
            
            if p and abs(p.val-nums[i]) <= t:
                return True
            
            root = avl.insert(root, nums[i])
            
            if avl.size > k:
                root = avl.delete(root, nums[i-k])
        
        return False

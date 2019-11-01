from typing import *


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.root = None

        for val in nums:
            self.__insert(val)
    
    def __insert(self, val: int):
        if self.root == None:
            self.root = TreeNode((val, 1))
            return
        
        node = self.root

        while node and node.val[0] != val:
            if node.val[0] < val:
                if not node.right:
                    node.right = TreeNode((val, 1))
                    return
                else:
                    node = node.right
            elif node.val[0] > val:
                if not node.left:
                    node.left = TreeNode((val, 1))
                    return
                else:
                    node = node.left
            else:
                node.val[1] += 1
                return
    
    def __klargest(self):
        stack = []
        k = self.k
        node = self.root

        while stack or node:
            if node:
                stack.append(node)
                node = node.right
            elif stack:
                node = stack.pop()
                val, count = node.val[0], node.val[1]
                k -= count
                if k <= 0:
                    return node.val[0]
                node = node.left
        
        return None
    
    def rev_order(self):
        res = []
        stack = []
        node = self.root

        while stack or node:
            if node:
                stack.append(node)
                node = node.right
            elif stack:
                node = stack.pop()
                res.append(node.val)
                node = node.left
        
        return res

    def add(self, val: int) -> int:
        self.__insert(val)

        print(self.rev_order())

        return self.__klargest()


kthLargest = KthLargest(3, [4,5,8,2])
print(kthLargest.add(3))
print(kthLargest.add(5))
# assert kthLargest.add(5) == 5
# assert kthLargest.add(10) == 5
# assert kthLargest.add(9) == 8
# assert kthLargest.add(4) == 8
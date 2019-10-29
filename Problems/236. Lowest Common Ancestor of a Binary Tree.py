from typing import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Рассуждение: https://www.youtube.com/watch?v=py3R23aAPCA

Ключ к решению - рассмотреть каждую ноду в качестве общего предка. 
Рекурсия будет передавать результаты снизу вверх. Поэтому первый найденный
предок будет ближайшим.

Если текущая нода не существует (равна None), значит мы достигли
конца дерева и надо выйти (вернуть None, т.к. поиск в данном под-дереве
не привел к нахождению p или q). 

Если нода является p или q, то нода - общий предок (по условию задачи).

Если нода не является p или q, то она может быть предком для p или q, 
но чтобы убедиться в этом, надо поискать p и q в левом и правом поддереве.

Если p или q были найдены в обоих поддеревьях, то текущая нода является 
общим предком.

Если p или q были найдены только в левом поддереве или только в правом, 
то текущая нода не ближайший общий предок и должна передать результат выше.

Если совсем ничего не было найдено, вернуть None, т.к. нода не является предком
p и q вообще.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p, q)
    
    def find(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return root
        
        if root == p or root == q:
            return root
        
        left_subtree = self.find(root.left, p, q)
        right_subtree = self.find(root.right, p, q)
        
        if left_subtree and right_subtree:
            return root
        
        if left_subtree:
            return left_subtree
        
        if right_subtree:
            return right_subtree
        
        return None
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#          F
#        /   \
#       B     G
#      / \     \
#     A   D     I
#       / \    /
#      C   E  H

F = TreeNode('F')
B = TreeNode('B')
G = TreeNode('G')
A = TreeNode('A')
D = TreeNode('D')
C = TreeNode('C')
E = TreeNode('E')
I = TreeNode('I')
H = TreeNode('H')
F.left = B
F.right = G
B.left = A
B.right = D
D.left = C
D.right = E
G.right = I
I.left = H

def pre_order_iter(root):
    if not root:
        return []

    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)
    
    return res

print(pre_order_iter(F))
# ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']

def in_order_iter(root):
    if not root:
        return []

    res = []
    stack = []
    node = root

    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right
    
    return res

print(in_order_iter(F))
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

def post_order_iter(root):
    if not root:
        return []
    
    res = []
    stack = []
    node = root
    visited = set()

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()

            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                res.append(node.val)
                visited.add(node)
                node = None
    
    return res

print(post_order_iter(F))
# ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']

def level_order(root):
    from collections import deque

    if not root:
        return []
    
    res = []
    deq = deque()
    deq.append(root)

    while deq:
        size = len(deq)
        level = []

        for _ in range(size):
            node = deq.popleft()
            level.append(node.val)
            
            if node.left:
                deq.append(node.left)
            
            if node.right:
                deq.append(node.right)
        
        res.append(level)
    
    return res

print(level_order(F))
# [['F'], ['B', 'G'], ['A', 'D', 'I'], ['C', 'E', 'H']]

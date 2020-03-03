class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
def search(root, val):
    if not root or root.val == val:
        return root
    
    if root.val < val:
        return search(root.right, val)
    
    return search(root.left, val)

def search_iter(root, val):
    while root and root.val != val:
        if root.val < val:
            root = root.right
        else:
            root = root.left
    
    return root

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if root.val < val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    
    return root

def insert_iter(root, val):
    node = root

    while node:
        if node.val < val:
            if not node.right:
                node.right = TreeNode(val)
                return root
            else:
                node = node.right
        else:
            if not node.left:
                node.left = TreeNode(val)
                return root
            else:
                node = node.left
    
    return root

def successor(root):
    root = root.right

    while root and root.left:
        root = root.left
    
    return root

def predecessor(root):
    root = root.left

    while root and root.right:
        root = root.right
    
    return root

def delete(root, val):
    if not root:
        return root
    
    if root.val < val:
        root.right = delete(root.right, val)
    elif root.val > val:
        root.left = delete(root.left, val)
    else:
        if not root.left and not root.right:
            return None
        elif root.right:
            s = successor(root)
            root.val = s.val
            root.right = delete(root.right, s.val)
        else:
            p = predecessor(root)
            root.val = p.val
            root.left = delete(root.left, p.val)
    
    return root

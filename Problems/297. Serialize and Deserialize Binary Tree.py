from typing import *

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        queue, res = [root], []
        size = len(queue)
        
        while any(queue):
            for _ in range(size):
                node = queue.pop(0)
                
                if node:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append('None')
                    queue.append(None)
                    queue.append(None)
            
            size *= 2
        
        return " ".join(res)
        
    def deserialize(self, data):
        if not data:
            return None
        
        data_list = data.split()
        root = TreeNode(int(data_list.pop(0)))
        root_nodes = [root]
        
        while data_list:
            size = len(root_nodes)

            for _ in range(size):
                node = root_nodes.pop(0)
                left = data_list.pop(0)
                right = data_list.pop(0)

                if not node:
                    continue
                
                if left != 'None':
                    left = TreeNode(int(left))
                    node.left = left
                    root_nodes.append(left)
                else:
                    root_nodes.append(None)
                
                if right != 'None':
                    right = TreeNode(int(right))
                    node.right = right
                    root_nodes.append(right)
                else:
                    root_nodes.append(None)
        
        return root

c = Codec()

node5 = TreeNode(5)
node5.left = TreeNode(2)
node5.right = TreeNode(3)
node5.right.left = TreeNode(2)
node5.right.right = TreeNode(4)
node5.right.left.left = TreeNode(3)
node5.right.left.right = TreeNode(1)

s = c.serialize(node5)
print(c.serialize(node5))
print(c.deserialize(s))
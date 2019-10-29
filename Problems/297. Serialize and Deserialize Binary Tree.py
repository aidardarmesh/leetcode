from typing import *

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ''

        queue, res = [root], []

        while any(queue):
            node = queue.pop(0)

            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        
        return ' '.join(res)
        
    def deserialize(self, data):
        if not data:
            return None
        
        data_list = data.split()
        root = node = TreeNode(int(data_list.pop(0)))
        queue = [root]

        while data_list and queue:
            node = queue.pop(0)

            if data_list:
                left = data_list.pop(0)
                if left != 'None':
                    left = TreeNode(int(left))
                    node.left = left
                    queue.append(left)
            
            if data_list:
                right = data_list.pop(0)
                if right != 'None':
                    right = TreeNode(int(right))
                    node.right = right
                    queue.append(right)

        return root

c = Codec()

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

print(c.serialize(node))

node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(3)

print(c.serialize(node))

node = None

print(c.serialize(node))

s = '1 2 3'
print(c.deserialize(s).val)

s = ''
print(c.deserialize(s))

s = '1 None 2 3'
print(c.deserialize(s).val)

s = '5 4 7 3 None 2 None -1 None 9'
print(c.deserialize(s).val)

s = '1 2 3 None None 4 5'
print(c.deserialize(s).val)
from typing import *

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.cnt = 0
        self.prev = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cap = capacity
        self.size = 0
        self.head = Node(-1, -1)
        self.head.cnt = float('inf')
        self.tail = Node(-1, -1)
        self.tail.cnt = float('-inf')
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _up(self, node):
        prev = node.prev

        while prev and prev.cnt <= node.cnt:
            prev = prev.prev
        
        # deleting node from current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # inserting after prev
        node.next = prev.next
        node.prev = prev
        prev.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if not key in self.map:
            return -1
        
        node = self.map[key]
        node.cnt += 1
        self._up(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        
        if key in self.map:
            node = self.map[key]
            node.val = value
            node.cnt += 1
            self._up(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            node.cnt += 1
            self.size += 1

            if self.cap < self.size:
                pre_tail = self.tail.prev
                pre_tail.prev.next = self.tail
                self.tail.prev = pre_tail.prev
                del self.map[pre_tail.key]
                self.size -= 1
            
            pre_tail = self.tail.prev
            pre_tail.next = node
            node.prev = pre_tail
            node.next = self.tail
            self.tail.prev = node

cache = LFUCache(2)
cache.put(1,1)
cache.put(2,2)
assert cache.get(1) == 1
cache.put(3,3)
assert cache.get(2) == -1
assert cache.get(3) == 3
cache.put(4,4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4

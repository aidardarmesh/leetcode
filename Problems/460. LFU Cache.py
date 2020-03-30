from typing import *
from collections import defaultdict

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:

    def __init__(self):
        self._head = Node(-1, -1)
        self._tail = Node(-1, -1)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def __len__(self):
        return self._size
    
    def appendleft(self, node):
        node.next = self._head.next
        node.prev = self._head
        node.next.prev = node
        self._head.next = node
        self._size += 1

    def pop(self, node=None):
        if not self._size:
            return
        
        if not node:
            node = self._tail.prev
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

        return node


class LFUCache:

    def __init__(self, capacity: int):
        self._node = {}
        self._freq = defaultdict(DLL)
        self._minfreq = 0
        self._capacity = capacity
        self._size = 0
    
    def _update(self, node):
        freq = node.freq
        self._freq[freq].pop(node)

        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        self._freq[node.freq].appendleft(node)

    def get(self, key):
        if not key in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
            
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].appendleft(node)
            self._minfreq = 1
            self._size += 1


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

cache = LFUCache(3)
cache.put(1,1)
cache.put(2,2)
cache.put(3,3)
cache.put(4,4)
assert cache.get(4) == 4
assert cache.get(3) == 3
assert cache.get(2) == 2
assert cache.get(1) == -1
cache.put(5,5)
assert cache.get(1) == -1
assert cache.get(2) == 2
assert cache.get(3) == 3
assert cache.get(4) == -1
assert cache.get(5) == 5

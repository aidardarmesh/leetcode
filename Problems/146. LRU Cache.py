from typing import *

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        # key: node
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _add_node(self, node):
        neigh = self.head.next
        node.next = neigh
        node.prev = self.head
        self.head.next = node
        neigh.prev = node
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_last(self):
        last = self.tail.prev
        self._remove_node(last)
        del self.cache[last.key]

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_head(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            self.size += 1
            node = ListNode(key, value)
            self.cache[key] = node
            self._add_node(node)
            
            if self.size > self.capacity:
                self._pop_last()
                self.size -= 1

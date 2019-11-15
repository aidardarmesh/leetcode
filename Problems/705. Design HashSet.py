from typing import *


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 1_000
        self.buckets = [[] for _ in range(self.n)]
    
    def _hash(self, key):
        return key % self.n

    def add(self, key: int) -> None:
        idx = self._hash(key)
        
        if not key in self.buckets[idx]:
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = self._hash(key)
        
        return key in self.buckets[idx]


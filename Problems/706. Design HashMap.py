from typing import *


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 1_000
        self.buckets = [[] for _ in range(self.n)]  # bucket is list and elem is bucket is also list
    
    def _hash(self, key):
        return key % self.n

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self._hash(key)

        for elem in self.buckets[idx]:
            if elem[0] == key:
                elem[1] = value
                return
        
        self.buckets[idx].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = self._hash(key)

        for elem in self.buckets[idx]:
            if elem[0] == key:
                return elem[1]
        
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self._hash(key)

        for i, elem in enumerate(self.buckets[idx]):
            if elem[0] == key:
                self.buckets[idx].pop(i)
                return


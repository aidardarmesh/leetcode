from typing import *


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n_buckets = 1_000
        self.buckets = [set() for _ in range(self.n_buckets)]  # each bucket is set
    
    def __hash(self, key):
        return key % self.n_buckets

    def add(self, key: int) -> None:
        idx = self.__hash(key)
        
        self.buckets[idx].add(key)

    def remove(self, key: int) -> None:
        idx = self.__hash(key)
        
        self.buckets[idx].discard(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = self.__hash(key)
        
        return key in self.buckets[idx]


from typing import *


class Pair:
        
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 1_000
        self.buckets = [[] for _ in range(self.n)]  # bucket is list and elem is bucket is also list
    
    def _hash(self, key):
        return key % self.n
    
    def _index(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        
        for i, pair in enumerate(bucket):
            if pair.key == key:
                return bucket, i
        
        return bucket, -1

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket, idx = self._index(key)
        
        if idx >= 0:
            bucket[idx].val = value
            return
        
        bucket.append(Pair(key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket, idx = self._index(key)

        if idx < 0:
            return -1
        
        return bucket[idx].val

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket, idx = self._index(key)
        
        if idx < 0:
            return
        
        bucket.pop(idx)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
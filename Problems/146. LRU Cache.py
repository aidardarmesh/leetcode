from typing import *
import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)

            return self.od[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        self.od[key] = value
        self.od.move_to_end(key)

        if len(self.od) > self.capacity:
            self.od.popitem(last=False)

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
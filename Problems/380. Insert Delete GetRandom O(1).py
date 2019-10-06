from typing import *
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.set:
            self.set.add(val)

            return True
        
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set:
            self.set.discard(val)
            
            return True
        
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.sample(self.set, 1)[0]

r = RandomizedSet()
print(r.insert(1)) # True
print(r.remove(2)) # False
print(r.insert(2)) # True
print(r.getRandom())
print(r.remove(1)) # True
print(r.insert(2)) # False
print(r.getRandom()) # 2
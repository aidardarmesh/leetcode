from typing import *

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        
        self.map[val] = len(self.data)
        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.map:
            return False
        
        last_val, idx = self.data[-1], self.map[val]
        self.data[idx], self.map[last_val] = last_val, idx
        
        self.data.pop()
        del self.map[val]
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand_idx = random.randrange(len(self.data))

        return self.data[rand_idx]

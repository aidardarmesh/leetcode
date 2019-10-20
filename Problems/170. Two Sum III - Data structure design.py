from typing import *

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        count = self.nums.get(number, 0)

        if count == 1:
            self.nums[number] += 1
        else:
            self.nums[number] = 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.nums:
            if value-key == key:
                if self.nums[key] == 2:
                    return True
            else:
                if value-key in self.nums:
                    return True
        
        return False
        

s = TwoSum()

s.add(1)
s.add(3)
s.add(5)
assert s.find(4) == True
assert s.find(7) == False

s = TwoSum()
s.add(0)
s.add(-1)
s.add(1)
assert s.find(0) == True

s = TwoSum()
s.add(0)
s.add(0)
assert s.find(0) == True

s = TwoSum()
s.add(3)
s.add(2)
s.add(1)
assert s.find(2) == False
assert s.find(3) == True
assert s.find(4) == True
assert s.find(5) == True
assert s.find(6) == False
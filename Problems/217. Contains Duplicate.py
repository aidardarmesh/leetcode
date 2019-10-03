from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))

s = Solution()

assert s.containsDuplicate([1,2,3,1]) == True
assert s.containsDuplicate([1,2,3,4]) == False
assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
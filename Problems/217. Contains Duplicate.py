from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set()

        for num in nums:
            if num in uniques:
                return True
            else:
                uniques.add(num)
        
        return False

s = Solution()

assert s.containsDuplicate([1,2,3,1]) == True
assert s.containsDuplicate([1,2,3,4]) == False
assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
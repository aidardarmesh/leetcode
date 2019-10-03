from typing import *

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        first, contains = {}, False

        for i, num in enumerate(nums):
            if num in first:
                if i - first[num] > k:
                    first[num] = i
                else:
                    contains = True
            else:
                first[num] = i
        
        return contains

s = Solution()

assert s.containsNearbyDuplicate([1,2,3,1], 3) == True
assert s.containsNearbyDuplicate([1,0,1,1], 1) == True
assert s.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
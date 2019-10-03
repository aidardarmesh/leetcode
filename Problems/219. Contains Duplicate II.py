from typing import *

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}

        for i, num in enumerate(nums):
            if num in last and i - last[num] <= k:
                return True

            last[num] = i
        
        return False

s = Solution()

assert s.containsNearbyDuplicate([1,2,3,1], 3) == True
assert s.containsNearbyDuplicate([1,0,1,1], 1) == True
assert s.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
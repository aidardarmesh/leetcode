from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, last = 0, float('-inf')
        
        for num in nums:
            if last != num:
                last = num
                nums[k] = num
                k += 1
        
        return k

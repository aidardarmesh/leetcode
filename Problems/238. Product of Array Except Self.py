from typing import *

class Solution:
    def product(self, nums: List[int]) -> int:
        prod = 1

        for num in nums:
            prod *= num
        
        return prod
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            res.append(self.product(nums[:i] + nums[i+1:]))
        
        return res

s = Solution()

assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
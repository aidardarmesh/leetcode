from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output, prod = [], 1

        for i in range(len(nums)):
            output.append(prod)
            prod *= nums[i]
        
        prod = 1

        for i in range(len(nums)-1, -1, -1):
            output[i] *= prod
            prod *= nums[i]
        
        return output


s = Solution()

assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert s.productExceptSelf([1,2]) == [2,1]
assert s.productExceptSelf([1,0]) == [0,1]
assert s.productExceptSelf([0,0]) == [0,0]
assert s.productExceptSelf([-1,-1,-1,-1]) == [-1,-1,-1,-1]
assert s.productExceptSelf([-1,2,-3,4]) == [-24,12,-8,6]
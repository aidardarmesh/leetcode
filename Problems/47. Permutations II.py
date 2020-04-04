from typing import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            if not nums:
                return nums

            if len(nums) == 1:
                return [nums]

            res = []

            for i in range(len(nums)):
                m = nums[i]
                rem = nums[:i] + nums[i+1:]

                for perm in helper(rem):
                    res.append([m] + perm)

            return res
        
        res = []
        perms = helper(nums)
        unique_serials = set()
        
        for perm in perms:
            perm_serial = ','.join([str(num) for num in perm])
            
            if not perm_serial in unique_serials:
                res.append(perm)
                unique_serials.add(perm_serial)
        
        return res

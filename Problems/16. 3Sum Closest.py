from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff = 999999
        closest_sum = 999999

        for i in range(n-2):
            l = i + 1
            r = n - 1
            
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                mod = abs(target - sum3)

                if mod < min_diff:
                    min_diff = mod
                    closest_sum = sum3

                if sum3 <= target:
                    while l < r and nums[l] == nums[l+1]:
                        l += 1

                    l += 1
                else:
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1

                    r -= 1
        
        return closest_sum

s = Solution()

assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2
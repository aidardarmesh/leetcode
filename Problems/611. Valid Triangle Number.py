from typing import *

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        cnt = 0
        
        for i in range(N-1, 1, -1):
            left, right = 0, i-1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    cnt += right-left
                    right -= 1
                else:
                    left += 1
        
        return cnt

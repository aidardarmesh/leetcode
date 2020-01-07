from typing import *

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        cnt = 0
        
        def bin_search(left, right, x):
            while left <= right:
                mid = (left+right) // 2
                
                if nums[mid] < x:
                    left = mid+1
                else:
                    right = mid-1
            
            return left
        
        for i in range(N):
            for j in range(i+1, N):
                k = bin_search(j+1, N-1, nums[i]+nums[j])
                
                cnt += (k-1) - (j+1) + 1
        
        return cnt

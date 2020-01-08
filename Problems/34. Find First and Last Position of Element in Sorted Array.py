from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_search(left, right, target):
            while left <= right:
                mid = (left+right) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
            return -1
        
        pos = bin_search(0, len(nums)-1, target)
        
        if pos == -1:
            return [-1, -1]
        
        left, right = pos, pos
        
        while left >= 0 and nums[left] == target:
            left -= 1
        
        while right <= len(nums)-1 and nums[right] == target:
            right += 1
        
        return [left+1, right-1]

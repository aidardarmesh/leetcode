from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftmost():
            left, right = 0, len(nums)-1
            candidate = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    candidate = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return candidate
        
        def rightmost():
            left, right = 0, len(nums)-1
            candidate = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    candidate = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return candidate
        
        return [leftmost(), rightmost()]
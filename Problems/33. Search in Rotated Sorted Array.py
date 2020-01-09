from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # target should be in right side
                # we can go right if
                # a. if target fits right side
                # b. it doesn't fit left side
                if target >= nums[left] or nums[mid] <= nums[right]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] < target:
                # target should be in left side
                # we can go left if
                # a. if it fits left side
                # b. it doesn't fit right side
                if target <= nums[right] or nums[left] <= nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
        
        return -1

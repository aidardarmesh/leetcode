from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid
            # logically, we need to go left
            elif nums[mid] > target:
                # target in left if
                # a. it fits left side
                #    or
                # b. no place in right side
                if target >= nums[left] or nums[mid] <= nums[right]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] < target:
                # target in right if
                # a. it fits in right side
                #    or
                # b. no place in left side
                if target <= nums[right] or nums[left] <= nums[mid]:
                    left = mid+1
                # all value in right side are less than target
                # therefore, go left
                else:
                    right = mid-1
        
        return -1

from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index], nums[i] = nums[i], nums[last_non_zero_index]
                last_non_zero_index += 1

a = [0,0,1]

s = Solution()

s.moveZeroes(a)

print(a)

[0,1,0,3,12]
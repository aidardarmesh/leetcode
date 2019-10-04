from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                zeros += 1

        while zeros > 0:
            nums.append(0)
            zeros -= 1

a = [0,0,1]

s = Solution()

s.moveZeroes(a)

print(a)
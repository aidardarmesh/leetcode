from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        summands = {}

        # 9 - 3 = 6, is it in summands? No, write 6 and its index in summands
        # 9 - 4 = 5, is it in summands? No, write 5 and its index in summands
        # 9 - 2 = 7, is it in summands? No, write 2 and its index in summands
        # 9 - 7 = 2, is it in summands? Yes, get summands[2]. It is index of 2 in nums list
        # Return current position and summand position

        for i in range(n):
            summand = target - nums[i]

            if summand in summands:
                return [summands[summand], i]
            else:
                summands[summand]
        
        return indices

s = Solution()
print(s.twoSum([3, 4, 2, 7, 11, 15], 9))
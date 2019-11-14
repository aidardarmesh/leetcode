from typing import *


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # maximum length of larget number in binary repr
        L = len(bin(max(nums)))-2

        

s = Solution()

assert s.findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
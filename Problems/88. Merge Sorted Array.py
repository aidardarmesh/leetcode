from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)

a = [1,0]
b = [2]

s = Solution()
s.merge(a,1,b,1)

print(a)
from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last_non_zero = m-1
        last = len(nums1)-1
        
        while nums2 and last_non_zero >= 0:
            if nums1[last_non_zero] > nums2[len(nums2)-1]:
                nums1[last] = nums1[last_non_zero]
                last_non_zero -= 1
            else:
                nums1[last] = nums2.pop()

            last -= 1
        
        while last_non_zero >= 0:
            nums1[last] = nums1[last_non_zero]
            last_non_zero -= 1
            last -= 1
        
        while nums2:
            nums1[last] = nums2.pop()
            last -= 1
        
        while last >= 0:
            nums1.pop(0)
            last -= 1

a = [1,0]
b = [2]

s = Solution()
s.merge(a,1,b,1)

print(a)
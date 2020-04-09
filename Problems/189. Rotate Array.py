from typing import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not k:
            return nums
        
        n = len(nums)
        k = k % n
        
        def mirror(start, end):
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        mirror(0, n-1)
        mirror(0, k-1)
        mirror(k, n-1)

s = Solution()

data = [1,2,3,4,5,6,7]

s.rotate(data, 3)
assert data == [5,6,7,1,2,3,4]
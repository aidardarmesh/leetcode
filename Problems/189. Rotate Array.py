from typing import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())

s = Solution()

data = [1,2,3,4,5,6,7]

s.rotate(data, 3)
assert data == [5,6,7,1,2,3,4]
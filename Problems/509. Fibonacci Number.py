from typing import *

class Solution:
    def fib(self, N: int) -> int:
        nums = [0, 1]

        if N < 2:
            return nums[N]

        for i in range(2, N+1):
            nums.append(nums[i-2] + nums[i-1])
        
        return nums.pop()

s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
print(s.fib(5))
from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum, freq, n = 0, 0, {0: 1}, len(nums)

        for i in range(n):
            sum += nums[i]

            if sum-k in freq:
                count += freq[sum-k]
            
            freq[sum] = freq.get(sum, 0) + 1
        
        return count

s = Solution()

assert s.subarraySum([1,1,1], 2) == 2
assert s.subarraySum([1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2], 6) == 5
assert s.subarraySum([0,0,0,0,0,0,0,0,0,0], 0) == 55
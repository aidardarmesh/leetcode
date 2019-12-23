from typing import *

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = r = 0
        ans = float('inf')
        
        for num in nums:
            r += num
            l = max(l, num)
        
        while l <= r:
            mid = (l + r) >> 1
            sum_ = 0
            cnt = 1
            
            for num in nums:
                if sum_ + num <= mid:
                    sum_ += num
                else:
                    cnt += 1
                    sum_ = num
            
            if cnt <= m:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

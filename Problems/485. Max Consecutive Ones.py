from typing import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_num = 0
        max_num = 0
        
        for num in nums:
            if num == 1:
                cur_num += 1
            else:
                cur_num = 0
            
            max_num = max(max_num, cur_num)
        
        return max_num

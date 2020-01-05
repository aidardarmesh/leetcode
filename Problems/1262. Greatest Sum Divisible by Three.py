from typing import *

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res, temp, mod_1, mod_2, remove = 0, 0, [], [], float('inf')
        
        for num in nums:
            if num % 3 == 0:
                res += num
            elif num % 3 == 1:
                temp += num
                mod_1.append(num)
            else:
                temp += num
                mod_2.append(num)
        
        mod_1.sort()
        mod_2.sort()
        
        if temp % 3 == 0:
            return res + temp
        elif temp % 3 == 1:
            if len(mod_1):
                remove = min(mod_1[0], remove)
                
            if len(mod_2) > 1:
                remove = min(mod_2[0] + mod_2[1], remove)
        else:
            if len(mod_2):
                remove = min(mod_2[0], remove)
                
            if len(mod_1) > 1:
                remove = min(mod_1[0] + mod_1[1], remove)
        
        return res + temp - remove

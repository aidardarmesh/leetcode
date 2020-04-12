from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits)-1, -1, -1):
            val = digits[i] + carry
            digits[i] = val % 10
            carry = val // 10
        
        if carry:
            return [1] + digits
        
        return digits

s = Solution()

assert s.plusOne([1,2,3]) == [1,2,4]
assert s.plusOne([4,3,2,1]) == [4,3,2,2]
assert s.plusOne([0]) == [1]
assert s.plusOne([9]) == [1,0]
assert s.plusOne([9,9]) == [1,0,0]
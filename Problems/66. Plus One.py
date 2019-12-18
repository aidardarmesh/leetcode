from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res, carry = [], 1

        while digits:
            digit = digits.pop()
            digit += carry

            carry = digit // 10
            digit = digit % 10
            
            res.append(digit)
        
        if carry:
            res.append(carry)
        
        return res[::-1]

s = Solution()

assert s.plusOne([1,2,3]) == [1,2,4]
assert s.plusOne([4,3,2,1]) == [4,3,2,2]
assert s.plusOne([0]) == [1]
assert s.plusOne([9]) == [1,0]
assert s.plusOne([9,9]) == [1,0,0]
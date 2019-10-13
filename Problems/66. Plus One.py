from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res, carry = [], 1

        while digits:
            digit = digits.pop()
            digit += carry

            if digit // 10 == 1:
                digit = digit % 10
                carry = 1
            else:
                carry = 0
            
            res.insert(0, digit)
        
        if carry > 0:
            res.insert(0, carry)
        
        return res

s = Solution()

assert s.plusOne([1,2,3]) == [1,2,4]
assert s.plusOne([4,3,2,1]) == [4,3,2,2]
assert s.plusOne([0]) == [1]
assert s.plusOne([9]) == [1,0]
assert s.plusOne([9,9]) == [1,0,0]
from typing import *

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for numb in range(left, right+1):
            digits = []
            numb_copy = numb

            while numb_copy > 0:
                numb_copy, digit = divmod(numb_copy, 10)
                digits.append(digit)

            self_dividing = True
            
            for digit in digits:
                if digit == 0 or numb % digit != 0:
                    self_dividing = False
            
            if self_dividing:
                res.append(numb)
        
        return res

s = Solution()

# print(s.selfDividingNumbers(1, 22))
print(s.selfDividingNumbers(66, 708))
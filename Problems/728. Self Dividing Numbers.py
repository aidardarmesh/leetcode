from typing import *

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for numb in range(left, right+1):
            self_dividing = True

            for digit in str(numb):
                if digit == '0' or numb % int(digit) != 0:
                    self_dividing = False
            
            if self_dividing:
                res.append(numb)
                    
        return res

s = Solution()

# print(s.selfDividingNumbers(1, 22))
print(s.selfDividingNumbers(66, 708))
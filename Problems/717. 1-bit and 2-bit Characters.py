from typing import *

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        one_bit = True

        while bits:
            if bits[0] == 1:
                bits.pop(0)
                bits.pop(0)
                one_bit = False
            else:
                bits.pop(0)
                one_bit = True
        
        return one_bit

s = Solution()

assert s.isOneBitCharacter([1, 0, 0]) == True
assert s.isOneBitCharacter([1, 1, 1, 0]) == False
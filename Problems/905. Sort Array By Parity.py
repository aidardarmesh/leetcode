from typing import *

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_A = []
        odd_A = []

        for a in A:
            if a % 2 == 0:
                even_A.append(a)
            else:
                odd_A.append(a)
        
        return even_A + odd_A

s = Solution()

assert s.sortArrayByParity([3,1,2,4]) == [2,4,3,1]
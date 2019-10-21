from typing import *

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        A_list = list(A)
        B_list = list(B)
        
        if len(A_list) != len(B_list):
            return False
        
        if len(A_list) == 0:
            return True

        for _ in range(len(A_list)):
            if A_list == B_list:
                return True
            
            A_list.append(A_list.pop(0))
        
        return False

s = Solution()

assert s.rotateString('abcde', 'cdeab') == True
assert s.rotateString('abcde', 'abced') == False
assert s.rotateString('', '') == True
assert s.rotateString('', 'a') == False
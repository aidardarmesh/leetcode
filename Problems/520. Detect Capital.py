from typing import *

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper, lower, first_upper, n = 0, 0, False, len(word)

        for i, char in enumerate(word):
            if "A" <= char and char <= "Z":
                if i == 0:
                    first_upper = True
                
                upper += 1
            elif "a" <= char and char <= "z":
                lower += 1
        
        if lower == n or upper == n or (first_upper and upper == 1):
            return True
        
        return False

s = Solution()

assert s.detectCapitalUse("adsada") == True
assert s.detectCapitalUse("USA") == True
assert s.detectCapitalUse("FlagG") == False
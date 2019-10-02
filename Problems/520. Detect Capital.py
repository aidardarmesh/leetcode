from typing import *

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()

s = Solution()

assert s.detectCapitalUse("adsada") == True
assert s.detectCapitalUse("USA") == True
assert s.detectCapitalUse("FlagG") == False
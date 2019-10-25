from typing import *

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        num1, num2 = list(num1), list(num2)
        rem, dec = 0, 0

        while num1 and num2:
            dec, rem = divmod(int(num1.pop()) + int(num2.pop()) + rem, 10)
            res.insert(0, str(rem))
            rem = dec
        
        while num1:
            dec, rem = divmod(int(num1.pop()) + rem, 10)
            res.insert(0, str(rem))
            rem = dec
        
        while num2:
            dec, rem = divmod(int(num2.pop()) + rem, 10)
            res.insert(0, str(rem))
            rem = dec
        
        if dec > 0:
            res.insert(0, str(dec))
        
        return ''.join(res)


s = Solution()

assert s.addStrings("9999", "") == "9999"
assert s.addStrings("999", "1") == "1000"
assert s.addStrings("999999999", "1") == "1000000000"
assert s.addStrings("13123145134", "2598534589") == "15721679723"
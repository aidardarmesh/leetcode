from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        quot, ans = 0, []
        i, j = len(a)-1, len(b)-1
        
        while i >= 0 and j >= 0:
            val = int(a[i]) + int(b[j]) + quot
            quot, carry = divmod(val, 2)
            ans.append(str(carry))
            i -= 1
            j -= 1
        
        while i >= 0:
            val = int(a[i]) + quot
            quot, carry = divmod(val, 2)
            ans.append(str(carry))
            i -= 1
        
        while j >= 0:
            val = int(b[j]) + quot
            quot, carry = divmod(val, 2)
            ans.append(str(carry))
            j -= 1
        
        if quot:
            ans += ['1']
        
        return ''.join(ans[::-1])

s = Solution()

assert s.addBinary("11", "1") == "100"
assert s.addBinary("1010", "1011") == "10101"
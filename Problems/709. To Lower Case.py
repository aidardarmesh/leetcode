from typing import *

class Solution:
    # using built-in function
    # 
    # def toLowerCase(self, str: str) -> str:
    #     return str.lower()

    def toLowerCase(self, str_in: str) -> str:
        str_out = ""
        ordA = ord('A')
        ordZ = ord('Z')

        for ch in str_in:
            ordCh = ord(ch)

            if ordA <= ordCh and ordCh <= ordZ:
                ch = chr(ord('a') + (ordCh - ordA))
            
            str_out += ch

        return str_out

s = Solution()

assert s.toLowerCase("Hello") == "hello"
assert s.toLowerCase("HELLO") == "hello"
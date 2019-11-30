from typing import *

class Solution:
    def toHexspeak(self, num: str) -> str:
        num = hex(int(num))[2:]
        num = num.upper().replace('0', 'O').replace('1', 'I')
        allowed = set(["A", "B", "C", "D", "E", "F", "I", "O"])
        
        for digit in num:
            if not digit in allowed:
                return "ERROR"
        
        return num

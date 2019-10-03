from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, int_, rem = [], 0, 0
        a = list(map(int, a))
        b = list(map(int, b))

        while a and b:
            sum = a.pop() + b.pop() + int_
            int_ = sum // 2
            rem = sum % 2
            res.insert(0, rem)
        
        while a:
            sum = a.pop() + int_
            int_ = sum // 2
            rem = sum % 2
            res.insert(0, rem)
        
        while b:
            sum = b.pop() + int_
            int_ = sum // 2
            rem = sum % 2
            res.insert(0, rem)
        
        if int_ != 0:
            res.insert(0, int_)
        
        return "".join(list(map(str, res)))

s = Solution()

assert s.addBinary("11", "1") == "100"
assert s.addBinary("1010", "1011") == "10101"
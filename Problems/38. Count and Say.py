from typing import *

class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"

        for i in range(n-1):
            cur = num[0]
            counter = 0
            num_temp = ""

            for digit in num:
                if digit == cur:
                    counter += 1
                else:
                    num_temp += str(counter) + cur
                    cur = digit
                    counter = 1
            
            num_temp += str(counter) + cur
            num = num_temp[:]

        return num

s = Solution()

assert s.countAndSay(1) == "1"
assert s.countAndSay(4) == "1211"
assert s.countAndSay(5) == "111221"
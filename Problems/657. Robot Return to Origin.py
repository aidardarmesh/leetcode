from typing import *

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0

        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "R":
                x += 1
            elif move == "L":
                x -= 1
        
        return x == 0 and y == 0

s = Solution()

assert s.judgeCircle("UD") == True
assert s.judgeCircle("LL") == False
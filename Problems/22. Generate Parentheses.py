from typing import *

class Solution:
    def __init__(self):
        self.parens = []
    
    def generate(self, cur, n_open, n_closed, n):
        if len(cur) == 2*n:
            self.parens.append(cur)
        
        if n_open < n:
            self.generate(cur+"(", n_open+1, n_closed, n)
        
        if n_closed < n_open:
            self.generate(cur+")", n_open, n_closed+1, n)

    def generateParenthesis(self, n: int) -> List[str]:
        self.generate("(", 1, 0, n)

        return self.parens

s = Solution()

assert s.generateParenthesis(3) == [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
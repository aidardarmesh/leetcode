from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(s, n_open, n_closed):
            if n_open < n:
                helper(s+'(', n_open+1, n_closed)
            
            if n_closed < n_open:
                helper(s+')', n_open, n_closed+1)
            
            if n_closed == n:
                res.append(s)
        
        helper('', 0, 0)
        
        return res

s = Solution()

assert s.generateParenthesis(3) == [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        queue = [('', 0, 0)]
        
        while queue:
            s, n_open, n_closed = queue.pop(0)
            
            if n_open < n:
                queue.append((s+'(', n_open+1, n_closed))
            
            if n_closed < n_open:
                queue.append((s+')', n_open, n_closed+1))
            
            if n_closed == n:
                res.append(s)
        
        return res

s = Solution()

assert s.generateParenthesis(3) == [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
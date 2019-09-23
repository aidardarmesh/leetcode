from typing import *

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        level = 0
        S_new = ""
        n = len(S)
        open_idx = 0

        for i in range(0, n):
            if S[i] == "(":
                if level == 0:
                    open_idx = i
                level += 1
            else:
                level -= 1

            if level == 0:
                S_new += S[open_idx+1:i]

        return S_new

s = Solution()

assert s.removeOuterParentheses("(()())(())") == "()()()"
assert s.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
assert s.removeOuterParentheses("()()") == ""
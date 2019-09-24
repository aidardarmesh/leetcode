from typing import *

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        stack = []

        for ch in S:
            if ch == "(":
                stack.append(ch)

                if len(stack) > 1:
                    result += ch
            else:
                stack.pop()

                if len(stack) > 0:
                    result += ch

        return result

s = Solution()

assert s.removeOuterParentheses("(()())(())") == "()()()"
assert s.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
assert s.removeOuterParentheses("()()") == ""
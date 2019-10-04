from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        open_p = []
        parens = { "(" : ")", "[" : "]", "{" : "}" }

        for p in s:
            if p in parens.keys():
                open_p.append(p)
            elif p in parens.values():
                if len(open_p) == 0 or p != parens[open_p.pop()]:
                    return False
            else:
                return False
        
        return open_p == []

s = Solution()

assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
assert s.isValid("([)]") == False
assert s.isValid("{[]}") == True
assert s.isValid("") == True
assert s.isValid("[") == False
assert s.isValid("]") == False
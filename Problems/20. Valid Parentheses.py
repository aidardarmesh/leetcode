from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        open_p = []
        parens = { "(" : ")", "[" : "]", "{" : "}" }

        for p in s:
            if p in parens.keys():
                open_p.append(p)
            else:
                if len(open_p) > 0 and p == parens[open_p.pop()]:
                    continue
                else:
                    return False
                    
        if len(open_p) != 0:
            return False
        
        return True

s = Solution()

assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
assert s.isValid("([)]") == False
assert s.isValid("{[]}") == True
assert s.isValid("") == True
assert s.isValid("[") == False
assert s.isValid("]") == False
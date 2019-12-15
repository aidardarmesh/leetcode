from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_ = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        open_ = set(map_.values())
        
        for c in s:
            if c in open_:
                stack.append(c)
            else:
                if stack:
                    if stack.pop() != map_[c]:
                        return False
                else:
                    return False
        
        return len(stack) == 0

s = Solution()

assert s.isValid("()") == True
assert s.isValid("()[]{}") == True
assert s.isValid("(]") == False
assert s.isValid("([)]") == False
assert s.isValid("{[]}") == True
assert s.isValid("") == True
assert s.isValid("[") == False
assert s.isValid("]") == False
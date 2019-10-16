from typing import *

class Solution:
    def render(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "#":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.render(S) == self.render(T)

s = Solution()

# assert s.backspaceCompare("ab#c", "ad#c") == True
# assert s.backspaceCompare("ab##", "c#d#") == True
# assert s.backspaceCompare("a##c", "#a#c") == True
# assert s.backspaceCompare("a#c", "b") == False
assert s.backspaceCompare("y#fo##f", "y#f#o##f") == True
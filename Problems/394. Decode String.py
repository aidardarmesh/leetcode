from typing import *

class Solution:
    def decodeString(self, s: str) -> str:
        stack, cur_str, cur_num = [], '', ''
        
        for c in s:
            if c.isdigit():
                cur_num += c
            elif c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = ''
            elif c == ']':
                cur_str = int(stack.pop()) * cur_str
                cur_str = stack.pop() + cur_str
                cur_num = ''
            else:
                cur_str += c
        
        return cur_str

from typing import *

class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        res = []
        
        for part in parts:
            if part == '..':
                if res:
                    res.pop()
            elif part == '' or part == '.':
                continue
            else:
                res.append(part)
        
        return '/' + '/'.join(res)

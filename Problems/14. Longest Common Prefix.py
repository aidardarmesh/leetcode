from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        if not strs:
            return res

        chars = list(strs[0])
        i = 0

        for char in chars:
            for str in strs:
                if len(str) > i and str[i] == char:
                    continue
                else:
                    return res
            
            res += char
            i += 1
        
        return res


s = Solution()

assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
assert s.longestCommonPrefix([]) == ""
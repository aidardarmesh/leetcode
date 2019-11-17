from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        strategy is that to get rid of older duplicate
        and try to make current string longer
        '''
        max_len = 0
        d = {}
        cur_str = ''
        
        for i in range(len(s)):
            if not s[i] in cur_str:
                cur_str += s[i]
                d[s[i]] = i
            else:
                cur_str = s[d[s[i]]+1:i+1]
                d[s[i]] = i
            max_len = max(max_len, len(cur_str))
        
        return max_len

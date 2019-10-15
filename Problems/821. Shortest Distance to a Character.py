from typing import *

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # for each index, if char in index is C => min_distance = 0
        # else make two pointers l=cur-1 and r=cur+1
        # until they get bounds or C, l-=1, r+=1
        # min(cur-l,r-cur)

        # find all indices of C in S: [3, 5, 6, 11]
        # for each index get min(abs(3-index),(5-index),...)
        # this one I like more. Eliminates bunch of if-s
        C_occurences, res = [], []

        for i, ch in enumerate(S):
            if ch == C:
                C_occurences.append(i)
        
        for i, ch in enumerate(S):
            pos = min([abs(i-C_index) for C_index in C_occurences])
            res.append(pos)
        
        return res

s = Solution()

assert s.shortestToChar("loveleetcode", 'e') == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
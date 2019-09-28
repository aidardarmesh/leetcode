from typing import *
import heapq, collections

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        res = ""

        for letter, count in counts.most_common():
            res += letter*count
        
        return res

s = Solution()

assert s.frequencySort("tree") == "eetr"
assert s.frequencySort("cccaaa") == "cccaaa"
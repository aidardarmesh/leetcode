from typing import *
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)

        return len(counts) == len(set(counts.values()))

s = Solution()

assert s.uniqueOccurrences([1,2,2,1,1,3]) == True
assert s.uniqueOccurrences([1,2]) == False
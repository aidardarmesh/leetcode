from typing import *
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniques = set()

        counts = collections.Counter(arr)

        for i in counts:
            if counts[i] in uniques:
                return False
            else:
                uniques.add(counts[i])

        return True

s = Solution()

assert s.uniqueOccurrences([1,2,2,1,1,3]) == True
assert s.uniqueOccurrences([1,2]) == False
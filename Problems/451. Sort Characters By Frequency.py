from typing import *
import heapq, collections

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(letter*count for letter, count in collections.Counter(s).most_common())

s = Solution()

assert s.frequencySort("tree") == "eetr"
assert s.frequencySort("cccaaa") == "cccaaa"
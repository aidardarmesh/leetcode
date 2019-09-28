from typing import *
import heapq, collections

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        most_frequent_letters = sorted(counts, key=counts.get, reverse=True)
        res = ""

        for letter in most_frequent_letters:
            res += letter*counts[letter]
        
        return res

s = Solution()

assert s.frequencySort("tree") == "eetr"
assert s.frequencySort("cccaaa") == "cccaaa"
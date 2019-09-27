from typing import *

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        uniques = set()
        
        for a in A:
            if a in uniques:
                return a
            else:
                uniques.add(a)

s = Solution()

assert s.repeatedNTimes([1,2,3,3]) == 3
assert s.repeatedNTimes([2,1,2,5,3,2]) == 2
assert s.repeatedNTimes([5,1,5,2,5,3,5,4]) == 5
from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            # merged is empty or int-s don't overlap
            if len(merged) == 0 or merged[-1][1] < interval[0]:
                merged.append(interval)
            # if overlap
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

s = Solution()

assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6], [8,10], [15,18]]
assert s.merge([[1,4],[4,5]]) == [[1,5]]
assert s.merge([[1,3],[4,5]]) == [[1,3],[4,5]]
assert s.merge([[1,4],[0,4]]) == [[0,4]]
assert s.merge([[1,4],[0,0]]) == [[0,0],[1,4]]
assert s.merge([[1,4],[0,2],[3,5]]) == [[0,5]]
assert s.merge([[1,4],[2,3]]) == [[1,4]]
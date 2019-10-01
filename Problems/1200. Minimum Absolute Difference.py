from typing import *

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_delta = 9999999
        result = []
        n = len(arr)
        arr = sorted(arr)

        for i in range(0, n-1):
            delta = arr[i+1] - arr[i]

            if delta < min_delta:
                result = []
                min_delta = delta

            if delta == min_delta:
                result.append([arr[i], arr[i+1]])

        return result

s = Solution()

assert s.minimumAbsDifference([4,2,1,3]) == [[1,2],[2,3],[3,4]]
assert s.minimumAbsDifference([1,3,6,10,15]) == [[1,3]]
assert s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]) == [[-14,-10],[19,23],[23,27]]
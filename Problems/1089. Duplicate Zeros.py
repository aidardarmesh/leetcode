from typing import *

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        for i in range(n-1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)

        while len(arr) > n:
            arr.pop()

s = Solution()
a = [1,0,2,3,0,4,5,0]
b = [1,2,3]
s.duplicateZeros(a)
s.duplicateZeros(b)
print(a)
print(b)
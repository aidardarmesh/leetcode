from typing import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(arr, k):
            ans = []
            
            if k == 1:
                return [[elem] for elem in arr]
            
            for i in range(len(arr)):
                m = arr[i]
                
                for comb in backtrack(arr[i+1:], k-1):
                    ans.append([m] + comb)
            
            return ans
        
        return backtrack([i for i in range(1, n+1)], k)


from typing import *

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        return [arr[i-1]^arr[j] if i else arr[j] for i, j in queries]

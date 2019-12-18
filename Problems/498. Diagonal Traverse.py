from typing import *

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        from collections import defaultdict
        
        N = len(matrix)
        M = len(matrix[0])
        hills = defaultdict(list)
        ans = []
        
        for i in range(N):
            for j in range(M):
                hills[i+j].append(matrix[i][j])
        
        for i in range(len(hills)):
            if i % 2 == 0:
                ans += hills[i][::-1]
            else:
                ans += hills[i]
        
        return ans

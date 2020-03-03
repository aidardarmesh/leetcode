from typing import *

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        counter = 0
        
        def bin_search(arr):
            left, right = 0, len(arr)-1
            
            while left <= right:
                mid = (left+right)//2
                
                if arr[mid] < 0:
                    right = mid-1
                else:
                    left = mid+1
            
            return left
        
        for arr in grid:
            counter += n - bin_search(arr)
        
        return counter

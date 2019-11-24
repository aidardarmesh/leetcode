from typing import *

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        
        for i in range(len(points)-1):
            start = points[i]
            end = points[i+1]
            
            time += max(abs(end[0]-start[0]), abs(end[1]-start[1]))
        
        return time

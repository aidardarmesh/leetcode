from typing import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = {}
        
        for x, y in points:
            dist[(x,y)] = x**2 + y**2
        
        return sorted(points, key=lambda point: dist[tuple(point)])[:K]

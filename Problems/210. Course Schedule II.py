from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        colors = {i: 0 for i in range(numCourses)}
        adj = {i: [] for i in range(numCourses)}
        ans = []
        
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        def dfs(v):
            if colors[v] == 2:
                return False
            
            colors[v] = 1
            
            for to in adj[v]:
                if colors[to] == 0:
                    if dfs(to):
                        return True
                elif colors[to] == 1:
                    return True
            
            colors[v] = 2
            ans.append(v)
            return False
        
        for v in adj:
            if dfs(v):
                return []
        
        return ans

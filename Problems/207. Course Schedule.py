from typing import *

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # preprocessing, making graph
        graph = defaultdict(list)
        colors = defaultdict(int)
        
        def dfs(s):
            colors[s] = 1
            
            for v in graph[s]:
                if colors[v] == 0:
                    if(dfs(v)):
                        return True
                elif colors[v] == 1:
                    return True
            
            colors[s] = 2
            
            return False
        
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        
        for i in range(numCourses):
            if dfs(i):
                # cycle detected
                return False
        
        for i in range(numCourses):
            if colors[i] != 2:
                return False
        
        return True

from typing import *

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = collections.defaultdict(list)
        
        for i, parent in enumerate(ppid):
            graph[parent].append(pid[i])
        
        ans = [kill]
        
        def dfs(v):
            for to in graph[v]:
                ans.append(to)
                
                dfs(to)
        
        dfs(kill)
        
        return ans

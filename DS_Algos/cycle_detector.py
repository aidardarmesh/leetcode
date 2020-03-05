from typing import *

class CycleDetector:
    '''
    WHITE: vertex is not processed. Initially all vertices are WHITE.
    GRAY: vertex if discovered (not processed).
    BLACK: vertex and all its descendants are procesed.

    While DFS, if we encounter edge from current edge is GRAY,
    then this edge is back-edge and there's cycle. 
    '''
    def __init__(self, n):
        self.n = n
        self.parent = {i: -1 for i in range(self.n)}
        self.colors = {i: 0 for i in range(self.n)}
        self.cycle_start = self.cycle_end = -1
    
    def detect(self, graph):
        def dfs(s):
            self.colors[s] = 1

            for to in graph[s]:
                if self.colors[to] == 0:
                    self.parent[to] = s

                    if dfs(to):
                        return True
                elif self.colors[to] == 1:
                    self.cycle_start = to
                    self.cycle_end = s
                    return True
            
            self.colors[s] = 2

            return False
        
        for i in range(self.n):
            if dfs(i):
                break
        
        if self.cycle_start == -1:
            print('Acyclic')
        else:
            print('Cycle')
            ans = []
            while self.cycle_start != self.cycle_end:
                ans.insert(0, self.cycle_end)
                self.cycle_end = self.parent[self.cycle_end]
            ans.insert(0, self.cycle_start)

        print(ans)

# directed
graph = {
    0: [],
    1: [0,3],
    2: [0],
    3: [4,5],
    4: [5,7],
    5: [6],
    6: [7],
    7: [5],
}

cd = CycleDetector(8)
cd.detect(graph)

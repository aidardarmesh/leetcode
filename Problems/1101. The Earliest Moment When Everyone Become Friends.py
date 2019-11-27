from typing import *

class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = {}
        self.rank = {}
        self.groups = n
    
    def make_set(self, v):
        self.parent[v] = v
        self.rank[v] = 0
    
    def find_set(self, v):
        if v == self.parent[v]:
            return v
        
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]
    
    def union_sets(self, u, v):
        u_root = self.find_set(u)
        v_root = self.find_set(v)

        if u_root == v_root:
            return
        
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[u_root] = v_root
            self.rank[v_root] = self.rank[u_root] + 1

        self.groups -= 1

class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        dsu = DSU(N)

        for i in range(N):
            dsu.make_set(i)
        
        logs = sorted(logs, key=lambda x: x[0])
        
        for timestamp, A, B in logs:
            dsu.union_sets(A, B)
            
            if dsu.groups == 1:
                return timestamp
        
        return -1

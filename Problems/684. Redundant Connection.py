from typing import *

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        redundant = []
        uf = {}
        
        # fulfilling uf
        for node1, node2 in edges:
            uf[node1] = node1
            uf[node2] = node2
        
        def find_set(v):
            if v == uf[v]:
                return v
            
            uf[v] = find_set(uf[v])
            
            return uf[v]
        
        def union_sets(u, v):
            u_root = find_set(u)
            v_root = find_set(v)
            
            if u_root == v_root:
                redundant.append([u,v])
                return
            
            uf[u_root] = v_root
        
        for node1, node2 in edges:
            union_sets(node1, node2)
        
        return redundant.pop() if redundant else []

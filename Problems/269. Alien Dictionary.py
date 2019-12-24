from typing import *

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def helper(first, second):
            i = j = 0
            
            while i < len(first) and j < len(second):
                if first[i] != second[j]:
                    return (first[i], second[j])
                
                i += 1
                j += 1
            
            return None
        
        ans = []
        graph = {}
        alphabet = set(words[0])
        
        for i in range(len(words)-1):
            edge = helper(words[i], words[i+1])
            alphabet = alphabet.union(set(words[i+1]))
            
            if edge:
                src, dest = edge
                
                if not src in graph:
                    graph[src] = [dest]
                else:
                    graph[src].append(dest)
        
        colors = {i: 0 for i in alphabet}
        
        def dfs(v):
            if colors[v] == 2:
                return
            
            colors[v] = 1
            
            if v in graph:
                for to in graph[v]:
                    if colors[to] == 0:
                        if dfs(to):
                            return True
                    elif colors[to] == 1:
                        return True
            
            colors[v] = 2
            ans.append(v)
            return False
        
        for v in graph:
            if dfs(v):
                return ''
        
        ans = ans[::-1]
        
        for v, color in colors.items():
            if color == 0:
                ans.append(v)
        
        return ''.join(ans)

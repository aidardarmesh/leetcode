from typing import *

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        N = len(image)
        M = len(image[0])
        scolor = image[sr][sc]
        visited = set()
        queue = [(sr,sc)]
        
        while queue:
            i, j = queue.pop(0)
            visited.add((i,j))
            image[i][j] = newColor
            
            for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ni < N and 0 <= nj < M:
                    if not (ni,nj) in visited and image[ni][nj] == scolor:
                        queue.append((ni, nj))
            
        return image

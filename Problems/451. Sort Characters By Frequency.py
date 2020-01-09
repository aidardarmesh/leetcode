from typing import *

class Solution:
    def frequencySort(self, s: str) -> str:
        import heapq
        
        heap = []
        ans = []
        cnt = collections.Counter(s)
        
        for char, num in cnt.items():
            heapq.heappush(heap, (-num, char))
        
        for _ in range(len(heap)):
            num, char = heapq.heappop(heap)
            ans.append(char*(-num))
        
        return ''.join(ans)

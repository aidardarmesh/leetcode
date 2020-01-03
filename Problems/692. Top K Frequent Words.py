from typing import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        heap = []

        for word, num in cnt.items():
            heapq.heappush(heap, (-num, word))
        
        return [heapq.heappop(heap) for _ in range(k)]

from typing import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return sorted(collections.Counter(words), key=lambda x: (-cnt[x], x))[:k]

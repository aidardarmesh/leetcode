from typing import *

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c:i for i, c in enumerate(S)}
        start = end = 0
        ans = []
        
        for i, c in enumerate(S):
            end = max(end, last[c])
            
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        
        return ans

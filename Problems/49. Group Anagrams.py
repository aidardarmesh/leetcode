from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            id = "".join(sorted(s))
            
            if not id in d:
                d[id] = []
            
            d[id].append(s)
        
        return [d[id] for id in d]

s = Solution()

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
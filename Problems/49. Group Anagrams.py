from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for str_ in strs:
            key = ''.join(sorted(str_))
            
            if key in d:
                d[key].append(str_)
            else:
                d[key] = [str_]
        
        return d.values()

s = Solution()

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
from typing import *


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def des_key(str_):
            base_ch = str_[0]
            res = []
            
            for ch in str_:
                res.append((ord(ch) - ord(base_ch)) % 26)
            
            return tuple(res)
        
        d = {}
        
        for str_ in strings:
            key = des_key(str_)
            
            if key in d:
                d[key].append(str_)
            else:
                d[key] = [str_]
        
        return d.values()


s = Solution()
print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))

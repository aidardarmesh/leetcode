from typing import *

class Solution:
    def strToDict(self, s: str) -> Dict:
        s_dict = {}

        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        
        return s_dict

    def isAnagram(self, s: str, t: str) -> bool:
        return self.strToDict(s) == self.strToDict(t)     

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        # multiplication of primes gives unrepeatable results
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        
        for s in strs:
            id = 1

            for ch in s:
                id *= primes[ord(ch) - ord('a')]
            
            if not id in d:
                d[id] = []
            
            d[id].append(s)
        
        return [d[id] for id in d]

s = Solution()

print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
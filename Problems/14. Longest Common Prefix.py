from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = {}
        min_len = float('inf')
        
        def insert(node, word):
            for c in word:
                if not c in node:
                    node[c] = {}
                
                node = node[c]
        
        for word in strs:
            min_len = min(min_len, len(word))
            insert(root, word)
        
        ans = []
        
        def traverse(node, ans, depth):
            if not depth or len(node) != 1:
                return ans
            
            for c in node:
                ans.append(c)
                traverse(node[c], ans, depth-1)
            
            return ans
        
        return ''.join(traverse(root, ans, min_len))

s = Solution()

assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
assert s.longestCommonPrefix([]) == ""
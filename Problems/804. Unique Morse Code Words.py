from typing import *

class Solution:
    def encode(self, str_in: str) -> str:
        alph = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = ""
        a_ord = ord('a')

        for ch in str_in:
            code += alph[ord(ch) - a_ord]

        return code
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_codes = set()

        for word in words:
            code = self.encode(word)

            if not code in unique_codes:
                unique_codes.add(code)
        
        return len(unique_codes)

s = Solution()

assert s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2
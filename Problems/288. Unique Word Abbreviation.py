from typing import *


class ValidWordAbbr:
    
    def make_abb(self, word: str) -> str:
        n = len(word)
        
        if n < 2:
            return None
            
        return word[0] + str(n-2) + word[n-1]

    def __init__(self, dictionary: List[str]):
        self.d = {}
        
        for word in dictionary:
            abb = self.make_abb(word)
            
            if not abb:
                continue
            
            if not abb in self.d:
                self.d[abb] = [word]
            else:
                self.d[abb].append(word)

    def isUnique(self, word: str) -> bool:
        abb = self.make_abb(word)
        
        if abb not in self.d or len(self.d[abb]) == 1 and self.d[abb][0] == word:
            return True
        
        return False
        

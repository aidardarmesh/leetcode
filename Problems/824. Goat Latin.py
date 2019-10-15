from typing import *

class Solution:
    def toGoatLatin(self, S: str) -> str:
        res, a_counter = [], 1
        vowels = ['a', 'e', 'i', 'o', 'u']

        for word in S.split():
            ch = word[0].lower()

            if ch in vowels:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            
            word += 'a' * a_counter
            res.append(word)
            a_counter += 1
        
        return ' '.join(res)

s = Solution()

assert s.toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert s.toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
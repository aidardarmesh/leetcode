from typing import *
import collections

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common = A.pop(0)
        common_count = collections.Counter(common)

        for word in A:
            word_count = collections.Counter(word)

            for char in common_count:
                if char in common_count:
                    common_count[char] = min(common_count[char], word_count[char])
                else:
                    common_count[char] = 0
        
        return common_count.elements()

s = Solution()

s.commonChars(["bella","label","roller"]) == ["e","l","l"]
s.commonChars(["cool","lock","cook"]) == ["c","o"]
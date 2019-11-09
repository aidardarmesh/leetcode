from typing import *


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        import re
        
        words = list(map(lambda x: x.lower(), re.findall(r'[\w]+', paragraph)))
        cnt = Counter(words)
        
        for ban_word in banned:
            del cnt[ban_word]
        
        word, appearances = cnt.most_common(1)[0]
        
        return word

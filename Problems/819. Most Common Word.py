from typing import *


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        import re
        
        cnt = Counter(re.findall(r'[\w]+', paragraph.lower()))
        
        for ban_word in banned:
            del cnt[ban_word]
        
        word, appearances = cnt.most_common(1)[0]
        
        return word

from typing import *

from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                int_word = word[:i] + '_' + word[i+1:]
                all_combo_dict[int_word].append(word)
        
        visited = {beginWord: True}
        queue = [(beginWord, 1)]
        
        while queue:
            cur_word, level = queue.pop(0)
            
            for i in range(L):
                int_word = cur_word[:i] + '_' + cur_word[i+1:]
                
                for word in all_combo_dict[int_word]:
                    if word == endWord:
                        return level + 1
                    
                    if not word in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                
                all_combo_dict[int_word] = []
        
        return 0

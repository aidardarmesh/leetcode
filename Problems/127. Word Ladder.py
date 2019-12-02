from typing import *

from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        L = len(beginWord)
        dictionary = set(wordList)
        visited = set([beginWord])
        queue = [(beginWord, 0)]

        while queue:
            word, level = queue.pop(0)

            if word == endWord:
                return level + 1

            for i in range(L):
                for c in alphabet:
                    inter_word = word[:i] + c + word[i+1:]

                    if inter_word in dictionary and not inter_word in visited:
                        queue.append((inter_word, level+1))
                        visited.add(inter_word)
        
        return 0

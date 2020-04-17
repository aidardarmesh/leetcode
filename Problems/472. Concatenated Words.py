from typing import *

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_end = False

        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_end = True
    
    def is_concat(self, word, i, num):
        if i == len(word):
            return num >= 2
        
        node = self.root
        
        for j in range(i, len(word)):
            c = word[j]
            
            if not c in node.children:
                return False
            
            node = node.children[c]
            
            if node.is_end:
                if self.is_concat(word, j+1, num+1):
                    return True
        
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        res = []
        
        for word in words:
            trie.insert(word)
            
        for word in words:
            if trie.is_concat(word, 0, 0):
                res.append(word)
        
        return res

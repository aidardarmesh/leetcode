from typing import *


class TrieNode:
    
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.is_word = True
    
    def searchEngRoot(self, word):
        cur = self.root
        eng_root = ''
        
        for c in word:
            if not c in cur.children:
                return None
            
            cur = cur.children[c]
            eng_root += c
            
            if cur.is_word:
                break
        
        return eng_root


class Solution:
    
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        
        for root_word in dict:
            trie.insert(root_word)
        
        words = sentence.split()
        
        for i, word in enumerate(words):
            replace = trie.searchEngRoot(word)
            
            if replace:
                words[i] = replace
        
        return ' '.join(words)

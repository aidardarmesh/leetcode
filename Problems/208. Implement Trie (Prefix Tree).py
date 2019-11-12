from typing import *


class TrieNode:
    
    def __init__(self, val):
        self.val = val
        self.is_word = False
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        
        for c in word:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        
        for c in prefix:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        
        return True

from typing import *

class TrieNode:
    def __init__(self):
        self.is_end = 0
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_end += 1
    
    def starts_with(self, prefix):
        node = self.root
        
        for c in prefix:
            if not c in node.children:
                return None
            node = node.children[c]
        
        return node
    
    def traverse(self, word, node, lst):
        if not node:
            return
        
        if node.is_end:
            for _ in range(node.is_end):
                lst.append(word)
        
        for c in node.children:
            self.traverse(word+c, node.children[c], lst)
    
    def content(self, prefix):
        lst = []
        node = self.starts_with(prefix)

        if node:
            if node.is_end:
                for _ in range(node.is_end):
                    lst.append(prefix)
            
            for c in node.children:
                self.traverse(prefix+c, node.children[c], lst)
        
        return lst

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        res = []
        
        for prod in products:
            trie.insert(prod)
        
        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            content = trie.content(prefix)
            content = sorted(content)
            content = content[:3]
            res.append(content)
        
        return res

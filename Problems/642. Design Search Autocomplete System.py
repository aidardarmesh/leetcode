# from typing import *


class TrieNode:
    
    def __init__(self):
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
    
    def findPrefixed(self, prefix):
        def find(node):
            res = []
            
            for c in node.children:
                rems = find(node.children[c])
                
                if rems:
                    for rem in rems:
                        res.append(c+rem)
                else:
                    res.append(c)
            
            return res
        
        node = self.root
        
        for c in prefix:
            if not c in node.children:
                return []
            node = node.children[c]
        
        rems = find(node)
        ans = []
        
        for rem in rems:
            ans.append(prefix + rem)
        
        return ans


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.trie = Trie()
        self.hotness = {}
        self.prefix = ""
        self.top_total = 3
        
        for i in range(len(times)):
            self.hotness[sentences[i]] = times[i]
        
        for sentence in sentences:
            self.trie.insert(sentence)

    def input(self, c):
        ans = []
        
        if c == "#":
            self.hotness[self.prefix] = self.hotness.get(self.prefix, 0) + 1
            self.trie.insert(self.prefix)
        else:
            self.prefix += c
            sentences = self.trie.findPrefixed(self.prefix)
            rating = []
            
            for sentence in sentences:
                rating.append((sentence, self.hotness[sentence]))
            
            # sort according to sentence value
            rating = sorted(rating, key=lambda x: x[0])
            
            # sort according to sentence hotness
            n = len(rating)

            for i in range(n-1, 0, -1):
                for j in range(i, 0, -1):
                    if rating[j][1] > rating[j-1][1]:
                        rating[j], rating[j-1] = rating[j-1], rating[j]
            
            for sentence, hotness in rating:
                ans.append(sentence)
            
            ans = ans[:self.top_total]
        
        return ans


system = AutocompleteSystem(["i love you","island","iroman","i love leetcode"], [5,3,2,2])

print(system.input("i"))
print(system.input(" "))
print(system.input("l"))
print(system.input("#"))

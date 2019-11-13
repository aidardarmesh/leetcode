# from typing import *


class TrieNode:
    
    def __init__(self):
        # self.is_end = False
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
        
        # node.is_end = True
    
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
        self.input = ""
        self.top_total = 3
        
        for i in range(len(times)):
            self.hotness[sentences[i]] = times[i]
        
        for sentence in sentences:
            self.trie.insert(sentence)
    
    def __input_ends(self, c):
        ending_chars = ["#"]

        if c in ending_chars:
            return True

        return False

    def inputChar(self, c):
        ans = []
        
        if self.__input_ends(c):
            self.hotness[self.input] = self.hotness.get(self.input, 0) + 1
            self.trie.insert(self.input)
        else:
            self.input += c
            sentences = self.trie.findPrefixed(self.input)
            rating = []
            
            for sentence in sentences:
                rating.append((sentence, self.hotness[sentence]))
            
            # sort according to sentence value
            rating = sorted(rating, key=lambda x: x[0])
            
            # sort according to sentence hotness
            for i in range(len(rating)-1):
                if rating[i][1] < rating[i+1][1]:
                    rating[i], rating[i+1] = rating[i+1], rating[i]
            
            for sentence, hotness in rating:
                ans.append(sentence)
            
            ans = ans[:self.top_total]
        
        return ans


system = AutocompleteSystem(["i love you","island","iroman","i love leetcode"], [5,3,2,2])
print(system.inputChar("i"))
print(system.inputChar(" "))
print(system.inputChar("l"))
print(system.inputChar("#"))

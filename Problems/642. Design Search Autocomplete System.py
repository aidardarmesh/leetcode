# from typing import *


class TrieNode:
    
    def __init__(self):
        self.is_end = False
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

        node.is_end = True
    
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
        ans = []
        
        for c in prefix:
            if not c in node.children:
                return []
            node = node.children[c]
        
        if node.is_end:
            ans.append(prefix)
        
        rems = find(node)
        
        if rems:
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
            self.prefix = ""
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

            for i in range(0, n-1):
                for j in range(0, n-1-i):
                    if rating[j][1] < rating[j+1][1]:
                        rating[j], rating[j+1] = rating[j+1], rating[j]
            
            for sentence, hotness in rating:
                ans.append(sentence)
            
            ans = ans[:self.top_total]
        
        return ans

system = AutocompleteSystem(["i love you","island","iroman","i love leetcode"], [5,3,2,2])

print(system.input("i")) # ["i love you", "island", "i love leetcode"]
print(system.input(" ")) # ["i love you", "i love leetcode"]
print(system.input("a")) # []
print(system.input("#")) # []
print(system.input("i")) # ["i love you", "island", "i love leetcode"]
print(system.input(" ")) # ["i love you", "i love leetcode", "i a"]
print(system.input("a")) # ["i a"]
print(system.input("#")) # []
print(system.input("i")) # ["i love you", "island", "i a"]
print(system.input(" ")) # ["i love you", "i a", "i love leetcode"]
print(system.input("a")) # ["i a"]
print(system.input("#")) # []



system = AutocompleteSystem(["abc","abbc","a"], [3,3,3])

print(system.input("b")) # []
print(system.input("c")) # []
print(system.input("#")) # []
print(system.input("b")) # ["bc"]
print(system.input("c")) # ["bc"]
print(system.input("#")) # []
print(system.input("a")) # ["a", "abbc", "abc"]
print(system.input("b")) # ["abbc", "abc"]
print(system.input("c")) # ["abc"]
print(system.input("#")) # []
print(system.input("a")) # ["abc", "a", "abbc"]
print(system.input("b")) # ["abc", "abbc"]
print(system.input("c")) # ["abc"]
print(system.input("#")) # []

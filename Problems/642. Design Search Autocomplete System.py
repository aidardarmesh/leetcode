# from typing import *


class Node:
    
    def __init__(self, sent, times):
        self.sent = sent
        self.times = times


class Trie:
    
    def __init__(self):
        self.times = 0
        self.children = {}


class AutocompleteSystem:

    def insert(self, trie, sent, times):
        for c in sent:
            if not c in trie.children:
                trie.children[c] = Trie()
            trie = trie.children[c]

        trie.times += times

    def __init__(self, sents, times):
        self.root = Trie()
        self.cur_sent = ""

        for i in range(len(times)):
            self.insert(self.root, sents[i], times[i])
    
    def lookup(self, trie, sent):
        for c in sent:
            if not c in trie.children:
                return []
            trie = trie.children[c]

        lst = []
        self.traverse(sent, trie, lst)

        return lst
    
    def traverse(self, sent, trie, lst):
        if trie.times:
            lst.append(Node(sent, trie.times))

        for c in trie.children:
            self.traverse(sent+c, trie.children[c], lst)

    def input(self, c):
        ans = []
        
        if c == "#":
            self.insert(self.root, self.cur_sent, 1)
            self.cur_sent = ""
        else:
            self.cur_sent += c
            res = self.lookup(self.root, self.cur_sent)

            # sort according to sentence value
            res = sorted(res, key=lambda x: x.sent)
            
            # sort according to sentence hotness
            n = len(res)

            for i in range(0, n-1):
                for j in range(0, n-1-i):
                    if res[j].times < res[j+1].times:
                        res[j], res[j+1] = res[j+1], res[j]
            
            for node in res:
                ans.append(node.sent)
            
            ans = ans[:3]
        
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

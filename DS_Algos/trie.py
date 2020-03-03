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
    
    def search_prefix(self, word):
        node = self.root

        for c in word:
            if not c in node.children:
                return None
            
            node = node.children[c]
        
        return node
    
    def search(self, word):
        node = self.search_prefix(word)

        return node is not None and node.is_end
    
    def starts_with(self, word):
        return self.search_prefix(word) is not None

    def content(self):
        words = []
        node = self.root

        for c in node.children:
            self.traverse(c, node.children[c], words)
        
        return words
    
    def traverse(self, word, node, words):
        if node.is_end:
            words.append(word)
        
        for c in node.children:
            self.traverse(word+c, node.children[c], words)
        

class TrieNode:
    
    def __init__(self):
        self.is_end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_end = True

    def search(self, word: str) -> bool:s
        def contains(node, word):
            for i in range(len(word)):
                c = word[i]
                
                if c == '.' and node.children:
                    for child in node.children.values():
                        if contains(child, word[i+1:]):
                            return True
                    
                    return False
                else:
                    if not c in node.children:
                        return False
                    else:
                        node = node.children[c]
            
            return node.is_end
        
        return contains(self.root, word)

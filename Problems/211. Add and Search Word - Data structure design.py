class TrieNode:
    
    def __init__(self):
        self.is_end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
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

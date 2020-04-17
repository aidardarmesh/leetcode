from typing import *

class File:

    def __init__(self):
        self.data = []
    
    def add_content(self, content):
        self.data.append(content)
    
    def get_content(self):
        return ''.join(self.data)


class Directory:
    
    def __init__(self):
        self.space = {}


class FileSystem:

    def __init__(self):
        self.root = Directory()
        self.root.space[''] = Directory()
    
    def _nodes(self, path):
        if path == '/':
            return ['']
        
        return path.split('/')

    def ls(self, path: str) -> List[str]:
        node = self.root
        
        for name in self._nodes(path):
            node = node.space[name]
        
        if isinstance(node, File):
            return [name]
        
        return sorted(node.space.keys())

    def mkdir(self, path: str) -> None:
        node = self.root
        nodes = self._nodes(path)
        
        for name in nodes:
            if not name in node.space:
                node.space[name] = Directory()
            
            node = node.space[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        nodes = self._nodes(filePath)
        filename = nodes[-1]
        
        for name in nodes[:len(nodes)-1]:
            node = node.space[name]
        
        if not filename in node.space:
            node.space[filename] = File()
        
        node = node.space[filename]
        node.add_content(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        nodes = self._nodes(filePath)
        
        for name in nodes:
            node = node.space[name]
        
        return node.get_content()

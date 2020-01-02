from typing import *

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        m = self.data[-1][1] if self.data else float('-inf')
        self.data.append((x, max(x, m)))

    def pop(self) -> int:
        if len(self.data) > 0:
            x, _ = self.data.pop()
            return x

    def top(self) -> int:
        if len(self.data) > 0:
            return self.data[-1][0]

    def peekMax(self) -> int:
        if len(self.data) > 0:
            return self.data[-1][1]

    def popMax(self) -> int:
        if len(self.data) > 0:
            m = self.data[-1][1]
            temp = []
            
            while self.data:
                x = self.pop()
                
                if x == m:
                    break
                
                temp.append(x)
            
            while temp:
                self.push(temp.pop())
            
            return m

from typing import *

class MinStack:

    def __init__(self):
        self.data = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def push(self, x: int) -> None:
        min_ = self.getMin()
        
        if min_ is None or x < min_:
            min_ = x
        
        self.data.append((x, min_))
        self.size += 1

    def pop(self) -> None:
        if not self.is_empty():
            self.data.pop()
            self.size -= 1

    def top(self) -> int:
        if not self.is_empty():
            return self.data[self.size-1][0]

    def getMin(self) -> int:
        if not self.is_empty():
            return self.data[self.size-1][1]


m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())
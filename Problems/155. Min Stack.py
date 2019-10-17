from typing import *

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return min(self.stack)


m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())
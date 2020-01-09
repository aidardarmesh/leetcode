from typing import *

class MinStack:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        if len(self.data) > 0:
            min_ = self.getMin()
            
            self.data.append((x, min(x, min_)))
        else:
            self.data.append((x, x))

    def pop(self) -> None:
        if len(self.data) > 0:
            return self.data.pop()[0]

    def top(self) -> int:
        if len(self.data) > 0:
            return self.data[-1][0]

    def getMin(self) -> int:
        if len(self.data) > 0:
            return self.data[-1][1]

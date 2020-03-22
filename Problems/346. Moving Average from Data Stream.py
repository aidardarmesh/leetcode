from typing import *

class MovingAverage:

    def __init__(self, size: int):
        from collections import deque
        
        self.size = size
        self.deq = deque()

    def next(self, val: int) -> float:
        if len(self.deq) == self.size:
            self.deq.popleft()
        
        self.deq.append(val)
        
        return sum(self.deq) / len(self.deq)

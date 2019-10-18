from typing import *

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        self.queue.append(val)
        
        if len(self.queue) > self.size:
            item = self.queue.pop(0)
        
        return sum(self.queue)/len(self.size)
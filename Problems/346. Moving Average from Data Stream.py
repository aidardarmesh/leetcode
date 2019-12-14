from typing import *

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.data = [0] * size
        self.head = self.window_sum = self.count = 0

    def next(self, val: int) -> float:
        self.count += 1

        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.data[tail] + val

        self.head = (self.head + 1) % self.size
        self.data[self.head] = val
        
        return self.window_sum / min(self.count, self.size)

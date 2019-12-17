from typing import *

class MyStack:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        holder = []
        count = 0
        
        while self.data:
            holder.append(self.data.pop(0))
            count += 1
        
        count -= 1
        
        while count:
            self.data.append(holder.pop(0))
            count -= 1
        
        if holder:
            return holder.pop(0)

    def top(self) -> int:
        if not self.empty():
            return self.data[len(self.data)-1]
        
        return -1

    def empty(self) -> bool:
        return len(self.data) == 0

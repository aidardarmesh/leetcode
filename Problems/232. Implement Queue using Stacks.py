from typing import *

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        stack_temp = []

        while self.stack:
            stack_temp.append(self.stack.pop())
        
        item = stack_temp.pop()

        while stack_temp:
            self.stack.append(stack_temp.pop())
        
        return item

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0

queue = MyQueue()

queue.push(1)
queue.push(2)
print(queue.peek()) # 1
print(queue.pop()) # 1
print(queue.empty()) # False
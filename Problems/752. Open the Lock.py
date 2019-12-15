from typing import *

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = ['0000']
        dist = 0
        visited = set()
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                lock = queue.pop(0)
                
                if lock in visited or lock in deadends:
                    continue
                
                visited.add(lock)

                if lock == target:
                    return dist
                
                for i in range(4):
                    val = int(lock[i])
                    next_ = (val + 1) % 10
                    prev_ = (val - 1) % 10
                    
                    next_lock = lock[:i] + str(next_) + lock[i+1:]
                    prev_lock = lock[:i] + str(prev_) + lock[i+1:]
                    
                    if not (next_lock in visited or next_lock in deadends):
                        queue.append(next_lock)
                    
                    if not (prev_lock in visited or prev_lock in deadends):
                        queue.append(prev_lock)
            
            dist += 1
        
        return -1

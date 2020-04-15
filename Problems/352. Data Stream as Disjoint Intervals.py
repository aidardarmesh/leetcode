from typing import *

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ints = []
        self.seen = set()

    def addNum(self, val: int) -> None:
        if not val in self.seen:
            self.seen.add(val)
            heapq.heappush(self.ints, [val, val])

    def getIntervals(self) -> List[List[int]]:
        temp = []
        
        while self.ints:
            if not temp:
                temp.append(heapq.heappop(self.ints))
            else:
                start, end = heapq.heappop(self.ints)
                
                if temp[-1][1] + 1 >= start:
                    temp[-1][1] = max(temp[-1][1], end)
                else:
                    temp.append([start, end])
        
        self.ints = temp
        
        return self.ints


obj = SummaryRanges()
obj.addNum(1)
print(obj.getIntervals())
obj.addNum(3)
print(obj.getIntervals())
obj.addNum(7)
print(obj.getIntervals())
obj.addNum(2)
print(obj.getIntervals())
obj.addNum(6)
print(obj.getIntervals())

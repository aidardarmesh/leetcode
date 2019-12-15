from typing import *

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        from collections import defaultdict
        
        N = len(T)
        ans = [0] * N
        weather = defaultdict(list)
        
        for day, temp in enumerate(T):
            for prev_temp in weather:
                if temp > prev_temp:
                    while weather[prev_temp]:
                        prev_day = weather[prev_temp].pop()
                        ans[prev_day] = day - prev_day
            
            weather[temp].append(day)
        
        return ans

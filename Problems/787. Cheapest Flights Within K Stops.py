from typing import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        import heapq

        graph = collections.defaultdict(list)

        for from_, to, cost in flights:
            graph[from_].append(to, cost)
        
        best = {}
        queue = [(0, -1, src)]

        while queue:
            cost, k, place = heapq.heappop(queue)

            if k > K or cost > best.get((k,place), float('inf')):
                continue
            
            for to, add_cost in graph[place]:
                new_cost = cost + add_cost

                if new_cost < best.get((k+1, to), float('inf')):
                    best[(k+1, to)] = new_cost
                    heapq.heappush(queue, (new_cost, k+1, to))
        
        return -1

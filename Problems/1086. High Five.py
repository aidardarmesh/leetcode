from typing import *
import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        grades, res = {}, []

        for item in items:
            top_grades = grades.get(item[0], [])
            heapq.heappush(top_grades, item[1])
            grades.setdefault(item[0], top_grades)
        
        for id in grades:
            avg = sum(heapq.nlargest(5, grades[id])) // 5
            res.append([id, avg])
        
        return res

s = Solution()

print(s.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
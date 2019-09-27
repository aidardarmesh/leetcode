from typing import *

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        total_profit = i = best_profit = 0
        n_diff = len(difficulty)
        jobs = sorted(list(zip(difficulty, profit)))

        for skill in sorted(worker):
            while i < n_diff and skill >= jobs[i][0]:
                best_profit = max(best_profit, jobs[i][1])

            total_profit += best_profit

        return total_profit

s = Solution()

assert s.maxProfitAssignment(
    [2,4,6,8,10],
    [10,20,30,40,50],
    [4,5,6,7]
) == 100

# edge cases
assert s.maxProfitAssignment(
    [4],
    [100],
    [2]
) == 0

assert s.maxProfitAssignment(
    [4,5,6],
    [10,10,20],
    [2,5]
) == 10

# test from problem
assert s.maxProfitAssignment(
    [66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63],
    [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77],
    [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]
) == 1392
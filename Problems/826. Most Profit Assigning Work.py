from typing import *

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        total_profit = 0
        n_diff = len(difficulty)
        last_profit = 0
        max_diff_index = 0

        # can't use dict, because there can be same difficulty values, but can't in dict
        # therefore, used sorted list with tuples
        diff_profits = sorted(list(zip(difficulty, profit)))

        # if next worker does not ace difficulty, his profit will be same as last one
        # (only if worker and difficulty lists are sorted)
        worker = sorted(worker)
        difficulty = sorted(difficulty)

        for ability in worker:
            while max_diff_index < n_diff and ability >= difficulty[max_diff_index]:
                cur_profit = diff_profits[max_diff_index][1]

                if cur_profit > last_profit:
                    last_profit = cur_profit
                
                max_diff_index += 1
                
            total_profit += last_profit

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
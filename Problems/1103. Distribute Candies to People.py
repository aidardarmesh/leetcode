from typing import *

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i, last = 0, 1
        a = [0 for i in range(num_people)]

        while candies > 0:
            if last > candies:
                last = candies
            
            a[i % num_people] += last
            candies -= last
            last += 1
            i += 1

        return a

s = Solution()

assert s.distributeCandies(7,4) == [1,2,3,1]
assert s.distributeCandies(10,3) == [5,2,3]
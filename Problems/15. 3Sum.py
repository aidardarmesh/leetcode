from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), []
        nums.sort()

        for i in range(n-2):
            l = i+1
            r = n-1

            while l < r:
                sum2 = nums[l] + nums[r]
                sum3 = nums[i] + sum2

                if sum3 < 0:
                    l += 1
                elif sum3 == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])

                    l += 1
                else:
                    r -= 1
        
        return res

s = Solution()
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [
    [-1, -1, 2],
    [-1, 0, 1]
]
assert s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]) == [
    [-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]
]
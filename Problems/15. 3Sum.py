from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r, res = 0, len(nums)-1, []
        nums.sort()

        while l < r:
            sum2 = nums[l] + nums[r]
            min_diff = 99999
            closest = 99999

            for i in range(l+1, r):
                sum3 = sum2 + nums[i]

                if sum3 == 0:
                    if [nums[l], nums[i], nums[r]] not in res:
                        res.append([nums[l], nums[i], nums[r]])
                elif abs(sum3) < min_diff:
                    min_diff = abs(sum3)
                    closest = sum3
            
            if closest < 0:
                l += 1
            else:
                r -= 1
        
        return res

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [
    [-1, 0, 1],
    [-1, -1, 2]
]

# -4 -1 -1 0 1 2
# l = -4, r = 2 => sum = -2, go from l to r exclusively to find t
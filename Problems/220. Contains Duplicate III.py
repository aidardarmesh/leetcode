from typing import *

class TreeNode:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        
        buckets = {}

        for i, num in enumerate(nums):
            if len(buckets) > k:
                b_id_old = nums[i-k-1] // (t+1)
                del buckets[b_id_old]

            b_id = num // (t+1)
            cond1 = b_id in buckets
            cond2 = b_id-1 in buckets and abs(buckets[b_id-1]-num) <= t
            cond3 = b_id+1 in buckets and abs(buckets[b_id+1]-num) <= t

            if cond1 or cond2 or cond3:
                return True

            buckets[b_id] = num
    
        return False


s = Solution()
assert s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) == True
assert s.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2) == True
assert s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) == False
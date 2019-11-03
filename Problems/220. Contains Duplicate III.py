from typing import *

class TreeNode:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False
        
        cache = {}
        
        for i in range(len(nums)):
            if i-k > 0:
                b_id_del = nums[i-k-1]//(t+1)
                del cache[b_id_del]
            
            b_id = nums[i]//(t+1)
            cond1 = b_id in cache
            cond2 = b_id-1 in cache and abs(cache[b_id-1]-nums[i]) <= t
            cond3 = b_id+1 in cache and abs(cache[b_id+1]-nums[i]) <= t

            if cond1 or cond2 or cond3:
                return True
            
            cache[b_id] = nums[i]
        
        return False


s = Solution()
assert s.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) == True
assert s.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2) == True
assert s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) == False
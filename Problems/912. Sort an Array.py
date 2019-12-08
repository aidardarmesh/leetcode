from typing import *

class Solution:
    def merge(self, l1, l2):
        res = []
        
        while l1 and l2:
            if l1[0] <= l2[0]:
                res.append(l1.pop(0))
            else:
                res.append(l2.pop(0))
        
        if l1:
            res += l1
        
        if l2:
            res += l2
        
        return res
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        m = len(nums) // 2
        
        left_list = self.sortArray(nums[:m])
        right_list = self.sortArray(nums[m:])
        
        return self.merge(left_list, right_list)

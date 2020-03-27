from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        prev = []
        res = {}
        
        for i in range(len(nums2)-1, -1, -1):
            found = False
            
            while prev:
                if prev[-1] > nums2[i]:
                    res[nums2[i]] = prev[-1]
                    found = True
                    break
                
                prev.pop()
            
            prev.append(nums2[i])
            
            if not found:
                res[nums2[i]] = -1
                continue
        
        return [res[num] for num in nums1]

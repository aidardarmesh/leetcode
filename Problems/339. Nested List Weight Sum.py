from typing import *

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        sum_ = 0
        depth = 1
        
        def helper(nested, depth):
            sum_ = 0
            
            for val in nested.getList():
                if val.isInteger():
                    sum_ += val.getInteger()*depth
                else:
                    sum_ += helper(val, depth+1)
            
            return sum_
        
        for val in nestedList:
            if val.isInteger():
                sum_ += val.getInteger()*depth
            else:
                sum_ += helper(val, depth+1)
        
        return sum_

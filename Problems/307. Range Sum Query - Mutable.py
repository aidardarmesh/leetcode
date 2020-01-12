from typing import *

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        
        self.N = len(nums)
        self.t = [None for _ in range(4*self.N)]

        def build(v, vl, vr):
            if vl == vr:
                self.t[v] = nums[vl]
                return
            
            vm = (vl + vr) // 2
            build(2*v+1, vl, vm)
            build(2*v+2, vm+1, vr)
            self.t[v] = self.t[2*v+1] + self.t[2*v+2]

        build(0, 0, self.N-1)

    def update(self, i: int, val: int) -> None:
        def modify(v, vl, vr, pos, val):
            if pos < vl or pos > vr:
                return
            
            if pos == vl == vr:
                self.t[v] = val
                return
            
            vm = (vl + vr) // 2
            modify(2*v+1, vl, vm, pos, val)
            modify(2*v+2, vm+1, vr, pos, val)
            self.t[v] = self.t[2*v+1] + self.t[2*v+2]

        modify(0, 0, self.N-1, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def query(v, vl, vr, l, r):
            if r < vl or l > vr:
                return 0
            
            if l <= vl and vr <= r:
                return self.t[v]
            
            vm = (vl + vr) // 2
            ql = query(2*v+1, vl, vm, l, r)
            qr = query(2*v+2, vm+1, vr, l, r)

            return ql + qr

        return query(0, 0, self.N-1, i, j)
    
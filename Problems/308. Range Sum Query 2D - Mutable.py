from typing import *

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        
        self.N = len(matrix)
        self.M = len(matrix[0])
        self.t = [[0]*4*self.M for _ in range(self.N)]
        
        def build(v, vl, vr, row):
            if vl == vr:
                self.t[row][v] = matrix[row][vl]
                return
            
            vm = (vl + vr) // 2
            build(2*v+1, vl, vm, row)
            build(2*v+2, vm+1, vr, row)
            self.t[row][v] = self.t[row][2*v+1] + self.t[row][2*v+2]
        
        for row in range(self.N):
            build(0, 0, self.M-1, row)

    def update(self, row: int, col: int, val: int) -> None:
        def modify(v, vl, vr, pos, val, row):
            if pos < vl or pos > vr:
                return
            
            if pos == vl == vr:
                self.t[row][v] = val
                return
            
            vm = (vl + vr) // 2
            modify(2*v+1, vl, vm, pos, val, row)
            modify(2*v+2, vm+1, vr, pos, val, row)
            self.t[row][v] = self.t[row][2*v+1] + self.t[row][2*v+2]
        
        modify(0, 0, self.M-1, col, val, row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        
        def query(v, vl, vr, l, r, row):
            if r < vl or l > vr:
                return 0
            
            if l <= vl and vr <= r:
                return self.t[row][v]
            
            vm = (vl + vr) // 2
            ql = query(2*v+1, vl, vm, l, r, row)
            qr = query(2*v+2, vm+1, vr, l, r, row)
            
            return ql + qr
        
        for row in range(row1, row2+1):
            ans += query(0, 0, self.M-1, col1, col2, row)
            
        return ans

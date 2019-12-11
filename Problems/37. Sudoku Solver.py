from typing import *

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        from collections import defaultdict
        
        # preprocessing
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        
        def block_id(r, c):
            return r//3*3 + c//3
        
        for r, row in enumerate(board):
            for c, char in enumerate(row):
                if char != '.':
                    rows[r].add(char)
                    cols[c].add(char)
                    blocks[block_id(r, c)].add(char)
        
        def is_valid(val, r, c):
            val = str(val)
            return not (val in rows[r] or val in cols[c] or val in blocks[block_id(r, c)])
        
        def place(val, r, c):
            val = str(val)
            board[r][c] = val
            rows[r].add(val)
            cols[c].add(val)
            blocks[block_id(r, c)].add(val)
        
        def remove(val, r, c):
            val = str(val)
            board[r][c] = '.'
            rows[r].remove(val)
            cols[c].remove(val)
            blocks[block_id(r, c)].remove(val)
        
        def backtrack():
            # board elem-s does not change
            for r, row in enumerate(board):
                for c, char in enumerate(row):
                    if char == '.':
                        for val in range(1, 10):
                            if is_valid(val, r, c):
                                place(val, r, c)
                                solved = backtrack()
                                
                                if solved:
                                    return True
                                
                                remove(val, r, c)
                        
                        return False
            
            return True
        
        backtrack()

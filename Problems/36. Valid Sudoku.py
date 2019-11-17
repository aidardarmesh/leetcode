from typing import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cells = {}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = board[i][j]
                    
                    # is unique in row
                    for k in range(j-1, -1, -1):
                        if val == board[i][k]:
                            return False
                    
                    for k in range(j+1, 9):
                        if val == board[i][k]:
                            return False
                    
                    # is unique in col
                    for k in range(i-1, -1, -1):
                        if val == board[k][j]:
                            return False
                    
                    for k in range(i+1, 9):
                        if val == board[k][j]:
                            return False
                    
                    idx = i // 3 * 3 + j // 3
                    
                    if idx in cells:
                        if val in cells[idx]:
                            return False
                        else:
                            cells[idx].append(val)
                    else:
                        cells[idx] = [val]
        
        return True

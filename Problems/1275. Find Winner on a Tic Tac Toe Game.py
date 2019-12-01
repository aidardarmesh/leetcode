from typing import *

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' ' for i in range(3)] for j in range(3)]
        
        for i, coord in enumerate(moves):
            if i % 2 == 0:
                grid[coord[0]][coord[1]] = 'X'
            else:
                grid[coord[0]][coord[1]] = 'O'
        
        def winner(player):
            if player == 0:
                str_ = 'XXX'
            else:
                str_ = 'OOO'
            
            if     ''.join(grid[0]) == str_ \
                or ''.join(grid[1]) == str_ \
                or ''.join(grid[2]) == str_ \
                or ''.join([grid[0][0],grid[1][0],grid[2][0]]) == str_ \
                or ''.join([grid[0][1],grid[1][1],grid[2][1]]) == str_ \
                or ''.join([grid[0][2],grid[1][2],grid[2][2]]) == str_ \
                or ''.join([grid[0][0],grid[1][1],grid[2][2]]) == str_ \
                or ''.join([grid[0][2],grid[1][1],grid[2][0]]) == str_:
                return True
            else:
                return False
        
        if winner(0):
            return 'A'
        elif winner(1):
            return 'B'
        
        for i in range(3):
            for j in range(3):
                if grid[i][j] == ' ':
                    return 'Pending'
        
        return 'Draw'
        

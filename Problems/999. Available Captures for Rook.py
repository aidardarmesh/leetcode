from typing import *

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        R_i, R_j, pawns = 0, 0, 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    R_i = i
                    R_j = j

        for i in range(R_i-1, -1, -1):
            if board[i][R_j] == "B":
                break
            elif board[i][R_j] == "p":
                pawns += 1
                break
        
        for i in range(R_i+1, 8):
            if board[i][R_j] == "B":
                break
            elif board[i][R_j] == "p":
                pawns += 1
                break

        for j in range(R_j-1, -1, -1):
            if board[R_i][j] == "B":
                break
            elif board[R_i][j] == "p":
                pawns += 1
                break
        
        for j in range(R_j+1, 8):
            if board[R_i][j] == "B":
                break
            elif board[R_i][j] == "p":
                pawns += 1
                break
        
        return pawns

s = Solution()

assert s.numRookCaptures(
    [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
) == 3

assert s.numRookCaptures(
    [
        [".",".",".",".",".",".",".","."],
        [".","p","p","p","p","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","B","R","B","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","p","p","p","p",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
) == 0

assert s.numRookCaptures(
    [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
) == 3
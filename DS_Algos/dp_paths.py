def paths(matrix):
    n = len(matrix)
    m = len(matrix[0])
    map_ = [[0 for j in range(m)] for i in range(n)]

    def count(row, col):
        if not (row < n and col < m) or matrix[row][col]:
            return 0
        
        if row == n-1 and col == m-1:
            return 1
        
        map_[row][col] = count(row+1, col) + count(row, col+1)

        return map_[row][col]

    return count(0, 0)

matrix = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,1,0],
    [0,0,0,0,1,0,0,0],
    [1,0,1,0,0,1,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,1,0,1,0],
    [0,1,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0],
]

print(paths(matrix))

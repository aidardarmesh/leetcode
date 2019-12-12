from typing import *

class Solution:
    def cleanRoom(self, robot):
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def backtrack(cell, d):
            visited.add(cell)
            robot.clean()
            
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + dirs[new_d][0], cell[1] + dirs[new_d][1])
                
                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                
                robot.turnRight()
        
        # 0: up, 1: right, 2: down, 3: left
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()
        backtrack((0,0),0)

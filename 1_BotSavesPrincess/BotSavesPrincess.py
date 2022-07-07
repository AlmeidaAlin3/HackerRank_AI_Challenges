#!/usr/bin/python

def get_position(who): #who is "p" or "m"        
    for row in range(len(grid)):
        col = grid[row].find(who)
        if col!=-1:
            return(row, col)
           
def displayPathtoPrincess(n, grid):      
    row_robot, col_robot = get_position("m")
    row_princess, col_princess = get_position("p")

    while(col_robot!=col_princess):
        if col_robot>col_princess:
            print("LEFT")
            col_robot-=1

        elif col_robot<col_princess:
            print("RIGHT")
            col_robot+=1
        
    while(row_robot!=row_princess):
        if row_robot<row_princess:
                print("DOWN")
                row_robot+=1

        elif row_robot>row_princess:
                print("UP")
                row_robot-=1

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)

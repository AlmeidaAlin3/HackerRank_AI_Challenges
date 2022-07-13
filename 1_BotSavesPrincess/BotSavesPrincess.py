#!/usr/bin/python

'''
### Bot saves princess ###

Princess Peach is trapped in one of the four corners of a square grid. 
You are in the center of the grid and can move one step at a time in any of the four directions. 
Can you rescue the princess?

Input format:
    The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.
    Grid is indexed using Matrix Convention

Output format:
    Print out the moves you will take to rescue the princess in one go. 
    The moves must be separated by '\n', a newline. 
    The valid moves are LEFT or RIGHT or UP or DOWN.

Sample input:
    3
    ---
    -m-
    p--

Sample output:
    DOWN
    LEFT

Task:
    Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the character array grid. 
    The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0]. 
    The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. 
    The goal is to reach the princess in as few moves as possible.
    The above sample input is just to help you understand the format. 
    The princess ('p') can be in any one of the four corners.
'''

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

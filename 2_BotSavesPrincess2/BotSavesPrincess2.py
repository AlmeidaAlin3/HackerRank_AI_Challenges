#!/bin/python3

'''
### Bot saves princess - 2 ###

In this version of "Bot saves princess", Princess Peach and bot's position are randomly set. 
Can you save the princess?

Task:
    Complete the function nextMove which takes in 4 parameters - an integer N, 
    integers r and c indicating the row & column position of the bot and the 
    character array grid - and outputs the next move the bot makes to rescue the princess.

Input Format:
    The first line of the input is N (<100), the size of the board (NxN). 
    The second line of the input contains two space separated integers, 
    which is the position of the bot.
    Grid is indexed using Matrix Convention
    The position of the princess is indicated by the character 'p' 
    and the position of the bot is indicated by the character 'm' 
    and each cell is denoted by '-' (ascii value: 45).

Output Format:
    Output only the next move you take to rescue the princess. 
    Valid moves are LEFT, RIGHT, UP or DOWN

Sample Input:
    5
    2 3
    -----
    -----
    p--m-
    -----
    -----

Sample Output:  
    LEFT

Resultant State:
    -----
    -----
    p-m--
    -----
    -----

Explanation:
    As you can see, bot is one step closer to the princess. 
'''

def get_position(who): #who is "p" or "m"        
    for row in range(len(grid)):
        col = grid[row].find(who)
        if col!=-1:
            return(row, col)
        
def print_world(grid):
    for i in len(grid):
        print(grid[i])
    print("")

def nextMove(n, r, c, grid):
    row_robot, col_robot = get_position("m")
    row_princess, col_princess = get_position("p")

    while(col_robot!=col_princess):
        if col_robot>col_princess:
            print("LEFT")
            col_robot-=1

        elif col_robot<col_princess:
            print("RIGHT")
            col_robot+=1
        print_world(grid)
    
    while(row_robot!=row_princess):
        if row_robot<row_princess:
                print("DOWN")
                row_robot+=1

        elif row_robot>row_princess:
                print("UP")
                row_robot-=1 
        print_world(grid)
    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))

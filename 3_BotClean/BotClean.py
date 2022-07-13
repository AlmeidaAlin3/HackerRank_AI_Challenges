#!/usr/bin/python

'''
### BotClean ###
The goal of Artificial Intelligence is to create a rational agent (Artificial Intelligence 1.1.4). 
An agent gets input from the environment through sensors and acts on the environment with actuators. 
In this challenge, you will program a simple bot to perform the correct actions based on environmental input.

Meet the bot MarkZoid. It's a cleaning bot whose sensor is a head mounted camera and whose actuators 
are the wheels beneath it. It's used to clean the floor.

The bot here is positioned at the top left corner of a 5*5 grid. 
Your task is to move the bot to clean all the dirty cells.

Input Format:
       The first line contains two space separated integers which indicate the current 
       position of the bot. The board is indexed using Matrix Convention
       5 lines follow representing the grid. Each cell in the grid is represented 
       by any of the following 3 characters: 
       'b' (ascii value 98) indicates the bot's current position, 
       'd' (ascii value 100) indicates a dirty cell 
       and '-' (ascii value 45) indicates a clean cell in the grid.
       Note If the bot is on a dirty cell, the cell will still have 'd' on it.

Output Format:
       The output is the action that is taken by the bot in the current step, 
       and it can be either one of the movements in 4 directions or cleaning up the cell in which 
       it is currently located. The valid output strings are LEFT, RIGHT, UP and DOWN or CLEAN. 
       If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. 
       Repeat this process until all the cells on the grid are cleaned.

Sample Input #00:
       0 0
       b---d
       -d--d
       --dd-
       --d--
       ----d

Sample Output #00:
       RIGHT

Resultant state:
       -b--d
       -d--d
       --dd-
       --d--
       ----d

Sample Input #01:
       0 1
       -b--d
       -d--d
       --dd-
       --d--
       ----d

Sample Output #01:
       DOWN

Resultant state:
       ----d
       -d--d
       --dd-
       --d--
       ----d

Task:
       Complete the function next_move that takes in 3 parameters posr, posc being the 
       co-ordinates of the bot's current position and board which indicates the board 
       state to print the bot's next move.
       The codechecker will keep calling the function next_move till the game is over 
       or you make an invalid move.
'''

def get_closest_garbage(board, posr, posc):
    garbages = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]=="d":
                garbages.append([row, col])
    
    closest = garbages[0]
    for g in garbages:
        new_dist = abs(g[0]-posr) + abs(g[1]-posc)
        old_dist = abs(closest[0]-posr) + abs(closest[1]-posc)
        if new_dist<old_dist:
            closest = g       
    return closest


def clean(row_garbage, col_garbage, row_robot, col_robot):
    if col_robot != col_garbage:
        if col_robot > col_garbage:  
            action = "LEFT"
            return(action)        
        
        elif col_robot < col_garbage:
            action="RIGHT"
            return(action)
   
    if row_robot != row_garbage:
        if row_robot < row_garbage:  
            action="DOWN"
            return(action)
        
        elif row_robot > row_garbage:
            action="UP"
            return(action)
    
    if (row_robot==row_garbage) and (col_robot==col_garbage):
        action = "CLEAN"
        return(action)


def next_move(posr, posc, board): 
    garbage = get_closest_garbage(board, posr, posc)
    action = clean(garbage[0], garbage[1], posr, posc)
    print(action)
    
    
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

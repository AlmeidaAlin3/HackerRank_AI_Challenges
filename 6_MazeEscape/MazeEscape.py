#!/usr/bin/python3

'''
### MAZE ESCAPE ###
Maze Escape is a popular 1 player game where a bot is trapped in a maze and is expected to 
find its way out. 
In this version of the game, 2 bots whose positions are not visible to each other are placed 
at random points in the maze. the first bot to find its way out of the maze wins the game.

The visibility of the bot is restricted to its 8 adjacent cells as shown in the figure below
    ---
    -b-
    ---
where b is the bot. Bots can be facing any of the 4 directions. To make this game more interesting, 
the orientation of both the bots are randomly chosen at the start of the game and the map visible 
to them also changes according to the orientation.

If the actual map is as shown below,
    #######
    #--#-b#
    #--#--#
    #--#--#
    e-----#
    #-----#
    #######

and your bot is positioned at (1,5) and is facing the RIGHT side of the maze, the input will be
    ###
    #b-
    #--

If your bot is facing UP, your input will be
    ###
    -b#
    --#

If your bot is facing LEFT, your input will be
    --#
    -b#
    ###

And if your bot is facing DOWN, your input will be
    #--
    #b-
    ###

It is to be noted that your bot faces the direction in which it chooses to make its next move.

Input Format:
    The walls are represented by character # ( ascii value 35), empty cells are represented 
    by - (ascii value 45), the maze door which is the indication of the way out is represented 
    by e (ascii value 101)
    The input contains 4 lines, the first line being the player id (1 or 2) and followed 
    by 3 lines, each line containing 3 of the above mentioned characters which represents 
    the 8 adjacent cells of the bot. The visible maze given as input always has the bot at the center.

    Constraints:
        5 <= r,c <= 30 where r, c is the number of rows and columns of the maze.

Output Format:
    Output UP, DOWN, LEFT or RIGHT which is the next move of the bot.

Sample Input:
    1
    ###
    #--
    #--

Sample Output:
    RIGHT

Explanation:
    Considering the maze given above. If the input is as given below with the bot initially facing the RIGHT side of the maze, if the bot chooses to go RIGHT, the new position of the bot in the maze would be

    #######
    #--#--#
    #--#-b#
    #--#--#
    e-----#
    #-----#
    #######

    The bot moves 1 step DOWN w.r.t the maze. As the bot is facing DOWN side of the maze, his next input would be
        #--
        #--
        #--
    with the bot at the center. 
'''


import random
import os


# --- 
# Flips the input horizontally
def flip_h(board):
    board_flipped_h = []
    for r in range(0, len(board), 1):
        b_row=[]
        for c in range(len(board[0])-1, -1, -1):
            b_row.append(board[r][c])
        board_flipped_h.append(b_row)
    return board_flipped_h


# --- 
# Flips the input vertically
def flip_v(board):
    board_flipped_v = []
    for r in range(len(board)-1, -1, -1):
        b_row=[]
        for c in range(0, len(board[0]), 1):
            b_row.append(board[r][c])
        board_flipped_v.append(b_row)
    return board_flipped_v  


# --- 
# Flips the input vetrically AND horizontally
def flip_vh(board):
    board_flipped_v = flip_v(board)
    board_flipped_hv = flip_h(board_flipped_v)
    return board_flipped_hv  


# --- 
# Changes the input from the bot's perspective to the standard board's orientation
def get_board_std(board, last_action):
    if last_action=="RIGHT": 
        board_std = flip_h(board)        
    elif last_action == "LEFT": 
        board_std = flip_v(board) 
    elif last_action=="DOWN": 
        board_std = flip_vh(board)
    else: #UP don't change view orientation
        board_std = board  
    return board_std
 
    
# --- 
# Saves last action to a txt file
def save_action(action):
    if not(os.path.isfile(r"file-maze/last_action.txt")):
        os.makedirs(os.path.dirname(r"file-maze/last_action.txt"), exist_ok=True)  
        with open(r"file-maze/last_action.txt", mode='w') as f:
            f.write(action)
            f.close()
            return
    else:
        with open(r"file-maze/last_action.txt", mode='w') as f:
            f.write(action)
            f.close()
            return

        
# --- 
# Get last action from the txt file
def get_last_action():
    if not(os.path.isfile(r"file-maze/last_action.txt")):
        return("UP")
    else:
        with open(r"file-maze/last_action.txt", mode='r') as f:
            last_action = f.read().split('\n')
            return(last_action)

    
# ---
# Chooses best action according to input
# If theres an escape, move to there; else, follow the wall clockwise.
def get_action(board_std):
    row_robot = 1
    col_robot = 1
    rows_wall = []
    cols_wall = []
    escape = False
    
    for r in range(len(board_std)):
        for c in range(len(board_std[r])):
            if board[r][c]=="e":
                row_escape = r
                col_escape = c
                escape = True
            if board[r][c]=="#":
                rows_wall.append(r)
                cols_wall.append(c)
    
    if escape:        
        if col_robot > col_escape:  
            action = "LEFT"
            return(action)        
        elif col_robot < col_escape:
            action="RIGHT"
            return(action)
        if row_robot < row_escape:  
            action="DOWN"
            return(action)
        elif row_robot > row_escape:
            action="UP"
            return(action)
        
    else: # follow the wall clockwise
        if board_std[0][0] == "#" and board_std[0][1] == "-":
            action = "UP"
            '''   #-/
                  /b/
                  ///   '''
    
        if board_std[0][1] == "#" and board_std[1][2] == "-":
            action = "RIGHT"
            '''   /#/
                  /b-
                  ///   '''
        
        if board_std[0][2] == "#" and board_std[1][2] == "-":
            action = "RIGHT"
            '''   //#
                  /b-
                  ///   '''
            
        if board_std[1][2] == "#" and board_std[2][1] == "-":
            action = "DOWN"
            '''   ///
                  /b#
                  /-/   '''
            
        if board_std[2][2] == "#" and board_std[2][1] == "-":
            action = "DOWN"
            '''   ///
                  /b/
                  /-#   '''
              
        if board_std[2][1] == "#" and board_std[1][0] == "-":
            action = "LEFT"
            '''   ///
                  -b/
                  /#/   '''
            
        if board_std[2][0] == "#" and board_std[1][0] == "-":
            action = "LEFT"
            '''   ///
                  -b/
                  #//   '''
            
        if board_std[1][0] == "#" and board_std[0][1] == "-":
            action = "UP"
            '''   /-/
                  #b/
                  ///   '''

        return(action)
    
    
# --- 
# Set next action 
def next_move(player, board):
    last_action = get_last_action()
    board_std = get_board_std(board, last_action)
    action = get_action(board_std)
    save_action(action)
    print(action)
    

# --- 
# Start application
if __name__ == "__main__":
    # Set data
    player = int(input())
    board = [[j for j in input().strip()] for i in range(3)]  
    next_move(player, board)

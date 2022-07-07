#!/usr/bin/python

# Head ends here

       
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

#!/usr/bin/python3
import os
import random
import re

#---
# converts a numeric position [x,y] to a string "x y \n"
# if empty [] returns ""
def num_to_str(pos_num):
    pos_str=""
    if len(pos_num)>0:
        pos_str = str(pos_num[0])+" "+str(pos_num[1])+"\n"
    return(pos_str)

    
#---
# converts a string position "x y \n" to numeric position [x,y]
# if empty "" returns []
def str_to_num(pos):
    if len(pos)>0:
        pos_str = re.split("[^0-9]", pos) #splits by " " and "\n"
        if pos_str[0]!="": #if not empty
            pos_num = [int(pos_str[0]), int(pos_str[1])]                    
            return(pos_num)
        else:
            return([]) #if empty ""
    else:
        return([]) #if empty ""
    
    
#---
# saves the position of new discovered garbages to a txt file 
# so, even if not visible anymore, we can remember to clean them
def memorize_new_garbages(board):
    current_garbages_num = get_garbages_positions(board)
    if len(current_garbages_num)>0:

        if not(os.path.isfile(r"file-bot/saw_garbages.txt")):
            os.makedirs(os.path.dirname(r"file-bot/saw_garbages.txt"), exist_ok=True)  
            with open(r"file-bot/saw_garbages.txt", mode='w') as f:
                f.write("\n")
                f.close()

        with open(r"file-bot/saw_garbages.txt", mode='r+') as f:
            memorized_garbages_str = f.read().split('\n') 
            for g_num in current_garbages_num:
                g_str = num_to_str(g_num)
                if g_str not in memorized_garbages_str:
                    f.write(g_str)
            f.close()
            
#            with open(r"file-bot/saw_garbages.txt", mode='r') as f:
#                memorized_garbages_str = f.read().split('\n')
#                print("--- final_memorized_garbages_str", memorized_garbages_str)

        
#---   
# get the current visible garbages:
def get_garbages_positions(board):
    garbages_num = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]=="d":
                garbages_num.append([row, col])
    return(garbages_num)
  

#---
# reads the txt file to remember what are the garbages once found that were not cleaned yet
def get_all_left_garbages():     
    with open(r"file-bot/saw_garbages.txt", mode='r') as f:
        memorized_garbages_str = f.read().split('\n')   
        
        if len(memorized_garbages_str)>0:  
            memorized_garbages_num = []
            for g_str in memorized_garbages_str: 
                if len(g_str)>0: 
                    g_num = str_to_num(g_str)
                    if g_num not in memorized_garbages_num:
                        memorized_garbages_num.append(g_num)
            f.close()
            
            if len(memorized_garbages_num)>0: 
                return(memorized_garbages_num, True)

            else: # no valid garbages position remaining in the txt file (i.e. there are only ""s)
                return([], False)

        else: # no garbages remaining in the txt file
            f.close()
            return([], False)    


#---
# returns the robot closest gargabe from all of those once saw and not cleaned yet
def get_closest_garbage(garbages_num, posx, posy):
    if len(garbages_num)>0:
        closest = garbages_num[0]
        for g_num in garbages_num:
            if len(g_num)>1:
                new_dist = abs(g_num[0]-posx) + abs(g_num[1]-posy)
                old_dist = abs(closest[0]-posx) + abs(closest[1]-posy)
                if new_dist<old_dist:
                    closest = g_num 
        return closest
    else:
        return []


#---
# clean the garbage and updates the txt file that stores the garbages yet to be clean
def move_to_clean(row_garbage, col_garbage, row_robot, col_robot):
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
        update_cleaned_garbage([row_garbage, col_garbage])
        return(action)  

    
#---   
# removes cleaned garbage from the txt file that stores remaining garbages
def update_cleaned_garbage(cleaned_num): 

###    
#    with open(r"file-bot/saw_garbages.txt", mode='r') as f:
#        memory = f.read().split('\n')
#        print("-memory", memory)
#        f.close()
###

    with open(r"file-bot/saw_garbages.txt", mode='r') as f:     
        memorized_garbages_str = f.read().split('\n')
        f.close()
    
    #os.makedirs(os.path.dirname(r"file-bot/saw_garbages.txt"), exist_ok=False)  
    with open(r"file-bot/saw_garbages.txt", mode='w') as f:
        cleaned_str = num_to_str(cleaned_num)[:-1] #removes the "\n" at the end        
        for g_str in memorized_garbages_str:
            if len(g_str)>1: #removes empty entries in the txt file
                if g_str != cleaned_str:
                    f.write(g_str+"\n")    
        f.close()
    
###
#    with open(r"file-bot/saw_garbages.txt", mode='r') as f:
#        memory = f.read().split('\n')
#        print("--memory", memory)
#        f.close()
###

#---
def next_move(posx, posy, board):
    memorize_new_garbages(board)
    garbages, is_dirty = get_all_left_garbages()
    
    if (is_dirty):
        closest_garbage = get_closest_garbage(garbages, posx, posy)
        action = move_to_clean(closest_garbage[0], closest_garbage[1], posx, posy)
    else:
        if posx<len(board[0])/2:
            if posy<=len(board)/2:
                action=random.choice(["RIGHT", "DOWN"])
            
            elif posy>len(board)/2:
                action=random.choice(["RIGHT", "UP"])
        
        elif posx>=len(board[0])/2:
            if posy<=len(board)/2:
                action=random.choice(["LEFT", "DOWN"])
            
            elif posy>len(board)/2:
                action=random.choice(["LEFT", "UP"])

                
    print(action)
    
    
#---
if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)  


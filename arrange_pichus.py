#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : Neelan Scheumann - nscheuma
#
# Based on skeleton code in CSCI B551, Fall 2020
#


import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Count total # of pichus on board
def count_pichus(board):
    return sum([ row.count('p') for row in board ] )

# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a pichu to the board at the given position, and return a new board (doesn't change original)
def add_pichu(board, row, col):
    return board[0:row] + [board[row][0:col] + ['p',] + board[row][col+1:]] + board[row+1:]

#check if you can see a pichu from a given spot
def valid_spot(board, row, col):
    #check left
    c = col
    while c >= 0:
        if board[row][c]=='.':
            c += -1
        elif board[row][c]=='X' or board[row][c]=='@':
            c = -1
        else:
            return False
    #check right
    c = col
    while c < len(board[row]):
        if board[row][c]=='.': 
            c += 1
        elif board[row][c]=='X' or board[row][c]=='@':
            c = len(board[row])
        else:
            return False
    #check up
    r = row
    while r >= 0:
        if board[r][col]=='.': 
            r += -1
        elif board[r][col]=='X' or board[r][col]=='@':
            r = -1
        else:
            return False
    #check down
    r = row
    while r < len(board):
        if board[r][col]=='.': 
            r += 1
        elif board[r][col]=='X' or board[r][col]=='@':
            r = len(board)
        else:
            return False
    return True

# Get list of successors of given board state
def successors(board):
    return [add_pichu(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if (board[r][c] == '.')
                                                                                                 and(valid_spot(board, r, c))]

# check if board is a goal state
def is_goal(board):
    return count_pichus(board) == K 

# run the standard search algorithm (i.e. the one that does allow for diagonal Pichus)
def standard_search(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors(fringe.pop()):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return None

# The next 4 functions are all to handle the extra credit portion of the assignment. They are all similar to functions above but were modified to 
# handle the unique case posed for extra credit.

# return the list of successors - the only difference from above is that this calls super_valid_spot instead of valid spot
def super_successors(board):
    return [add_pichu(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if (board[r][c] == '.')
                                                                                                 and(super_valid_spot(board, r, c))]

#check if you can see a pichu from a given spot - adds in the four diagonal directions as well to handle the extra credit case
def super_valid_spot(board, row, col):
    max_c = len(board[row])
    max_r = len(board)
    #check left
    c = col
    while c >= 0:
        if board[row][c]=='.':
            c += -1
        elif board[row][c]=='X' or board[row][c]=='@':
            c = -1
        else:
            return False
    #check right
    c = col
    while c < max_c:
        if board[row][c]=='.': 
            c += 1
        elif board[row][c]=='X' or board[row][c]=='@':
            c = len(board[row])
        else:
            return False
    #check up
    r = row
    while r >= 0:
        if board[r][col]=='.': 
            r += -1
        elif board[r][col]=='X' or board[r][col]=='@':
            r = -1
        else:
            return False
    #check down
    r = row
    while r < max_r:
        if board[r][col]=='.': 
            r += 1
        elif board[r][col]=='X' or board[r][col]=='@':
            r = len(board)
        else:
            return False
    #check up and to the left
    c = col
    r = row
    while c >= 0 and r >= 0:
        if board[r][c]=='.':
            c += -1
            r += -1
        elif board[r][c]=='X' or board[r][c]=='@':
            c = -1
        else:
            return False
    #check up and to the right
    c = col
    r = row
    while c < max_c and r >= 0:
        if board[r][c]=='.':
            c += 1
            r += -1
        elif board[r][c]=='X' or board[r][c]=='@':
            r = -1
        else:
            return False
    #check down and to the left
    c = col
    r = row
    while c >= 0 and r < max_r:
        if board[r][c]=='.':
            c += -1
            r += 1
        elif board[r][c]=='X' or board[r][c]=='@':
            c = -1
        else:
            return False
    #check down and to the right
    c = col
    r = row
    while c < max_c and r < max_r:
        if board[r][c]=='.':
            c += 1
            r += 1
        elif board[r][c]=='X' or board[r][c]=='@':
            r = len(board)
        else:
            return False
    return True

# checks to see if the goal state has been met
def is_super_goal(board, i):
    return count_pichus(board) == i

# runs the search algorithm, but instead of calling successors, it calls super_successors
def super_search(initial_board, i):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in super_successors(fringe.pop()):
            if is_super_goal(s, i):
                return(s)
            fringe.append(s)
    return None


# Solve! 
def solve(initial_board):
    i = K
    # if i/K is greater than 0, run the standard search algorithm
    if i > 0:
        return standard_search(initial_board)
    # if i/K is equal to 0, run the super_search algorithm instead until it can't find a solution, then return the last iteration that had a successful solution
    elif i == 0:
        i = 2
        while super_search(initial_board, i):
            i += 1
        i -= 1
        return super_search(initial_board, i)
    # if K is negative, then return a phrase indicating the error
    else:
        return "K must be greater than or equal to 0"

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])

    # This is K, the number of agents
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")



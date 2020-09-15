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

# Solve!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors( fringe.pop() ):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return None

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])

    # This is K, the number of agents
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")



#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
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

# Get list of successors of given board state
def successors(board):
    return [ add_pichu(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.' ]

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
    return False

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])

    # This is K, the number of agents
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")



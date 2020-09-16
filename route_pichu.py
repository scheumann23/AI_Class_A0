#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : Neelan Scheumann - nscheuma
#
# Based on skeleton code provided in CSCI B551, Fall 2020.


import sys
import json

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col, visits):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

	# Return only moves that are within the board and legal (i.e. go through open space ".") and have not been visited before
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) 
                                        and (map[move[0]][move[1]] in ".@" ) 
                                        and (move not in visits)]

# Calculate the euclidian distance between two coordinates to use as a heuristic later on
def euclid_dist(current_state, target_state):
    return ((current_state[0] - target_state[0])**2 + (current_state[1] - target_state[1])**2)**0.5

# Create a function to pop the highest priority in the queue
def priority_pop(fringe):
    min = fringe[0][3]
    index = 0 
    for i in range(len(fringe)):
        if fringe[i][3] < min:
            min = fringe[i][3]
            index = i
    return fringe.pop(index)

# Determine the direction traveled when given two positions 
def get_direction(last_move, curr_move):
    if last_move[0] - curr_move[0] == 1:
        return "N"
    elif last_move[0] - curr_move[0] == -1:
        return "S"
    elif last_move[1] - curr_move[1] == 1:
        return "W"
    elif last_move[1] - curr_move[1] == -1:
        return "E"

# Perform search on the map
def search1(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        # Find target position (need it to compute heuristic)
        target_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="@"][0]
        # Find measure of herutstic to target
        heuristic = euclid_dist(pichu_loc, target_loc)
        
        fringe=[(pichu_loc,0,'',heuristic)]
        #initialize the list of visited places with []
        visited = []

        while fringe:
            (curr_move, curr_dist, curr_dir, curr_cost)=priority_pop(fringe)
            for move in moves(house_map, *curr_move, visited):
                if house_map[move[0]][move[1]]=="@":
                    return curr_dist+1, curr_dir + get_direction(curr_move, move)
                else:
                    # if the move doesn't get you to the goal state, add the move coordinates, the new distance, the path traveled so far, and the total cost to the fringe
                    fringe.append((move, curr_dist + 1, curr_dir + get_direction(curr_move, move), euclid_dist(move, target_loc)+curr_dist + 1))
                # after the move is added to the fringe, add it to the list of visited places so that we don't return and backtrack
                visited.append(move)
        # if the fringe every empties out it must mean that there is no solution so return 'Inf'
        return "Inf"

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search1(house_map)
        if solution == 'Inf':
            print("Here's the solution I found:")
            print(solution)
        else:
            print("Here's the solution I found:")
            print(solution[0], end=" ")
            print(solution[1])


# a0

### Notes
1. I added a print statement after it checked each move to show me where it was getting caught in a loop and its between (2,2) and (2,3). I think this is because it is implementing DFS and the stack gets caught in a loop. 
2. Another issue is that the moves function allows pichu to move backwards.
    - The first thing I did was add a list of places that had been visited already so I could eliminate any move that would return me to a location that I have already explored

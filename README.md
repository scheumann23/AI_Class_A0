# a0

### Part 1: Route Pichu

##### Issues with starter code
The starter code provided by the instructors was very helpful as a place to start, but I quickly realized that it wasn't perfect. The search algorithm would constantly get caught in a loop and continue running without end. To help me debug where the issue was, I added several print statements (even though I am sure there are better ways to debug code!) in order to see what the fringe looked like as the algorithm progressed. I noticed that it kept getting caught in a loop whenever it encountered a "dead end," that is, a cell that has no choice but to backtrack and return to the cell it just came from. This helped me uncover the main issue with the starter code. Since there was no record of where the search had already been, whenever it got to a point where it would be forced to backtrack and return to a cell it just came from, it would simply return to the dead end once again and thus the never ending cycle would start. 

##### My solution
To help prevent the never ending loops, the first thing I did was add a list of places that been visited already so that I could quickly eliminate any cell that had already been explored when the move() function was called. After that change, if the algorithm began to search down a dead end, as soon as it hit the end it would no longer see moving backwards as a valid move and would be force to serach elsewhere in the fringe. Once I had that issue fixed, I began trying to improve the efficiency of the search. The starter code had implemented depth first search, but I instead chose to implement A* search because it can improve the time complexity of the search. For the heuristic function I decided to choose the Euclidian distance from the next cell being explored to the target. I wrote a simple helper function that computed the distance between to sets of coordinates and then also created a simple formula that would scan the map to find the location of the target. 

The other main component of the A* implementation is the idea of the priority queue for storing the fringe. First, to the fringe I added several additional elements to each potential move on the board, the total distance travelled so far, as well as the sum of the distance travelled and the heuristic function. Then I created a helper funtion that would search through the list of elements in the fringe and calculate the index of the "move" with the lowest combined distance and pop this element. 

With the heuristic function and the priority queue all set, the final step was to keep track of the directions that had been travelled up to that point. In order to accomplish this I wrote one more helper function that would take two sets of coordinates and return the direction travelled from the first set to the second. I also added an empty list to each element in the fringe so that I could keep track of all the states that had been searched through so far.

With the pieces all in place, I put everything together into the new and improved search1() function. As soon as the goal state is reached, the total distance as well as the list of directions gets returned. The final step was to take care of the case when there was no solution. To accomplish this, I added a line to the code that says if the length of the fringe is ever 0 when it gets checked, which means the entire search space has been explored and there is no solution, return 'Inf'

##### Assumptions
Some of the assumptions I am making in this solution is that a bird can only fly vertically or horizontally, and not diagonally. Second, I am assuming the shape of the map is rectangular in shape. This assumptions comes into play with the successor function checks for valid moves. If the map was somehow curved, my solution would most likely produce incorrect results, or at least be slower than it could be. 

### Part 2: Arrange Pichu

##### coming soon...


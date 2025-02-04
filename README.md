[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/nUqUKvy6)
# Assignment 4
Instructions [here](https://docs.google.com/document/d/1Og72uENh-BqaacZ4XRTXjIE4-AM_DUqYaQbsQva-ut8/edit?usp=sharing)


-Dead cells with 3 live neighbores become alive on next turn
-Live cells need 2 or 3 live neighbores to survive at the end of the turn
-Live cells will die at the end of the turn if they have more than 3 or less than 2 live neighbores
-Program goal: Read inputs from file_in, apply the cell life and death rules over 100 turns, write the output to file_out

Requirements:
-Program must be able to handle grids of any size
-Must use 2D lists to represent the grid
-Inner list items should 0s to represent dead cells, and 1s to represent live cells
-Main function must contain:
    -Accept input and output file names
    -Return a boolian value showing whether or not to visualize the simulation through view_grid function
    -Read the starting grid from the file
    -Run the cellular automaton through 100 steps
    -Save the final grid to the output file in the data/output folder.
    -Output file should be formatted the same way as input files
    -Use relative paths for file names
-Do not modify the header of the main function
-Write functions for each sub task

# NOTES
- wait lol I think I just figured out that my neighbour_sum function is adding to itself for row0? 
- this is not what's happening for the other rows though, but they're still off.
1:04pm 10 Dec 2024. CURRENT NEIGHBOUR_SUM ROW OUTPUTS FOR INPUT FILE A.TXT:
row0
actually i am going to write this to a new interim file

2:06pm 10 Dec 2024. 
Eric's advice for end of row/col calculations: 
- To check if a cell is off the bottom edge of the grid, you'd have to do something like this:
    - row_index >= len(grid)
- and to check if it's off the right edge of the grid:
    - col_index >= len(grid[row_index])

- tracing my algorithm and realizing that the neighbor sum function currently only accounts for the corners and center, and is not having a way to account for the edges of all rows.

# What I think rows 0 to 4 should look like from the neighbors some calculations based on my manual tracing:
## rows 0-4 SHOULD look like:
[1, 3, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 5, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[2, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
## rows 0-4 after Test 2:
[1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[2, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
## rows 0-4 after test 3.4:
[1, 2, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[2, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



# NEIGHBOURS_SUM PSEUDOCODE PLANNING
## OPTION 1
Top left, top right, all top
leftmost, rightmost
bottom left, bottom right, all bottom
else

## OPTION 2
- iterate over all leftmost cells first, then all rightmost cells, then anything else
if row_index[0]:
    if column_index[0]:
    elif column_index[last_row_index]:
    else: # all other leftmost values
wait no doing it like this isn't checking precisely the order I'm thinking, this would check all top first. 

if column_index[0]: # any leftmost cell

- Check top left
    - grid[0][0]
- Then check bottom left
    - grid[row_index = len(grid)][0]
    - may not be the right way to calculate final row index in program, may need to do as conditional? 
- Then check all left (will catch all other leftmost cells that are not caught by top or bottom left corners)
    - grid[row_index][0]
    
- Then check top right
    - grid[0][column_index = len(grid)]
- Then check all top (top left and top right have been checked previously)
    - grid[0][column_index]
    - grid[first_row][any_column]

- Then check bottom right
    - grid[row_index = len(grid)][column_index = len(grid)]
    - grid[last_row][last_column]

- Then check all bottom (bottom left and bottom right have been checked previously)
    - grid[row_index = len(grid)][column_index]
    - grid[last_row_index][any_column_index]

- Then check all else.
    - run test to see if current final else statement works as-is

## OPTION 3
- iterate through all top first - going by row_index as first coordinate

### all first_row items:
if row_index[0]: 
    if column_index[0]: 
        # specifies top left corner
        # grid[0][0]
    elif column_index[last_column_index]: 
        # specify top right corner
        # grid[0][last_column_index]
    else:
        # all other topmost values
        # grid[0][any_other_column_index]

### all last_row items:
elif row_index[last_row_index]: 
    if column_index[0]: 
        # specifies bottom left corner
        # grid[last_row_index][0]
    elif column_index[last_column_index]: 
        # specify bottom right corner
        # grid[last_row_index][last_column_index]
    else:
        # all other bottommost values
        # grid[last_row_index][any_other_column_index] 

### any other rows:   
else:
    if column_index[0]: 
        # specifies any leftmost cells
        # grid[any_other_row_index][0]
    elif column_index[last_column_index]: 
        # specify any rightmost cells
        # grid[any_other_row_index][last_column_index]
    else:
        # all other values
        # grid[any_other_row_index][any_other_column_index]


# TROUBLESHOOTING CELL_STATE()
- 9:45pm 12 Dec 2024: commented out portion of "if (grid[row_index][column_index] == 0): # and (neighbour_grid[row_index][column_index] < 3 or neighbour_grid[row_index][column_index] < 3):" to check if it was simply accurately checking for dead cells
    - is checking for dead cells; all currently dead cells are returning as dead 
    - revealed that cell survives is not functioning right; cell comes to life is not functioning right
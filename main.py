from matplotlib import pyplot as plt
# ---------------------------------------------------------------------------------------------------
# process input file
def remove_borders(input_grid: list) -> list:
    """
    Removes the ▒ borders and \n from an input grid list's rows; returns borderless_grid as a list.
    Parameters:
        input_grid: a 2D list with a border of "▒" characters and body contents of " " and "█"
    """
    borderless_grid = [] # because list can be changed from within functions, i want to make a list to work with without changing input_grid
    for row in input_grid:
        if row[1] == " " or row[1] == "█": # removing top and bottom ▒ border rows
            working_row = list(row)
            working_row = working_row[1:-2] # removing the left and right borders and newline characters
            borderless_grid.append(working_row)
    return borderless_grid
def convert_grid_characters_to_binary(special_characters_grid: list) -> list:
    """
    Converts the special characters from the input grid to binary characters to represent the grid  for use as a binary grid in cellular automaton calculations.
    Parameters:
        special_characters_grid: a 2D list with body contents of " " and "█"
    """
    binary_grid = []
    working_row = []
    for row in special_characters_grid:
        for character in row:
            if character == "█":
                character = 1
                working_row.append(character)
            else:
                character = 0
                working_row.append(character)
        binary_grid.append(working_row)
        working_row = [] # necessary to reset the value of the working row list so that it doesnot continue to add endlessly it to a single inner list with in binary grid

    return binary_grid
def process_input(input_grid: list) -> list:
    """
    Processes a special character-based grid for use as a binary grid in cellular automaton calculations.
    Parameters:
        input_grid: a 2D list with a border of "▒" characters and body contents of " " and "█"
    """
    borderless_grid = remove_borders(input_grid)
    binary_grid = convert_grid_characters_to_binary(borderless_grid)        
    return binary_grid
# ---------------------------------------------------------------------------------------------------
# process output file
def convert_grid_to_special_characters(binary_grid: list) -> list:
    """
    Converts the binary from the input grids to special characters to represent the grid for use in cellular automaton calculations.
    Parameters:
        binary_grid: a 2D list consisting of 1s and 0s as the inner list items
    """
    special_characters_grid = []
    working_row = []
    for row in binary_grid:
        for character in row:
            if character == 1:
                character = "█"
                working_row.append(character)
            else:
                character = " "
                working_row.append(character)
        special_characters_grid.append(working_row)
        working_row = [] # necessary to reset the value of the working row list so that it does not continue to add endlessly it to a single inner list with in binary grid

    return special_characters_grid
def add_top_and_bottom_borders(grid: list) -> list:
    """
    Adds top and bottom borders of "▒" special characters to a 2D list.
    Parameters:
        borderless_grid: a 2D list; intended to be one that does not have a border
    """
    bordered_grid = grid
    working_row = []
    for index in range(len(grid[0])):
        working_row.append("▒") # adding 1 special border character per index location in a grid row
    working_row = "".join(working_row) # turns working row from list in the string
    bordered_grid.insert(0, working_row)
    bordered_grid.append(working_row)
    return bordered_grid
def add_left_and_right_borders(borderless_grid: list) -> list:
    """
    Adds left and right "▒" borders and \n to the end of each row in a 2D list.
    Parameters:
        borderless_grid: a 2D list; intended to be one that does not have a border
    """
    bordered_grid = [] 
    working_row = []
    # adding left and right borders and new lines
    for row in borderless_grid: 
        row = ''.join(row) # turns row from list into string
        working_row.append("▒") # adds left border to working row
        working_row.append(row) # adds row string to working row
        working_row.append("▒\n") # adds right border and new line to working row
        working_row = "".join(working_row) # turns working row from list into string
        bordered_grid.append(working_row)
        working_row = [] # clear value of working row
    return bordered_grid
def add_borders(borderless_grid: list) -> list:
    """
    Adds top and bottom borders of "▒" special characters to a 2D list.
    Parameters:
        borderless_grid: a 2D list; intended to be one that does not have a border
    """
    bordered_grid = add_top_and_bottom_borders(borderless_grid)
    bordered_grid = add_left_and_right_borders(bordered_grid)
    return bordered_grid
def process_output(working_grid: list) -> list:
    """
    Processes the working binary grid to display for file output.
    Parameters:
        working_grid: a 2D list of 1s and 0s
    """
    special_characters_grid = convert_grid_to_special_characters(working_grid)        
    output_grid = add_borders(special_characters_grid)
    return output_grid
# ---------------------------------------------------------------------------------------------------
# cell life and death calculations
def live_neighbours_grid(output_filename: str, grid: list) -> None:
    """
    Accepts a binary grid of cellular automaton cell states, calls neighbour_check function to calculate number of live neighbours per cell, and writes data to an output file to create a grid of live neighbours per cell. Intended to help troubleshoot functionality of neighbour_check function. Accepts user input to record test number, test goal, and test functionality. 

    Parameters:
        output_filename: a valid file path. Enter a blank string if you do not wish to use the function.
        grid: a binary grid of cellular automaton cell state data. 
    """
    neighbour_row = []
    if output_filename != "":
        file_out = open(output_filename, "a")
        file_out.write("\n--------------------------------------\n")
        file_out.write("TEST NUMBER: ")
        file_out.write(input("TEST NUMBER: "))
        file_out.write("\nGOAL: ")
        file_out.write(input("GOAL: "))
        file_out.write("\n--------------------------------------\n")
        file_out.write("TEST: ")
        file_out.write(input("TEST: "))
        file_out.write("\n--------------------------------------\nRESULT: \n--------------------------------------\n")
        neighbour_sum = 0
        # -------------------------------------------------------------------------------------------
        # iterate over each cell in each row: 
        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])): 
            # ---------------------------------------------------------------------------------------
            # run neighbour_sum function for each cell in row:
                neighbour_sum = neighbour_check(grid, row_index, column_index)
                neighbour_row.append(neighbour_sum)
            neighbour_sum = 0
            # for each row in grid, convert row of neighbour_sums to an output_row that will be written to the neighbour sums output file. then, flush the contents of neighbour_row, neighbour_sum, and output_row.  
            output_row = "".join(str(neighbour_row))   
            file_out.write(output_row)
            file_out.write("\n")
            neighbour_row = []
            output_row = []
        file_out.close()
        
def neighbour_check(grid:list, row_index: int, column_index: int) -> int:
    """
    checks the number of live neighbours per cell in grid; returns value as integer
    """
    # set starting value of neighbour_sum variable
    neighbour_sum = 0
    # -------------------------------------------------------------------------------------------
    # check number of live neighbours for each cell in each row; write the value to the neighbour_sum variable:
    # CHECK LIVE NEIGHBOURS OF ALL TOP ROW CELLS
    if row_index == 0: # checks all cells in row0
        if column_index == 0: 
        # top left corner
        # checks: e,se,s -------------------------
            neighbour_sum = grid[row_index][column_index + 1] + grid[row_index + 1][column_index + 1] + grid[row_index + 1][column_index]

        elif column_index == (len(grid[row_index]) - 1): 
        # top right corner
        # checks: w,sw,s -------------------------
            neighbour_sum = grid[row_index][column_index - 1] + grid[row_index + 1][column_index - 1] + grid[row_index + 1][column_index] 

        else:
        # all other topmost cells
        # checks: w,e,se,s,sw -------------------------
            neighbour_sum = grid[row_index][column_index - 1] + grid[row_index][column_index + 1] + grid[row_index + 1][column_index + 1] + grid[row_index + 1][column_index] + grid[row_index + 1][column_index - 1]

    # CHECK LIVE NEIGHBOURS OF ALL MIDDLE ROW CELLS:
    elif ((len(grid) - 1) > row_index > 0): # checks all cells in row1 to the row before the final row index (ie., row(len(grid)-1))
        if column_index == 0: 
            # any leftmost cells
            # checks: n,ne,e,se,s -------------------------
            neighbour_sum = grid[row_index - 1][column_index] + grid[row_index - 1][column_index + 1] + grid[row_index][column_index + 1] + grid[row_index + 1][column_index + 1] + grid[row_index + 1][column_index]

        elif column_index == (len(grid[row_index]) - 1): 
            # any rightmost cells
            # checks: w,nw,n,s,sw -------------------------
            neighbour_sum = grid[row_index][column_index - 1] + grid[row_index - 1][column_index - 1] + grid[row_index - 1][column_index] + grid[row_index + 1][column_index] + grid[row_index + 1][column_index - 1]

        else:
            # all other middle row values
            # checks: w,nw,n,ne,e,se,s,sw -------------------------
            neighbour_sum = grid[row_index][column_index - 1] + grid[row_index - 1][column_index - 1] + grid[row_index - 1][column_index] + grid[row_index - 1][column_index + 1] + grid[row_index][column_index + 1] + grid[row_index + 1][column_index + 1] + grid[row_index + 1][column_index] + grid[row_index + 1][column_index - 1]

    # CHECK LIVE NEIGHBOURS OF ALL BOTTOM ROW CELLS:
    else: # checks all cells in row at final index position since this row is not accounted for by previous decision branches
        if column_index == 0: 
        # bottom left corner
        # checks: n,ne,e -------------------------
            neighbour_sum = grid[row_index - 1][column_index] + (grid[row_index - 1][column_index + 1] + grid[row_index][column_index + 1])

        elif column_index == (len(grid[row_index]) - 1):                
        # bottom right corner
        # w,nw,n -------------------------
            neighbour_sum = grid[row_index][column_index - 1] + (grid[row_index - 1][column_index - 1] + grid[row_index - 1][column_index])

        else: 
        # all other bottommost cells
        # checks: w,nw,n,ne,e -------------------------
            neighbour_sum = grid[row_index][column_index - 1] + (grid[row_index - 1][column_index - 1] + grid[row_index - 1][column_index]) + (grid[row_index - 1][column_index + 1] + grid[row_index][column_index + 1])

    return neighbour_sum

def cell_state_calc(grid: list) -> list:
    """
    Calls the neighbour_check function to count the live neighbours of a given cell, then evaluates the life/death state of the cell for the next time step. Outputs a 2D list to represent the cell grid at the next time step.
    Parameters:
        grid: a 2D list of 1s and 0s to represent live and dead cells respectively
    """
    working_row = []
    working_grid = []
    neighbour_sum = 0
    # -----------------------------------------------------------------------------------------------
    # iterate over each cell in each row: 
    for row_index in range(len(grid)):
        for column_index in range(len(grid[row_index])): # grid[row_index] means that you can select just the range of each row rather than selecting the whole thing each loop
        # -------------------------------------------------------------------------------------------
        # run neighbour_sum function for each cell in row:
            neighbour_sum = neighbour_check(grid, row_index, column_index)
    # -----------------------------------------------------------------------------------------------
    # check life/death state for each cell in each row of grid and compare to number of live neighbours to determine correct output state for next step; add next state of cell to working_row list:
        # -------------------------------------------------------------------------------------------
        # if cell is alive:
            if grid[row_index][column_index] == 1:
                # and cell has more than three or less than two live neighbors:
                if neighbour_sum > 3 or neighbour_sum < 2:
                    # cell is alive and dies
                    print("cell dies :(")
                    working_row.append(0)
                # and cell has two or three neighbors:
                else:
                    # cell is alive and survives
                    print("cell survives!")
                    working_row.append(1)
        # -------------------------------------------------------------------------------------------
        # if cell is dead:
            else: 
                # and cell has exactly three live neighbours:
                if neighbour_sum == 3:
                    # cell comes to life
                    print("cell comes to life!")
                    working_row.append(1)
                # and has less or more than three live neighbours:
                else:
                    # cell stays dead
                    working_row.append(0)
            
            # flush value of neighbour_sum after checking each cell in each row of grid
            neighbour_sum = 0 

        # add working_row (states of cells in grid at next time step) as inner list item of working_grid outer list to fill in next time step's cell grid
        working_grid.append(working_row)
        working_row = []
    return working_grid 

# ---------------------------------------------------------------------------------------------------
# grid visualization function
def view_grid(grid, frame_delay: float, step_number: int) -> None:
    """
    shows an image of the current state of the grid
    parameters:
        grid - list-of-lists representing the current grid. Inner lists use 0s to represent dead cells, and 1s to represent live ones
        frame_delay - the program will pause for this many seconds after displaying the image. 0.1s gives a pretty good animation effect
        step_number - the step number of the supplied grid (will be displayed above the image)
    """

    # check that the grid supplied is not empty
    if len(grid) == 0:
        raise Exception("grid is empty")

    # check that all rows contain the same number of cells
    row_lengths = set([len(row) for row in grid])
    if len(row_lengths) != 1:
        raise Exception(f"not all grid rows are the same length. Found lengths: {row_lengths}")

    # check that all rows contain only 0s and 1s
    if not all([set(row) <= {0, 1} for row in grid]):
        raise Exception("only 0 and 1 are allowed in grid")

    # plot the grid
    plt.cla()
    plt.imshow(grid)
    plt.title(f'step {step_number}')
    plt.pause(frame_delay)


def main(input_filename: str, output_filename: str, display: bool) -> None:
    """
    main function
    parameters:
        input_filename: file to read the starting configuration from
        output_filename: file to write the ending configuration (after 100 steps) to
        display: if True, the program should display the grid steps (using the provided view_grid function)
                 if False, the program should not display the grid steps.
    """
    # read the contents of file_in to a 2D list of 0s and 1s to represent the cell grid
    file_in = open(input_filename, "r", encoding='UTF-8')
    input_lines= file_in.readlines()
    file_in.close()
    input_grid = process_input(input_lines)

    # perform the live vs dead cells checking function on a per turn basis using a counter; pass the value of counter+1 into view_grid() to display steps in visualization
    working_grid = input_grid
    counter = 0
    while counter < 100:
        print(f"\nTurn {counter}\n")
        live_neighbours_grid("", working_grid) # pass in a valid file path to an output file if you would like to run neighbour_sum tests
        working_grid = cell_state_calc(working_grid)
        if display is True:
            view_grid(working_grid, 0.01, (counter + 1))
        counter += 1

    # convert working_grid back to special characters and write to output file
    output_grid = process_output(working_grid)
    file_out = open(output_filename, "w", encoding='UTF-8')
    for row in output_grid:
        output_line = "".join(str(row))
        file_out.write(output_line) 
    file_out.close()
        
main("./data/input/a.txt", "./data/output/output_a.txt", True)
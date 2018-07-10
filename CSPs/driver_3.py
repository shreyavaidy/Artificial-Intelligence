#!/usr/bin/env python
# coding:utf-8

"""
Usage:
$ python3 driver.py <81-digit-board>
$ python3 driver.py   => this assumes a 'sudokus_start.txt'

Saves output to output.txt
"""

import queue
import sys
import time

ROW = "ABCDEFGHI"
COL = "123456789"
TIME_LIMIT = 1.  # max seconds per board
out_filename = 'output.txt'
src_filename = 'sudokus_start.txt'


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def string_to_board(s):
    """
        Helper function to convert a string to board dictionary.
        Scans board L to R, Up to Down.
    """
    return {ROW[r] + COL[c]: int(s[9 * r + c])
            for r in range(9) for c in range(9)}


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def write_solved(board, f_name=out_filename, mode='w+'):
    """
        Solve board and write to desired file, overwriting by default.
        Specify mode='a+' to append; otherwise ='w+'.
    """

    # Calling the backtracking function
    result = backtracking(board)

    # Write board to file
    outfile = open(f_name, mode)
    outfile.write(result)
    outfile.write('\n')
    outfile.close()

    return result


# Algorithm to get updated values
def algo_hue(csp, values):

    h_queue = queue.Queue()
    visited = set()

    for s, d in csp.items():
        if (d != '0'):
            visited.add(s)
            values[s] = d

            for peer in neighbors[s]:
                tmp = values[peer]
                new_val = tmp.replace(d, "")

                if (len(new_val) == 1):
                    if peer not in visited:
                        h_queue.put(peer)
                values[peer] = new_val

    while not h_queue.empty():
        node_key = h_queue.get()
        visited.add(node_key)
        d = values[node_key]
        for peer in neighbors[node_key]:
            tmp = values[peer]
            new_val = tmp.replace(d, "")
            if (len(new_val) == 1):
                if peer not in visited:
                    h_queue.put(peer)
            values[peer] = new_val

    return values


#Generate a 3x3 sudoku grid with numbers 1 to 9
def number(a, b):
    num = []
    for i in a:
        for j in b:
            num.append(i + j)
    return num

#Check if the solution is a allowable solution before returning to the main function
def is_allowed(sol):
    flag = 1
    for s, d in sol.items():
        if len(d) == 0:
            flag = 0
            break
    return flag

#Check if the solution is correct
def is_solved(updated):
    solution = sudoku_dict
    to_assign = []
    for s, d in updated.items():
        if len(d) > 1:
            to_assign.append(s)
            solution[s] = '0'
        else:
            solution[s] = d

    return (solution, to_assign)


def backtrack(Sol_domain, isolved):
    start=time.time()
    while not isolved:
        pos_sol = dict(Sol_domain.get())
        new_sol, to_assign = is_solved(pos_sol)
        if (len(to_assign) == 0):
            isolved = 1
            break
        else:
            hue = []
            for i in to_assign:
                hue.append(len(pos_sol[i]))

            choose = hue.index(min(hue))
            current_key = to_assign[choose]
            values_pos = pos_sol[current_key]
            for val in values_pos:
                temp_sol = dict(pos_sol)
                temp_sol[current_key] = val
                temp_ac_3 = algo_hue(new_sol, temp_sol)
                if is_allowed(temp_ac_3):
                    Sol_domain.put(temp_ac_3)

    new_board = ''.join([new_sol[key] for key in keys])
    end = time.time()
    # print(" Running_time: {0:.8f}".format(end - start) + "\n")
    # print_board(string_to_board(new_board))
    write_solved(string_to_board(new_board), mode='a+')

    return

def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this

    solved_board = board
    #Convert it back to string
    #Execute the entire logic with keys
    #Convert it back and then return ?

    # time.sleep(5.)
    return board_to_string(solved_board)


#Main function -- program starts from here
if __name__ == '__main__':
    isolved = 0
    value_of_position = '123456789'
    r_key, c_key = [], []
    cell_keys = []
    cell_keys = [number(i, j) for i in ['ABC', 'DEF', 'GHI'] for j in ['123', '456', '789']]
    # print(cell_keys)
    keys = [i + j for i in ROW for j in COL]

    for i in ROW:
        r_key.append([i + j for j in COL])
    for j in COL:
        c_key.append([i + j for i in ROW])


    if len(sys.argv) > 1:  # Run a single board, as done during grading
        sudoku_in = sys.argv[1]
        init_values = sudoku_in

        #Dictionary with keys and input values
        sudoku_dict = dict(zip(keys, init_values))
        units = dict((s, [u for u in (r_key + c_key + cell_keys) if s in u]) for s in sudoku_dict)
        neighbors = dict((s, set(sum(units[s], [])) - set([s])) for s in sudoku_dict)
        # print(neighbors)

        #Dictionary with sudoku input dict and the value of the positions in order
        partial_sol = dict((s, value_of_position) for s in sudoku_dict)
        # print(partial_sol)

        # Calling the algo to minimize
        updated = algo_hue(sudoku_dict, partial_sol)

        # Create a last-in-first-out queue to add updated values
        solution_domain = queue.LifoQueue()
        solution_domain.put(updated)

        # Calling the backtracking function
        backtrack(solution_domain, isolved)

    else:
        print("Running all from sudokus_start")

        #  Read boards from source.
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        iter = 1
        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):
            init_values = line
            # print(iter)
            iter=iter+1

            # Dictionary with keys and input values
            sudoku_dict = dict(zip(keys, init_values))
            units = dict((s, [u for u in (r_key + c_key + cell_keys) if s in u]) for s in sudoku_dict)
            neighbors = dict((s, set(sum(units[s], [])) - set([s])) for s in sudoku_dict)

            # Dictionary with sudoku input dict and the value of the positions in order
            partial_sol = dict((s, value_of_position) for s in sudoku_dict)

            # Calling the algo to minimize
            updated = algo_hue(sudoku_dict, partial_sol)
            solution_domain = queue.LifoQueue()
            solution_domain.put(updated)

            # Calling the backtracking function
            backtrack(solution_domain, isolved)

        print("Finished all boards in file.")
"""
Artificial Intelligence - HW 1
"""
import time

from heapq import heappush
from heapq import heappop
import sys

#To redirect all print to an external file
outputfile = open('output.txt', 'w')
sys.stdout = outputfile


def expand(state):
    """
    Returns a list of expanded states as (Action, state) tuples.
    """

    m = len(state)
    n = len(state[0])
    row = 0
    col = 0

    #Find position of 0 on the current board config
    z_pos = 0

    for i in range(m):
        for j in range(n):
            #print state[i][j]
            if state[i][j] == 0:
                z_pos = 1
                row = i
                col = j
                break
        if z_pos == 1:
            break

    #Expand the board by swapping '0' on the board with possible neighbors
    cur_state = state
    expanded_nodes = []
    path = []

    if (row - 1 > -1):
        #Move Up
        path.append("Up")
        path.append(swap_cells(cur_state, row, col, row - 1, col))
        expanded_nodes.append(tuple(path))
        path = []
    if (row + 1 < n):
        #Move Down
        path.append("Down")
        # Swap with element below
        path.append(swap_cells(cur_state, row, col, row + 1, col))
        expanded_nodes.append(tuple(path))
        path = []
    if (col - 1 > -1):
        #Move Left
        path.append("Left")
        path.append(swap_cells(cur_state, row, col, row, col - 1))
        expanded_nodes.append(tuple(path))
        path = []
    if (col + 1 < n):
        # Move Right
        path.append("Right")
        path.append(swap_cells(cur_state, row, col, row, col + 1))
        expanded_nodes.append(tuple(path))

    return expanded_nodes


def rev_expand(state):
    """
    For DFS
    Returns a list of expanded states as (Action, state) tuples.
    """

    m = len(state)
    n = len(state[0])
    row = 0
    col = 0

    #Find position of 0 on the current board config
    z_pos = 0

    for i in range(m):
        for j in range(n):
            #print state[i][j]
            if state[i][j] == 0:
                z_pos = 1
                row = i
                col = j
                break
        if z_pos == 1:
            break

    #Expand the board by swapping '0' on the board with possible neighbors
    cur_state = state
    expanded_nodes = []
    path = []

    if (col + 1 < n):
        # Move Right
        path.append("Right")
        path.append(swap_cells(cur_state, row, col, row, col + 1))
        expanded_nodes.append(tuple(path))
    if (col - 1 > -1):
        #Move Left
        path.append("Left")
        path.append(swap_cells(cur_state, row, col, row, col - 1))
        expanded_nodes.append(tuple(path))
        path = []
    if (row + 1 < n):
        # Move Down
        path.append("Down")
        # Swap with element below
        path.append(swap_cells(cur_state, row, col, row + 1, col))
        expanded_nodes.append(tuple(path))
        path = []
    if (row - 1 > -1):
        #Move Up
        path.append("Up")
        path.append(swap_cells(cur_state, row, col, row - 1, col))
        expanded_nodes.append(tuple(path))

    return expanded_nodes


def swap_cells(state, r1, c1, r2, c2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped.
    """
    # print state
    value1 = state[r1][c1]
    value2 = state[r2][c2]

    swapped_state = []
    for row in range(len(state)):
        new_row = []
        for column in range(len(state[row])):
            if row == r1 and column == c1:
                new_row.append(value2)
            elif row == r2 and column == c2:
                new_row.append(value1)
            else:
                new_row.append(state[row][column])
        swapped_state.append(tuple(new_row))
    return tuple(swapped_state)


def create_goal_state(n):
    """
	Returns the goal state for a n-puzzle.
	"""

    goalState = []
    val = 0

    for r in range(n):
        new_row = []
        for c in range(n):
            new_row.append(val)
            val += 1
        goalState.append(tuple(new_row))

    return tuple(goalState)


def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise.
    """
    n = len(state)
    goalState = create_goal_state(n)

    return (state == goalState)


def get_solution(goalState, initialState, parents, actions):
    """
    Recovers the sequence of actions taken from initial to goal state.
    """

    soln = []
    state = goalState

    while state != initialState:
        soln.append(actions[state])
        state = parents[state]

    soln.reverse()

    #print soln
    return soln


def bfs(initialState):
    """
    Implementing breadth first search.
    Returns four values: A list of actions, and the number of states expanded
    """

    parents = {}
    actions = {}
    solution = []

    states_expanded = 0
    max_frontier = 0

    frontier = [initialState]
    explored = set()

    seenState = set()
    seenState.add(initialState)

    #BFS algorithm
    while len(frontier) != 0:
        node = frontier.pop(0)      #Removing first element from queue
        explored.add(node)
        #states_expanded += 1

        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

        #Solution is reached if current node is the goal state
        if goal_test(node):
            solution = get_solution(node, initialState, parents, actions)
            #print "printing solution"
            break

        states_expanded += 1
        neighbors = expand(node)

        for neighbor in neighbors:
            #Separating actions and neighboring states of current state
            nextState = neighbor[1]
            action = neighbor[0]

            if nextState not in explored and nextState not in seenState:
                parents[nextState] = node
                actions[nextState] = action
                frontier.append(nextState)
                seenState.add(nextState)

    return solution, frontier, max_frontier, states_expanded


def dfs(initialState):
    """
    Depth first search.
    """

    parents = {}
    actions = {}
    solution = []

    states_expanded = 0
    max_frontier = 0

    frontier = [initialState]
    explored = set()
    seenState = set()
    seenState.add(initialState)

    #DFS algorithm
    while len(frontier) != 0:

        node = frontier.pop()                               #Removing last element from stack
        #print node
        states_expanded += 1
        explored.add(node)

        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

        if goal_test(node):
            solution = get_solution(node, initialState, parents, actions)
            break

        neighbors = rev_expand(node)
        for neighbor in neighbors:
            nextState = neighbor[1]
            action = neighbor[0]

            if nextState not in explored and nextState not in seenState:
                parents[nextState] = node
                actions[nextState] = action
                frontier.append(nextState)
                seenState.add(nextState)

    #print solution
    return solution, frontier, max_frontier, states_expanded


def manhattan_distance(curstate):
    """
    Compute the manhattan distance between the current
    position and the goal position. Then sum all distances.
    """

    n = len(curstate)
    md = 0          #manhattan distance

    for r in range(n):
        for c in range(n):
            value = curstate[r][c]
            if value != 0:
                i = int(value/n)
                j = value%n
                # distance is equivalent to difference of indexes
                md += (abs(r - i) + abs(c - j))

    # print md
    return md


def astar(initialState):
    """
    A-star search using manhattan distance as the heuristic.
    """

    parents = {}
    actions = {}

    costs = {}
    costs[initialState] = 0
    solution = []

    states_expanded = 0
    max_frontier = 0

    frontier = [(costs[initialState], initialState)]
    explored = set()

    #A-star algorithm
    while len(frontier) != 0:
        node = heappop(frontier)
        poppedState = node[1]
        explored.add(poppedState)

        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

        if goal_test(poppedState):
            solution = get_solution(poppedState, initialState, parents, actions)
            break

        states_expanded += 1
        neighbors = expand(poppedState)
        # successor in (action, state) format
        for neighbor in neighbors:
            nextState = neighbor[1]
            action = neighbor[0]

            #value for h(n) in f(n) = g(n)+h(n)
            h_value = manhattan_distance(nextState)

            cost = costs[poppedState] + 1    #costs stores value of only g(n)

            if nextState not in costs:
                parents[nextState] = poppedState
                actions[nextState] = action
                costs[nextState] = cost
                heappush(frontier, (cost+h_value, nextState))
            elif cost < costs[nextState]:
                f_value = costs[nextState] + h_value

                index = frontier.index((f_value, nextState))
                frontier[index] = frontier[-1]
                x = frontier.pop()

                costs[nextState] = cost
                parents[nextState] = poppedState
                actions[nextState] = action
                heappush(frontier, (cost+h_value, nextState))

    #print(frontier)
    return solution, frontier, max_frontier, states_expanded


def print_results(solution, states_expanded):
    """
    Helper function to format output according to specification
    """
    if solution is None:
        print "No solution found."
    else:
        print "path_to_goal:", solution
        print "cost_of_path: {}".format(len(solution))
        print "nodes_expanded:", states_expanded
        #print "nodes_expanded: {}".format(states_expanded)
        print "search_depth: {}".format(len(solution))


# Program entry point!
if __name__ == "__main__":

    #input = raw_input()
    input = sys.argv
    method = input[1]
    n_puzzle = input[2]

    n_puzzle = n_puzzle.split(',')
    total = len(n_puzzle)
    rows = int(total ** 0.5)  # Calculate the number of rows which is N-value in this puzzle
    matrix = tuple(n_puzzle[i:i + rows] for i in range(0, total, rows))

    for i in range(rows):
        for j in range(rows):
            matrix[i][j] = int(matrix[i][j])

    n_puzzle = tuple(tuple(x) for x in matrix)
    # print n_puzzle
    # test_state = ((1,2,3), (5,6,7),(0,8,4))

    if (method == "bfs"):
        start = time.time()
        solution, frontier, max_frontier, states_expanded = bfs(n_puzzle)  # Running the search
        end = time.time()
        print_results(solution, states_expanded)
        slen = len(solution)
        print "max_search_depth:", slen+1
        print "running_time: {0:.8f}".format(end - start)

    elif (method == "dfs"):
        start = time.time()
        solution, frontier, max_frontier, states_expanded = dfs(n_puzzle)  # Running the search
        end = time.time()
        print_results(solution, states_expanded)
        print "max_search_depth:", max_frontier
        print "running_time: {0:.8f}".format(end - start)

    elif (method == "ast"):
        start = time.time()
        solution, frontier, max_frontier, states_expanded = astar(n_puzzle)
        print_results(solution, states_expanded)
        end = time.time()
        print "max_search_depth: {}".format(len(solution))
        print "running_time: {0:.8f}".format(end - start)


    # to print max_ram_usage depending on platform
    if sys.platform == "win32":
        import psutil
        print "max_ram_usage:", psutil.Process().memory_info().rss
    else:
        import resource
        print("max_ram_usage:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
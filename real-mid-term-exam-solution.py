from mt_utils import *


class NumberedMaze(Problem):

    def __init__(self):
        # Complete the implementation of initial function by calling
        # the parent constructor and initialize with the initial and goal state
        # Write your code below this line!
        super().__init__((1, 1, 1), (7, 10, 0))  # Initializing the init state and goal state
        self.H1 = list(range(1, 8))  # the row index of the figurine
        self.H2 = list(range(1, 11))  # the column index of the figurine
        self.H3 = list(range(10))  # the numbered value of the current value
        # Write your code above this line!
        self.T = ((1, 5, 3, 4, 3, 6, 7, 1, 1, 6),
                  (4, 4, 3, 4, 2, 6, 2, 6, 2, 5),
                  (1, 3, 9, 4, 5, 2, 4, 2, 9, 5),
                  (5, 2, 3, 5, 5, 6, 4, 6, 2, 4),
                  (1, 3, 3, 2, 5, 6, 5, 2, 3, 2),
                  (2, 5, 2, 5, 5, 6, 4, 8, 6, 1),
                  (9, 2, 3, 6, 5, 6, 2, 2, 2, 0))

    def actions(self, state):
        # Complete the implementation of possible operators.
        # The function should return all next possible actions from the input state.
        # Write your code below this line!
        acts = []
        if state[0] - state[2] > 0 and state[1] - state[2] > 0:
            acts.append(1)
        if state[0] - state[2] > 0:
            acts.append(2)
        if state[0] - state[2] > 0 and state[1] + state[2] < 11:
            acts.append(3)
        if state[1] - state[2] > 0:
            acts.append(4)
        if state[1] + state[2] < 11:
            acts.append(5)
        if state[0] + state[2] < 8 and state[1] - state[2] > 0:
            acts.append(6)
        if state[0] + state[2] < 8:
            acts.append(7)
        if state[0] + state[2] < 8 and state[1] + state[2] < 11:
            acts.append(8)
        return acts
        # Write your code above this line! Delete the 'pass' keyword

    def result(self, state, action):
        # Write a function that return the new state when using the given action in case of the input state
        # Write your code below this line!

        # Checking if the action is inside our boundaries
        if action not in self.actions(state):
            return state

        # Making an editable list from our tuple

        new_state = list(state)

        # The lines for changing the row

        if action in [6, 7, 8]:
            new_state[0] = new_state[0] + new_state[2]
        elif action in [1, 2, 3]:
            new_state[0] = new_state[0] - new_state[2]
        else:
            new_state[0] = state[0]

        # The lines for changing the column

        if action in [3, 5, 8]:
            new_state[1] = new_state[1] + new_state[2]
        elif action in [1, 4, 6]:
            new_state[1] = new_state[1] - new_state[2]
        else:
            new_state[1] = new_state[1]

        new_state[2] = self.T[new_state[0] - 1][new_state[1] - 1]
        return tuple(new_state)
        # Write your code above this line! Delete the 'pass' keyword.


def breadth_first_graph_search(problem):
    # Write your code below this line!
    frontier = deque([Node(problem.initial)])
    res_path = []
    explored = set()
    while frontier:
        node = frontier.popleft()
        res_path.append(node.state)
        if problem.goal_test(node.state):
            print(res_path)
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
    return None
    # Write your code above this line! Delete the 'pass' keyword.


def main():
    # 1. Exercise: Fill in the missing parts of init function and print out the initial state (1 point)
    # Write your code below this line!
    our_maze = NumberedMaze()
    print(our_maze.initial)
    # Write your code above this line! Delete the 'pass' keyword.

    # 2. Exercise: Fill out the actions function and test if it works correctly (using the initial state) (3 points)
    # Write your code below this line!
    print(our_maze.actions(our_maze.initial))
    # Write your code above this line!

    # 3. Exercise: Fill out the result function and test if it works correctly (3 points)
    # Write your code below this line!
    print(our_maze.result(our_maze.initial, 8))
    # Write your code above this line!

    # 4. Fill out the breadth_first_graph_search function and solve the problem using it (1.5 point)
    # Write your code below this line!
    print(breadth_first_graph_search(our_maze))
    # Write your code above this line!


if __name__ == '__main__':
    main()

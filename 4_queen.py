from search import Problem, Trial_Error


def convert_state_to_list(state):
    return [list(x) for x in state]


def covert_list_to_state(state):
    return tuple([tuple(x) for x in state])
class FourQueensProblem(Problem):
    def __init__(self):
        # Fill out the __init__ call with only the initial state of the problem (in tuple of tuples format)
        # super().__init__()
        super().__init__((
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
        ))

    def actions(self, state):
        # Return a list of possible actions in "o i j" format where
        # i is the row (from 1 to 4) and j is the column (from 1 to 4)
        acts = []
        for i in range(4):
            for j in range(4):
                if state[i][j] == 0:
                    acts.append(f"o {i+1} {j+1}")

    def result(self, state, action):
        # Return with the new state of the result of the action parameter used in the state parameter.
        # Tip: don't forget to convert state to list of lists and then convert the result back to tuple of tuples
        pass

    def goal_test(self, state):
        # For a given state parameter check if it is a goal state.
        # Tip 1: don't forget conversions; Tip 2: you can use any() or all() for easier implementation
        pass


def main():
    # Test every method that you created: actions, result, goal_test.
    # Also try to solve the problem using the Trial_Error method (found in the search library)
    pass


main()

from search import Problem, Trial_Error


class Cup3(Problem):
    def __init__(self):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        super().__init__((5, 0, 0), [(4, 0, 1), (4, 1, 0)])
        self.H1 = list(range(6))  # 0 1 2 3 4 5
        self.H2 = list(range(4))  # 0 1 2 3
        self.H3 = list(range(3))  # 0 1 2
        self.H = [self.H1, self.H2, self.H3]
        # super().__init__(initial_state, goal_states)

    def actions(self, state):
        """Return all the actions that can be executed in the given
        state"""
        acts = []
        for i in range(3):
            for j in range(3):
                if i != j and state[i] > 0:
                    acts.append(f"o {i+1} {j+1}")
        return acts

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. Assume that the action is one of
        self.actions(state)."""

        pass


def main():
    c = Cup3()
    print(c.initial)
    print(c.H1)
    print(c.H2)
    print(c.H3)
    print(c.H)
    print(c.actions(c.initial))
    print(c.actions((2, 2, 1)))
    # print(Trial_Error(c))


main()

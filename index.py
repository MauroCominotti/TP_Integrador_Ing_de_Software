from simpleai.search import (
    SearchProblem,
    breadth_first
)

from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL = (
    (1, 4, 2),
    (0, 3, 5),
    (6, 7, 8),
)

GOAL = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
)


def where_is(piece, state):
    # find a piece in the board, and return the row and column indexes.
    for row_index, row in enumerate(state):
        for col_index, current_piece in enumerate(row):
            if current_piece == piece:
                return row_index, col_index


class EigthPuzzle(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        return state == GOAL

    def actions(self, state):
        empty_row, empty_col = where_is(0, state)

        available_actions = []

        if(empty_row > 0):  # up
            available_actions.append(state[empty_row - 1][empty_col])

        if(empty_row < 2):  # down
            available_actions.append(state[empty_row + 1][empty_col])

        if(empty_col > 0):  # left
            available_actions.append(state[empty_row][empty_col - 1])

        if(empty_col < 2):  # right
            available_actions.append(state[empty_row][empty_col + 1])
        return available_actions

    def result(self, state, action):
        empty_row, empty_col = where_is(0, state)
        piece_row, piece_col = where_is(action, state)

        state_as_lists = list(list(row) for row in state)

        state_as_lists[empty_row][empty_col] = action
        state_as_lists[piece_row][piece_col] = 0

        new_state = tuple(tuple(row) for row in state_as_lists)
        return new_state


def printing_results(algorithm):
    print("Path from initial goal:")
    for action, state in algorithm.path():
        print("Action:", action)
        print("State:")
        for i in state:  # print as table
            print(", ".join([str(l).rjust(3) for l in i]))
        print()


problem = EigthPuzzle(INITIAL)

# We use the WebViewer to add interactive search viewers
viewer = WebViewer()
breadth_first_result = breadth_first(
    problem, graph_search=True, viewer=viewer)
print("############ breadth_first_result ############")
print("Goal node breadth_first_result:", breadth_first_result)
print()
printing_results(breadth_first_result)

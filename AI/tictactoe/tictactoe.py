"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    move_count = 0
    for row in board:
        for square in row:
            if square is not EMPTY:
                move_count += 1

    if move_count % 2 == 0:
        return X
    else:
        return O


    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] is EMPTY:
                actions.add((i,j))
    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if action not in actions(board) and terminal(board) is not True:
        raise Exception

    board2 = copy.deepcopy(board)
    move = player(board)

    board2[i][j] = move

    return board2

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if ((board[0][0] == board[1][1] and board[1][1] == board [2][2]) or (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[1][1] is not EMPTY):
        return board[1][1]

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]  # Row winner
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]  # Column winner

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False

    return True
    raise NotImplementedError


def utility(board, depth):
    """
    Returns a score based on the outcome of the board and how many moves it took to get there:
    - 1 if X has won, adjusted by depth (sooner wins are better).
    - -1 if O has won, adjusted by depth (slower losses are better for X).
    - 0 for a tie.
    """

    result = winner(board)
    if result == X:
        return 1 - depth * 0.01  # Faster wins are better (lower depth means quicker win)
    elif result == O:
        return -1 + depth * 0.01  # Slower losses are better (higher depth means delayed loss)
    elif terminal(board):
        return 0  # Tie

    # No winner yet, return neutral score
    return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    if terminal(board) == True:
        return None


    if current_player == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action), 1)  # Start depth at 1 for the first move
            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action), 1)  # Start depth at 1 for the first move
            if score < best_score:
                best_score = score
                best_action = action
        return best_action

    raise NotImplementedError


def max_value(board, depth):
    if terminal(board):
        return utility(board, depth)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), depth + 1))
    return v

def min_value(board, depth):
    if terminal(board):
        return utility(board, depth)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), depth + 1))
    return v

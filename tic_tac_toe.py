"""
tic_tac_toe module has functions that allow players to play tic tac toe on console.
These functions display a visual representation of the board, accept user input
for moves, update the game board with those moves, check for winning conditions/draw,
and announce the result of the game once it has concluded. 
Main is a driver that uses these functions to run the game.
"""


def display_board(board):
    """Builds the board for output, returns visual representation of board.

    Parameters:
        board: nested list representing tic tac toe board.

    Returns:
        visual_board a string representation of the tic tac toe board.
    """
    visual_board = f"   1   2   3\n" \
                   f"1  {board[0][0]} | {board[0][1]} | {board[0][2]}\n" \
                   f"   --+---+--\n" \
                   f"2  {board[1][0]} | {board[1][1]} | {board[1][2]}\n" \
                   f"   --+---+--\n" \
                   f"3  {board[2][0]} | {board[2][1]} | {board[2][2]}\n"
    return visual_board


def next_turn(turn):
    """Updates turn variable to appropriate player's move.

    Parameters:
        turn: string representing the player with the move.

    Returns:
        turn after having assigned the appropriate value.
    """
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    return turn


def read_move(turn):
    """Reads player's move from user input and returns the row,column coordinates.

    Parameters:
        turn: string representing the player with the move.

    Returns:
        A tuple (int, int) representing the row, column coordinates of player move.
    """
    move = input(f"Enter {turn} move (row,column no spaces)> ")
    return tuple(int(x.strip()) for x in move.split(','))


def validate_move(move, board):
    """
    Verifies that move is between 1 and 3 and the square is unoccupied.

    Parameters:
        move: tuple (int, int) representing row, column of player move.
        board: nested list representing tic tac toe board.

    Returns: True if valid move, False if invalid move.
    """
    if 1 <= move[0] <= 3 and 1 <= move[1] <= 3 and board[move[0] - 1][move[1] - 1] == " ":
        return True
    else:
        return False


def execute_move(move, board, turn):
    """
    Executes player move and updates game_board, move_count.

    Parameters:
        move: tuple (int, int) representing row, column of player move.
        board: nested list representing tic tac toe board.
        turn: string "X" or "O" indicating who has the move.
    """
    board[move[0] - 1][move[1] - 1] = turn


def is_game_over(board, move_count, turn):
    """
    Determines whether game has ended if conditions met.

    Parameters:
        board: nested list representing tic tac toe board.
        move_count: int for current number of moves in the game.
        turn: string "X" or "O" indicating who has the move.

    Returns: True if the game has ended, False otherwise.
    """
    return move_count >= 5 and board[0][0] == board[0][1] == board[0][2] == turn \
        or board[1][0] == board[1][1] == board[1][2] == turn\
        or board[2][0] == board[2][1] == board[2][2] == turn\
        or board[0][0] == board[1][0] == board[2][0] == turn\
        or board[0][1] == board[1][1] == board[2][1] == turn\
        or board[0][2] == board[1][2] == board[2][2] == turn\
        or board[0][0] == board[1][1] == board[2][2] == turn\
        or board[0][2] == board[1][1] == board[2][0] == turn


def main():
    turn = "X"  # Turn variable tracks which player has the move.
    board = [[" " for _ in range(3)] for _ in range(3)]
    move_count = 1

    draw = False
    while draw is False:
        if move_count > 9:  # Draw condition met when all squares are occupied without a winner.
            draw = True
        else:
            print(display_board(board))
            move = read_move(turn)
            if validate_move(move, board):
                execute_move(move, board, turn)
                move_count = move_count + 1
            else:
                while not validate_move(move, board):  # Loop until valid move supplied by player.
                    print("Invalid move, try again.")
                    move = read_move(turn)
                execute_move(move, board, turn)
                move_count = move_count + 1
            if is_game_over(board, move_count, turn):
                break
            turn = next_turn(turn)
    print(display_board(board))
    if draw is False:
        print(f"{turn} is the winner!")  # Player who last moved must be winner unless a draw occurred.
    else:
        print("The game ended in a draw.")


if __name__ == '__main__':
    main()

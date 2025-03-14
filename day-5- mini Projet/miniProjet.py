def display_board(board):
    """Display the current state of the game board."""
    print("\nCurrent Board:")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print()


def initialize_board():
    """Create an empty 3x3 board."""
    return [[" ", " ", " "] for _ in range(3)]


def check_win(board, player):
    """Check if the specified player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    """Check if the board is full (tie game)."""
    return all(cell != " " for row in board for cell in row)


def get_move(player, board):
    """Get a valid move from the player."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            # Check if the input is valid
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Invalid position. Row and column must be between 0 and 2.")
        except ValueError:
            print("Please enter numbers for row and column.")


def play_game():
    """Main game loop."""
    board = initialize_board()
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Players take turns entering row (0-2) and column (0-2) to place their mark.")

    while True:
        display_board(board)

        # Get the player's move
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        # Check for win
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break

        # Check for tie
        if is_board_full(board):
            display_board(board)
            print("The game is a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


def main():
    """Run the game and handle play again logic."""
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
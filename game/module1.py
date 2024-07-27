import sys

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    """Check if the player has won."""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all([cell != " " for row in board for cell in row])

def get_move():
    """Get the player's move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError
            return divmod(move, 3)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def get_ai_move(board):
    """Get the AI's move using basic rules."""
    # Find the first empty spot (this can be improved with better logic)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return (i, j)

def main():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    ai_enabled = False

    # Check for AI flag in command-line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "-ai" and sys.argv[2].lower() == "true":
        ai_enabled = True

    print("Tic-Tac-Toe Game")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        if ai_enabled and player == "O":
            row, col = get_ai_move(board)
            print(f"AI chooses position ({row * 3 + col + 1})")
        else:
            row, col = get_move()
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        turn += 1

if __name__ == "__main__":
    main()

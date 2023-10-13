def print_board(board):
    print("\nTic Tac Toe Board:\n")
    for row in board:
        print(*row)
    print()


def check_winner(board):
    def check_line(line):
        return line[0] == line[1] == line[2] and isinstance(line[0], str)

    # Check rows and columns
    for i in range(3):
        if check_line(board[i]) or check_line([board[j][i] for j in range(3)]):
            return True

    # Check diagonals
    if check_line([board[i][i] for i in range(3)]) or check_line(
        [board[i][2 - i] for i in range(3)]
    ):
        return True

    return False


def play_tic_tac_toe():
    condition = input("Do you want to play a game of Tic Tac Toe? (Y/N): ")

    if condition.lower() == "y":
        xoBoard = [[0] * 3 for _ in range(3)]  # Board initialization
        print_board(xoBoard)

        count = 9  # No. of turns

        while count != 0:
            xoInputLocation = input("\nEnter a numeric location: ")  # Get user input

            if (
                xoInputLocation.isnumeric() and 1 <= int(xoInputLocation) <= 9
            ):  # Check input validity
                idx = int(xoInputLocation) - 1
                row, col = divmod(idx, 3)

                if xoBoard[row][col] not in ["X", "O"]:
                    player_symbol = "X" if count % 2 == 0 else "O"
                    xoBoard[row][col] = player_symbol
                    print(f"\nInput {player_symbol} at {col},{row}\n")
                    print_board(xoBoard)
                    count -= 1

                    if check_winner(xoBoard):
                        exit("\nGame Over")
                else:
                    print("\nInvalid move. Spot already taken.")
            else:
                print("\nInvalid input. Enter a number within the range.")

        print("\nIt's a tie!")
    else:
        exit("\nAlright! Maybe next time.")


play_tic_tac_toe()
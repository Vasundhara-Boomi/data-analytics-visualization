import numpy as np

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return " " not in board

def main():
    board = np.full((3, 3), " ")
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[current_player]
        print("Player {}, it's your turn.".format(player))

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player
            print_board(board)

            if check_win(board, player):
                print("Player {} wins!".format(player))
                break
            elif is_draw(board):
                print("It's a draw!")
                break

            current_player = 1 - current_player  # Switch players

        else:
            print("Invalid move! Try again.")

if __name__ == "__main__":
    main()

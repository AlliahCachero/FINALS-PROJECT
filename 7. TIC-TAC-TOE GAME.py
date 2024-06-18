
# ICT 09 – Programming 1

# FINAL PROJECT

# 7. Tic-tac-toe game:
# - Create a game of tic-tac-toe in a console mode without another graphical tool. Each player
#   should enter their names and play the game. Every time the player places an input, the
#   program should produce a screen and show the input of the player. This sequence should
#   continue up to the end of the game.

def print_board(board):
    for row in board:
        print("  | ".join(row))
        print("-" * 12)

def check_winner(board, mark):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [mark, mark, mark] in win_conditions

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    player1_name = input("Enter the name for player 1 (X): ")
    player2_name = input("Enter the name for player 2 (O): ")
    
    players = [(player1_name, "X"), (player2_name, "O")]
    current_player = 0

    for _ in range(9):
        print_board(board)
        name, mark = players[current_player]
        row = int(input(f"{name}, enter the row (0-2): "))
        col = int(input(f"{name}, enter the column (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = mark
            if check_winner(board, mark):
                print_board(board)
                print(f"{name} wins!")
                return
            current_player = 1 - current_player
        else:
            print("This cell is already taken. Choose another one.")
    
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()


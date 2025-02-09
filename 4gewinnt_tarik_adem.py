import random

def main():
    print("Vier Gewinnt - Start!")
    game_mode = input("Möchten Sie gegen den Computer spielen? (y/n): ").lower()
    board = initialize_board()
    current_player = 1  # Spieler 1 beginnt
    while True:
        print_board(board)
        if current_player == 1 or game_mode == 'n':
            column = get_move(current_player)
        else:
            column = get_computer_move(board)
        make_move(board, column, current_player)
        if check_winner(board, current_player):
            print_board(board)
            print(f"Spieler {current_player} hat gewonnen!")
            break
        if check_draw(board):
            print_board(board)
            print("Unentschieden!")
            break
        current_player = 3 - current_player  # Wechsel zum anderen Spieler

def initialize_board():
    return [[0 for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))
    print()

def get_move(player):
    column = -1
    while column < 0 or column > 6:
        try:
            column = int(input(f"Spieler {player}, wähle eine Spalte (0-6): "))
        except ValueError:
            pass
    return column

def get_computer_move(board):
    valid_columns = [col for col in range(7) if board[0][col] == 0]
    return random.choice(valid_columns)

def make_move(board, column, player):
    for row in range(5, -1, -1):  # Start bei der letzten Reihe
        if board[row][column] == 0:
            board[row][column] = player
            break

def check_winner(board, player):
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    for row in range(3):
        for col in range(7):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + 3 - i][col + i] == player for i in range(4)):
                return True
    return False

def check_draw(board):
    return all(board[0][col] != 0 for col in range(7))

if __name__ == "__main__":
    main()

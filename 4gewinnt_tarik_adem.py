def main():
    print("Vier Gewinnt - Start!")
    board = initialize_board()
    current_player = 1  # Spieler 1 beginnt
    while True:
        print_board(board)
        column = get_move(current_player)
        make_move(board, column, current_player)
        if check_winner(board, current_player):
            print(f"Spieler {current_player} hat gewonnen!")
            break
        current_player = 3 - current_player  # Spielerwechsel

def initialize_board():
    return [[0 for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def get_move(player):
    column = int(input(f"Spieler {player}, wähle eine Spalte (0-6): "))
    return column

def make_move(board, column, player):
    for row in range(5, -1, -1):  # Start bei der letzten Reihe
        if board[row][column] == 0:
            board[row][column] = player
            break

def check_winner(board, player):
    # Waagrechte Gewinnüberprüfung
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Senkrechte Gewinnüberprüfung
    for row in range(3):
        for col in range(7):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Diagonale Gewinnüberprüfung
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + 3 - i][col + i] == player for i in range(4)):
                return True

    return False

if __name__ == "__main__":
    main()
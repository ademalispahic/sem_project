def main():
    print("Vier Gewinnt - Start!")
    board = initialize_board()
    print_board(board)

def initialize_board():
    return [[0 for _ in range(7)] for _ in range(6)]  # 6 Reihen, 7 Spalten

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

if __name__ == "__main__":
    main()
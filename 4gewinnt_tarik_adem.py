import random
import math


def main():
    """
    Der Einstiegspunkt des Programms, der das Spiel startet.

    Initialisiert das Spiel und fragt den Spieler, ob er gegen den Computer oder mit einem anderen Spieler spielt.

    Returns
    -------
    None
    """
    # Standardwerte für 4 Gewinnt
    default_rows = 6
    default_cols = 7
    default_wincnt = 4

    # Benutzereingabe für Spielmodus (gegen Computer oder 2 Spieler)
    while True:
        game_mode = input("Möchtest du gegen den Computer spielen? (Ja/Nein): ").strip().lower()
        if game_mode == "ja":
            computer_game = 1
            break
        elif game_mode == "nein":
            computer_game = 0
            break
        else:
            print("Ungültige Eingabe, bitte 'Ja' oder 'Nein' eingeben.")

    print(f"Spiel gestartet mit {default_rows} Reihen, {default_cols} Spalten und {default_wincnt} in Reihe für den Gewinn.")
    
    game = Game(default_rows, default_cols, default_wincnt, computer_game)
    game.start()


class Game:
    """
    Eine Klasse, die das Spiel „Vier Gewinnt“ implementiert.

    Attributes
    ----------
    turn : int
        Der aktuelle Spieler (0 für Spieler 1, 1 für Spieler 2).
    cols : int
        Anzahl der Spalten im Spiel (immer 7).
    rows : int
        Anzahl der Reihen im Spiel (immer 6).
    wincnt : int
        Anzahl der Steine in Reihe, um zu gewinnen (immer 4).
    computer_game : int
        1, wenn gegen den Computer gespielt wird, andernfalls 0.
    board : list
        Das Spielfeld als 2D-Liste.
    cfw : CheckForWin
        Instanz der CheckForWin-Klasse zur Gewinnüberprüfung.
    ai : AIMoves
        Instanz der AIMoves-Klasse zur Berechnung der Computerzüge.

    Methods
    -------
    create_board()
        Erstellt das Spielfeld.
    print_board()
        Gibt das Spielfeld auf der Konsole aus.
    get_move(player)
        Fordert den Spieler auf, einen Zug zu wählen.
    make_move(column, player)
        Setzt einen Stein auf das Spielfeld.
    check_winner(player)
        Überprüft, ob der Spieler gewonnen hat.
    check_draw()
        Überprüft, ob das Spiel unentschieden ist.
    start()
        Startet das Spiel und verwaltet den Spielverlauf.
    """

    def __init__(self, rows=6, cols=7, wincnt=4, computer_game=0):
        """
        Initialisiert das Spiel mit den festgelegten Parametern.

        Parameters
        ----------
        rows : int
            Anzahl der Reihen im Spiel.
        cols : int
            Anzahl der Spalten im Spiel.
        wincnt : int
            Anzahl der Steine in Reihe, um zu gewinnen.
        computer_game : int
            1, wenn gegen den Computer gespielt wird, andernfalls 0.
        """
        self.turn = 0
        self.cols = cols
        self.rows = rows
        self.wincnt = wincnt
        self.computer_game = computer_game
        self.board = self.create_board()
        self.cfw = CheckForWin(wincnt)
        self.ai = AIMoves(self.cfw)

    def create_board(self):
        """
        Erstellt das Spielfeld.

        Returns
        -------
        list
            Das Spielfeld als 2D-Liste, die mit 0 initialisiert ist.
        """
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def print_board(self):
        """
        Gibt das Spielfeld auf der Konsole aus.

        Returns
        -------
        None
        """
        for row in self.board:
            print(" ".join(str(cell) if cell != 0 else "." for cell in row))
        print()

    def get_move(self, player):
        """
        Fordert den Spieler auf, eine Spalte für seinen Zug zu wählen.

        Parameters
        ----------
        player : int
            Der aktuelle Spieler (1 oder 2).

        Returns
        -------
        int
            Die gewählte Spalte.
        """
        column = -1
        while column < 0 or column >= self.cols:
            try:
                column = int(input(f"Spieler {player}, wähle eine Spalte (0-{self.cols-1}): "))
                if self.board[0][column] != 0:
                    print("Diese Spalte ist voll, wähle eine andere!")
                    column = -1  # Zuweisung zurücksetzen, wenn die Spalte voll ist
                elif column < 0 or column >= self.cols:
                    print("Ungültige Spalte, wähle eine andere!")
                    column = -1  # Zuweisung zurücksetzen, wenn die Spalte ungültig ist
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl zwischen 0 und 6 eingeben.")
        return column

    def make_move(self, column, player):
        """
        Setzt einen Stein in die gewählte Spalte.

        Parameters
        ----------
        column : int
            Die Spalte, in der der Stein gesetzt wird.
        player : int
            Der aktuelle Spieler (1 oder 2).

        Returns
        -------
        bool
            Gibt True zurück, wenn der Zug gültig war, ansonsten False.
        """
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                return True
        return False

    def check_winner(self, player):
        """
        Überprüft, ob der Spieler gewonnen hat.

        Parameters
        ----------
        player : int
            Der aktuelle Spieler (1 oder 2).

        Returns
        -------
        bool
            True, wenn der Spieler gewonnen hat, sonst False.
        """
        # Horizontal check
        for row in range(self.rows):
            for col in range(self.cols - self.wincnt + 1):
                if all(self.board[row][col + i] == player for i in range(self.wincnt)):
                    return True

        # Vertical check
        for row in range(self.rows - self.wincnt + 1):
            for col in range(self.cols):
                if all(self.board[row + i][col] == player for i in range(self.wincnt)):
                    return True

        # Diagonal (down-right) check
        for row in range(self.rows - self.wincnt + 1):
            for col in range(self.cols - self.wincnt + 1):
                if all(self.board[row + i][col + i] == player for i in range(self.wincnt)):
                    return True

        # Diagonal (up-right) check
        for row in range(self.wincnt - 1, self.rows):
            for col in range(self.cols - self.wincnt + 1):
                if all(self.board[row - i][col + i] == player for i in range(self.wincnt)):
                    return True

        return False

    def check_draw(self):
        """
        Überprüft, ob das Spiel unentschieden ist.

        Returns
        -------
        bool
            True, wenn das Spiel unentschieden ist, sonst False.
        """
        return all(self.board[0][col] != 0 for col in range(self.cols)) and not self.check_winner(1) and not self.check_winner(2)

    def start(self):
        """
        Startet das Spiel und verwaltet den Spielverlauf.

        Returns
        -------
        None
        """
        game_over = False
        turn = 0

        while not game_over:
            self.print_board()

            if turn % 2 == 0:  # Spieler 1
                column = self.get_move(1)
            else:  # Spieler 2
                if self.computer_game == 1:
                    column = self.ai.get_best_move(self.board, 2)  # Computerzug
                else:
                    column = self.get_move(2)

            if not self.make_move(column, 1 if turn % 2 == 0 else 2):
                continue

            if self.check_winner(1 if turn % 2 == 0 else 2):
                self.print_board()
                print(f"Spieler {1 if turn % 2 == 0 else 2} hat gewonnen!")
                game_over = True
                break

            if self.check_draw():
                self.print_board()
                print("Unentschieden!")
                game_over = True
                break

            turn += 1


class CheckForWin:
    """
    Eine Klasse zur Überprüfung von Gewinnbedingungen.

    Attributes
    ----------
    wincnt : int
        Die Anzahl der Steine in Reihe, um zu gewinnen.

    Methods
    -------
    check_winner(board, player)
        Überprüft das Spielfeld auf eine Gewinnkombination für den angegebenen Spieler.
    """

    def __init__(self, wincnt):
        """
        Initialisiert die CheckForWin-Klasse.

        Parameters
        ----------
        wincnt : int
            Die Anzahl der Steine in Reihe, um zu gewinnen.
        """
        self.wincnt = wincnt

    def check_winner(self, board, player):
        """
        Überprüft das Spielfeld auf eine Gewinnkombination für den angegebenen Spieler.

        Parameters
        ----------
        board : list
            Das Spielfeld.
        player : int
            Der aktuelle Spieler (1 oder 2).

        Returns
        -------
        bool
            True, wenn der Spieler gewonnen hat, sonst False.
        """
        # Horizontale Überprüfung
        for row in range(len(board)):
            for col in range(len(board[0]) - self.wincnt + 1):
                if all(board[row][col + i] == player for i in range(self.wincnt)):
                    return True

        # Vertikale Überprüfung
        for row in range(len(board) - self.wincnt + 1):
            for col in range(len(board[0])):
                if all(board[row + i][col] == player for i in range(self.wincnt)):
                    return True

        # Diagonale Überprüfung (down-right)
        for row in range(len(board) - self.wincnt + 1):
            for col in range(len(board[0]) - self.wincnt + 1):
                if all(board[row + i][col + i] == player for i in range(self.wincnt)):
                    return True

        # Diagonale Überprüfung (up-right)
        for row in range(self.wincnt - 1, len(board)):
            for col in range(len(board[0]) - self.wincnt + 1):
                if all(board[row - i][col + i] == player for i in range(self.wincnt)):
                    return True

        return False


class AIMoves:
    """
    Eine Klasse zur Berechnung des besten Zugs für den Computer.

    Attributes
    ----------
    cfw : CheckForWin
        Instanz der CheckForWin-Klasse zur Überprüfung der Gewinnbedingungen.

    Methods
    -------
    get_best_move(board, player)
        Berechnet den besten Zug für den Computer.
    """

    def __init__(self, cfw):
        """
        Initialisiert die AIMoves-Klasse.

        Parameters
        ----------
        cfw : CheckForWin
            Instanz der CheckForWin-Klasse.
        """
        self.cfw = cfw

    def get_best_move(self, board, player):
        """
        Berechnet den besten Zug für den Computer.

        Parameters
        ----------
        board : list
            Das Spielfeld.
        player : int
            Der aktuelle Spieler (1 oder 2).

        Returns
        -------
        int
            Die gewählte Spalte für den besten Zug des Computers.
        """
        valid_columns = [col for col in range(len(board[0])) if board[0][col] == 0]
        return random.choice(valid_columns)


if __name__ == "__main__":
    main()
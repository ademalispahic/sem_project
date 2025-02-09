import unittest
from game import Game



class TestGame(unittest.TestCase):
    def setUp(self):
        # Setup für die Tests
        self.game = Game(rows=6, cols=7, wincnt=4, computer_game=0)  # Standardwerte für das Spiel

    def test_valid_move(self):
        #Test für gültigen Zug
        # Spieler 1 setzt einen Stein in die erste Spalte
        column = 0
        self.assertTrue(self.game.make_move(column, 1))  # Erfolgreicher Zug

    def test_invalid_move_column_full(self):
        # Test für ungültige Züge in eine volle Spalte.

        # Fülle die erste Spalte
        for _ in range(6):
            self.game.make_move(0, 1)  # Spieler 1 setzt Steine in Spalte 0

        # Spieler 2 sollte keinen Zug mehr in Spalte 0 machen können
        self.assertFalse(self.game.make_move(0, 2))  # Spalte ist voll

    def test_check_winner_horizontal(self):
        # Waagrechte Gewinnüberprüfung
        # Setze Steine in einer horizontalen Reihe
        self.game.make_move(0, 1)  # Spieler 1
        self.game.make_move(1, 1)  # Spieler 1
        self.game.make_move(2, 1)  # Spieler 1
        self.game.make_move(3, 1)  # Spieler 1

        self.assertTrue(self.game.check_winner(1))  # Spieler 1 sollte gewonnen haben

    def test_check_winner_vertical(self):
        # Senkrechte Gewinnüberprüfung
        # Setze Steine in einer vertikalen Reihe
        self.game.make_move(0, 1)  # Spieler 1
        self.game.make_move(0, 1)  # Spieler 1
        self.game.make_move(0, 1)  # Spieler 1
        self.game.make_move(0, 1)  # Spieler 1

        self.assertTrue(self.game.check_winner(1))  # Spieler 1 sollte gewonnen haben

if __name__ == '__main__':
    unittest.main()

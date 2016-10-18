
import unittest
from tic_tac_toe import tic_tac_toe_state_checker


class Tic_Tac_Toe_State_Checker_Test(unittest.TestCase):
    """Tests for tic_tac_toe_state_checker from tic_tac_toe.py.
    Checks weather:
    - board is NxN
    - who won X, O or none
    """

    def test_tic_tac_toe_1(self):
        """Test - none won board."""
        board_1 = [
            "XO.",
            ".OX",
            ".X."
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_1), ".")

    def test_tic_tac_toe_2(self):
        """Test - X won board.
        Board contains extra empty line at beginning and end."""
        board_2 = [
            "X..",
            ".X.",
            "..X",
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_2), "X")

    def test_tic_tac_toe_3(self):
        """Test - none won board."""
        board_3 = [
            "O..",
            ".X.",
            "..O",
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_3), ".")

    def test_tic_tac_toe_4(self):
        """Test - O won board."""
        board_4 = [
            "..O..",
            "..O..",
            "..O..",
            "..O..",
            "..O..",
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_4), "O")

    def test_tic_tac_toe_5(self):
        """Test - board is not NxN, return False."""

        board_5 = [
            "XXOO.",
            "...X.",
            "OOOO",
            "...",
            "....."
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_5), False)


if __name__ == '__main__':
    unittest.main()
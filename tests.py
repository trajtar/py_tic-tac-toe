import unittest

import tic_tac_toe


# TODO(lwieczorek) add tests for draw
class TicTacToeStateTest(unittest.TestCase):
    """Tests tic_tac_toe.state."""

    def assert_result(self, board, result):
        self.assertEqual(tic_tac_toe.state(board), result)

    def test_x_won(self):
        """X won."""

        board_a = [
            "X..",
            ".X.",
            "..X",
        ]

        self.assert_result(board_a, 'X')

    def test_o_won(self):
        """O won."""

        board_a = [
            "..O..",
            "..O..",
            "..O..",
            "..O..",
            "..O..",
        ]
        board_b = [
            ".....",
            ".....",
            "OOOOO",
            ".....",
            ".....",
        ]
        self.assert_result(board_a, 'O')
        self.assert_result(board_b, 'O')

    def test_invalid_dimensions(self):
        """Board has invalid dimensions."""

        board = [
            "XX..",
            "...X.",
            "OOOO",
            "...",
            ".....",
        ]
        self.assert_result(board, False)

    def test_no_winner(self):
        """No winner."""

        board_a = [
            "XO.",
            ".OX",
            ".X.",
        ]
        board_b = [
            "O..",
            ".X.",
            "..O",
        ]
        self.assert_result(board_a, '.')
        self.assert_result(board_b, '.')


if __name__ == '__main__':
    unittest.main()

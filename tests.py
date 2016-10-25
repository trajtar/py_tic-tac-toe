import unittest

import tic_tac_toe


# TODO(lwieczorek) add tests for draw
class TicTacToeStateTest(unittest.TestCase):
    """Tests tic_tac_toe.state."""

    def assert_result(self, board, result):
        self.assertEqual(tic_tac_toe.state(board), result)

    def test_no_winner(self):
        """No winner."""

        board_a = [
            "XOO",
            "OXX",
            "XXO",
        ]
        board_b = [
            "OOX",
            "XXO",
            "OXO",
        ]
        self.assert_result(board_a, '.')
        self.assert_result(board_b, '.')

    def test_x_won(self):
        """X won."""

        board = [
            "XOO",
            "OXO",
            "OOX",
        ]
        board_b = [
            "OOX",
            "OXO",
            "XOO",
        ]
        self.assert_result(board, 'X')
        self.assert_result(board_b, 'X')

    def test_o_won(self):
        """O won."""

        board = [
            "XOOOX",
            "XOOXO",
            "XXOXX",
            "OXOXX",
            "XXOOO",
        ]
        self.assert_result(board, 'O')

        board_b = [
            "XOX",
            "OOO",
            "XXO",
        ]
        self.assert_result(board_b, 'O')

    def test_invalid_dimensions(self):
        """Board has invalid dimensions."""

        board = [
            "XXOOX",
            "OXXO",
            "OOOO",
            "OXO",
            "OXOXX",
        ]
        self.assert_result(board, False)

    def test_draw(self):
        """"Draw"""
        board_a = [
            "XOX",
            "XOX",
            "OXO",
        ]
        board_b = [
            "OXX",
            "XOO",
            "XOX",
        ]
        board_c = [
            "OX.",
            "OX.",
            "OX."]

        self.assert_result(board_a, 'XO')
        self.assert_result(board_b, 'XO')
        self.assert_result(board_c, 'XO')


if __name__ == '__main__':
    unittest.main()

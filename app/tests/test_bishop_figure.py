from unittest import TestCase

from app.figures import Bishop


class TestBishop(TestCase):
    def test_list_available_moves(self):
        bishop = Bishop("E4")
        moves = bishop.list_available_moves()
        expected_moves = [
            "F5",
            "G6",
            "H7",
            "D5",
            "C6",
            "B7",
            "A8",
            "F3",
            "G2",
            "H1",
            "D3",
            "C2",
            "B1",
        ]
        self.assertEqual(moves, expected_moves)

    def test_validate_move_valid_move(self):
        bishop = Bishop("D4")
        validated_move = bishop.validate_move("E5")
        self.assertTrue(validated_move)

    def test_validate_move_invalid_move(self):
        bishop = Bishop("D4")
        validated_move = bishop.validate_move("D5")
        self.assertFalse(validated_move)

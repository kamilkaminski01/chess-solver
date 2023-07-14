from unittest import TestCase

from app.figures import King


class TestKing(TestCase):
    def test_list_available_moves(self):
        king = King("E4")
        moves = king.list_available_moves()
        expected_moves = ["D3", "D4", "D5", "E3", "E5", "F3", "F4", "F5"]
        self.assertEqual(moves, expected_moves)

    def test_validate_move_valid_move(self):
        king = King("D4")
        validated_move = king.validate_move("E5")
        self.assertTrue(validated_move)

    def test_validate_move_invalid_move(self):
        king = King("D4")
        validated_move = king.validate_move("D6")
        self.assertFalse(validated_move)

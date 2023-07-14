from unittest import TestCase

from app.figures import Knight


class TestKnight(TestCase):
    def test_list_available_moves(self):
        knight = Knight("D4")
        moves = knight.list_available_moves()
        expected_moves = ["F5", "F3", "B5", "B3", "E6", "E2", "C6", "C2"]
        self.assertEqual(moves, expected_moves)

    def test_validate_move_valid_move(self):
        knight = Knight("D4")
        validated_move = knight.validate_move("B3")
        self.assertTrue(validated_move)

    def test_validate_move_invalid_move(self):
        knight = Knight("D4")
        validated_move = knight.validate_move("D5")
        self.assertFalse(validated_move)

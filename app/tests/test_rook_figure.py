from unittest import TestCase

from app.figures import Rook


class TestRook(TestCase):
    def test_list_available_moves(self):
        rook = Rook("D4")
        moves = rook.list_available_moves()
        expected_moves = [
            "D5",
            "D6",
            "D7",
            "D8",
            "D3",
            "D2",
            "D1",
            "E4",
            "F4",
            "G4",
            "H4",
            "C4",
            "B4",
            "A4",
        ]
        self.assertEqual(moves, expected_moves)

    def test_validate_move_valid_move(self):
        rook = Rook("D4")
        validated_move = rook.validate_move("D5")
        self.assertTrue(validated_move)

    def test_validate_move_invalid_move(self):
        rook = Rook("D4")
        validated_move = rook.validate_move("E5")
        self.assertFalse(validated_move)

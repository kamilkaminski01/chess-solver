from unittest import TestCase

from app.figures import Queen


class TestQueen(TestCase):
    def test_list_available_moves(self):
        queen = Queen("E4")
        moves = queen.list_available_moves()
        expected_moves = [
            "E5",
            "E6",
            "E7",
            "E8",
            "E3",
            "E2",
            "E1",
            "F4",
            "G4",
            "H4",
            "D4",
            "C4",
            "B4",
            "A4",
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
        queen = Queen("A1")
        validated_move = queen.validate_move("H8")
        self.assertTrue(validated_move)

    def test_validate_move_invalid_move(self):
        queen = Queen("A1")
        validated_move = queen.validate_move("F8")
        self.assertFalse(validated_move)

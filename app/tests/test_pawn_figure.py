from unittest import TestCase

from app.figures import Pawn


class TestPawnFigure(TestCase):
    def test_list_available_moves_forward_move(self):
        pawn = Pawn("E3")
        moves = pawn.list_available_moves()
        self.assertEqual(moves, ["E4"])

    def test_list_available_moves_initial_double_move(self):
        pawn = Pawn("E2")
        moves = pawn.list_available_moves()
        self.assertEqual(moves, ["E3", "E4"])

    def test_list_available_moves_invalid_field(self):
        pawn = Pawn("E9")
        moves = pawn.list_available_moves()
        self.assertEqual(moves, [])

    def test_validate_move_valid_move(self):
        pawn = Pawn("E2")
        validated_move = pawn.validate_move("E3")
        self.assertTrue(validated_move)

    def test_validate_move_invalid_move(self):
        pawn = Pawn("E2")
        validated_move = pawn.validate_move("F3")
        self.assertFalse(validated_move)

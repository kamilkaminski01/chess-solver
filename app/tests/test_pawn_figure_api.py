from unittest import TestCase

from app.app import app
from app.exceptions import APIExceptions


class TestPawnAPI(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_list_moves_pawn(self):
        response = self.app.get("/api/v1/pawn/e2")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["figure"], "pawn")
        self.assertEqual(data["currentField"], "E2")
        self.assertEqual(data["error"], None)
        self.assertEqual(data["availableMoves"], ["E3", "E4"])

    def test_list_moves_invalid_figure(self):
        response = self.app.get("/api/v1/invalid_figure/a1")
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["figure"], "invalid_figure")
        self.assertEqual(data["currentField"], "A1")
        self.assertEqual(data["error"], APIExceptions.FigureNotFound)
        self.assertEqual(data["availableMoves"], [])

    def test_list_moves_invalid_field(self):
        response = self.app.get("/api/v1/pawn/h15")
        data = response.get_json()

        self.assertEqual(response.status_code, 409)
        self.assertEqual(data["figure"], "pawn")
        self.assertEqual(data["currentField"], "H15")
        self.assertEqual(data["error"], APIExceptions.FieldNotFound)
        self.assertEqual(data["availableMoves"], [])

    def test_validate_move_valid_move(self):
        response = self.app.get("/api/v1/pawn/e2/e3")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["figure"], "pawn")
        self.assertEqual(data["currentField"], "E2")
        self.assertEqual(data["destField"], "E3")
        self.assertEqual(data["move"], "valid")
        self.assertEqual(data["error"], None)

    def test_validate_move_invalid_move(self):
        response = self.app.get("/api/v1/pawn/e2/f3")
        data = response.get_json()

        self.assertEqual(response.status_code, 409)
        self.assertEqual(data["figure"], "pawn")
        self.assertEqual(data["currentField"], "E2")
        self.assertEqual(data["destField"], "F3")
        self.assertEqual(data["move"], "invalid")
        self.assertEqual(data["error"], APIExceptions.InvalidMove)

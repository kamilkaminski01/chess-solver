from unittest import TestCase

from app.app import app
from app.exceptions import APIExceptions


class TestKingAPI(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_list_moves_king(self):
        response = self.app.get("/api/v1/king/e4")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["figure"], "king")
        self.assertEqual(data["currentField"], "E4")
        self.assertEqual(data["error"], None)
        self.assertEqual(
            data["availableMoves"],
            ["D3", "D4", "D5", "E3", "E5", "F3", "F4", "F5"],
        )

    def test_list_moves_invalid_figure(self):
        response = self.app.get("/api/v1/invalid_figure/a1")
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["figure"], "invalid_figure")
        self.assertEqual(data["currentField"], "A1")
        self.assertEqual(data["error"], APIExceptions.FigureNotFound)
        self.assertEqual(data["availableMoves"], [])

    def test_list_moves_invalid_field(self):
        response = self.app.get("/api/v1/king/h15")
        data = response.get_json()

        self.assertEqual(response.status_code, 409)
        self.assertEqual(data["figure"], "king")
        self.assertEqual(data["currentField"], "H15")
        self.assertEqual(data["error"], APIExceptions.FieldNotFound)
        self.assertEqual(data["availableMoves"], [])

    def test_validate_move_valid_move(self):
        response = self.app.get("/api/v1/king/e4/f5")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["figure"], "king")
        self.assertEqual(data["currentField"], "E4")
        self.assertEqual(data["destField"], "F5")
        self.assertEqual(data["move"], "valid")
        self.assertEqual(data["error"], None)

    def test_validate_move_invalid_move(self):
        response = self.app.get("/api/v1/king/e4/g6")
        data = response.get_json()

        self.assertEqual(response.status_code, 409)
        self.assertEqual(data["figure"], "king")
        self.assertEqual(data["currentField"], "E4")
        self.assertEqual(data["destField"], "G6")
        self.assertEqual(data["move"], "invalid")
        self.assertEqual(data["error"], APIExceptions.InvalidMove)

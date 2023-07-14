from unittest import TestCase

from app.app import app
from app.exceptions import APIExceptions


class TestBishopAPI(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_list_moves_bishop(self):
        response = self.app.get("/api/v1/bishop/d4")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["figure"], "bishop")
        self.assertEqual(data["currentField"], "D4")
        self.assertEqual(data["error"], None)
        self.assertEqual(
            data["availableMoves"],
            [
                "E5",
                "F6",
                "G7",
                "H8",
                "C5",
                "B6",
                "A7",
                "E3",
                "F2",
                "G1",
                "C3",
                "B2",
                "A1",
            ],
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
        response = self.app.get("/api/v1/bishop/h15")
        data = response.get_json()

        self.assertEqual(response.status_code, 409)
        self.assertEqual(data["figure"], "bishop")
        self.assertEqual(data["currentField"], "H15")
        self.assertEqual(data["error"], APIExceptions.FieldNotFound)
        self.assertEqual(data["availableMoves"], [])

    def test_validate_move_valid_move(self):
        response = self.app.get("/api/v1/bishop/d4/e5")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["figure"], "bishop")
        self.assertEqual(data["currentField"], "D4")
        self.assertEqual(data["destField"], "E5")
        self.assertEqual(data["move"], "valid")
        self.assertEqual(data["error"], None)

    def test_validate_move_invalid_move(self):
        response = self.app.get("/api/v1/bishop/d4/e6")
        data = response.get_json()

        self.assertEqual(response.status_code, 409)
        self.assertEqual(data["figure"], "bishop")
        self.assertEqual(data["currentField"], "D4")
        self.assertEqual(data["destField"], "E6")
        self.assertEqual(data["move"], "invalid")
        self.assertEqual(data["error"], APIExceptions.InvalidMove)

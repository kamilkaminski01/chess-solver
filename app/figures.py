from typing import List

from consts import valid_columns, valid_king_moves, valid_knight_moves


class Figure:
    def __init__(self, current_field: str):
        self.current_field = current_field.upper()

    def list_available_moves(self):
        self.current_column = self.current_field[0].upper()
        self.current_row = int(self.current_field[1])
        self.column_index = valid_columns.index(self.current_column)
        self.next_column = (
            valid_columns[self.column_index + 1] if self.column_index + 1 != 8 else None
        )
        self.previous_column = (
            valid_columns[self.column_index - 1] if self.column_index != 0 else None
        )
        self.next_row = self.current_row + 1
        self.previous_row = self.current_row - 1
        self.available_moves = []

    def validate_move(self, dest_field: str) -> bool:
        self.dest_field = dest_field.upper()
        list_of_available_moves = self.list_available_moves()
        return self.dest_field in list_of_available_moves


class Pawn(Figure):
    def list_available_moves(self):
        super().list_available_moves()

        # Forward move
        next_row = self.current_row + 1
        if 1 <= next_row <= 8:
            self.available_moves.append(f"{self.current_column}{next_row}")

        # First double move from the initial position
        if self.current_row == 2:
            next_row = self.current_row + 2
            if 1 <= next_row <= 8:
                self.available_moves.append(f"{self.current_column}{next_row}")

        return self.available_moves


class Knight(Figure):
    def list_available_moves(self) -> List[str]:
        super().list_available_moves()

        for move in valid_knight_moves:
            next_col_index = self.column_index + move[0]
            if 0 <= next_col_index < len(valid_columns):
                next_col = valid_columns[next_col_index]
                next_row = self.current_row + move[1]
                if 1 <= next_row <= 8:
                    self.available_moves.append(f"{next_col}{next_row}")

        return self.available_moves


class Bishop(Figure):
    def list_available_moves(self) -> List[str]:
        super().list_available_moves()
        range_end = len(valid_columns) - self.column_index

        # Diagonal moves towards top-right
        for i in range(1, range_end):
            next_col = valid_columns[self.column_index + i]
            next_row = self.current_row + i
            if next_col is not None and next_row <= 8:
                self.available_moves.append(f"{next_col}{next_row}")
            else:
                break

        # Diagonal moves towards top-left
        for i in range(1, self.column_index + 1):
            prev_col = valid_columns[self.column_index - i]
            next_row = self.current_row + i
            if prev_col is not None and next_row <= 8:
                self.available_moves.append(f"{prev_col}{next_row}")
            else:
                break

        # Diagonal moves towards bottom-right
        for i in range(1, range_end):
            next_col = valid_columns[self.column_index + i]
            prev_row = self.current_row - i
            if next_col is not None and prev_row >= 1:
                self.available_moves.append(f"{next_col}{prev_row}")
            else:
                break

        # Diagonal moves towards bottom-left
        for i in range(1, self.column_index + 1):
            prev_col = valid_columns[self.column_index - i]
            prev_row = self.current_row - i
            if prev_col is not None and prev_row >= 1:
                self.available_moves.append(f"{prev_col}{prev_row}")
            else:
                break

        return self.available_moves


class Rook(Figure):
    def list_available_moves(self) -> List[str]:
        super().list_available_moves()

        # Moves towards the top of the board
        for row in range(self.current_row + 1, 9):
            self.available_moves.append(f"{self.current_column}{row}")

        # Moves towards the bottom of the board
        for row in range(self.current_row - 1, 0, -1):
            self.available_moves.append(f"{self.current_column}{row}")

        # Moves towards the right side of the board
        for col in valid_columns[self.column_index + 1 :]:
            self.available_moves.append(f"{col}{self.current_row}")

        # Moves towards the left side of the board
        for col in reversed(valid_columns[: self.column_index]):
            self.available_moves.append(f"{col}{self.current_row}")

        return self.available_moves


class Queen(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        range_end = len(valid_columns) - self.column_index

        # Moves towards the top of the board
        for row in range(self.current_row + 1, 9):
            self.available_moves.append(f"{self.current_column}{row}")

        # Moves towards the bottom of the board
        for row in range(self.current_row - 1, 0, -1):
            self.available_moves.append(f"{self.current_column}{row}")

        # Moves towards the right side of the board
        for col in valid_columns[self.column_index + 1 :]:
            self.available_moves.append(f"{col}{self.current_row}")

        # Moves towards the left side of the board
        for col in reversed(valid_columns[: self.column_index]):
            self.available_moves.append(f"{col}{self.current_row}")

        # Diagonal moves towards top-right
        for i in range(1, range_end):
            next_col = valid_columns[self.column_index + i]
            next_row = self.current_row + i
            if next_col is not None and next_row <= 8:
                self.available_moves.append(f"{next_col}{next_row}")
            else:
                break

        # Diagonal moves towards top-left
        for i in range(1, self.column_index + 1):
            prev_col = valid_columns[self.column_index - i]
            next_row = self.current_row + i
            if prev_col is not None and next_row <= 8:
                self.available_moves.append(f"{prev_col}{next_row}")
            else:
                break

        # Diagonal moves towards bottom-right
        for i in range(1, range_end):
            next_col = valid_columns[self.column_index + i]
            prev_row = self.current_row - i
            if next_col is not None and prev_row >= 1:
                self.available_moves.append(f"{next_col}{prev_row}")
            else:
                break

        # Diagonal moves towards bottom-left
        for i in range(1, self.column_index + 1):
            prev_col = valid_columns[self.column_index - i]
            prev_row = self.current_row - i
            if prev_col is not None and prev_row >= 1:
                self.available_moves.append(f"{prev_col}{prev_row}")
            else:
                break

        return self.available_moves


class King(Figure):
    def list_available_moves(self) -> List[str]:
        super().list_available_moves()

        for move in valid_king_moves:
            next_col_index = self.column_index + move[0]
            if 0 <= next_col_index < len(valid_columns):
                next_col = valid_columns[next_col_index]
                next_row = self.current_row + move[1]
                if 1 <= next_row <= 8:
                    self.available_moves.append(f"{next_col}{next_row}")

        return self.available_moves


figures = {
    "pawn": Pawn,
    "knight": Knight,
    "bishop": Bishop,
    "rook": Rook,
    "queen": Queen,
    "king": King,
}

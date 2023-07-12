from typing import List

from consts import valid_columns


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
    def list_available_moves(self) -> List[str]:
        super().list_available_moves()

        # For the A column
        if self.current_column == valid_columns[0] and self.current_row != 8:
            self.available_moves.append(f"{self.next_column}{self.next_row}")

        # For the H column
        if self.current_column == valid_columns[7] and self.current_row != 8:
            self.available_moves.append(f"{self.previous_column}{self.next_row}")

        # For the rest of columns
        if self.column_index not in [0, 7] and self.next_row != 9:
            self.available_moves.append(f"{self.previous_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.next_row}")

        return self.available_moves


class Knight(Figure):
    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class Bishop(Figure):
    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class Rook(Figure):
    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class Queen(Figure):
    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        pass


class King(Figure):
    def list_available_moves(self) -> List[str]:
        super().list_available_moves()

        # For the A column and 1 row
        if self.current_column == valid_columns[0] and self.current_row == 1:
            self.available_moves.append(f"{self.current_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.current_row}")

        # For the H column and 1 row
        if self.current_column == valid_columns[7] and self.current_row == 1:
            self.available_moves.append(f"{self.current_column}{self.next_row}")
            self.available_moves.append(f"{self.previous_column}{self.next_row}")
            self.available_moves.append(f"{self.previous_column}{self.current_row}")

        # For the 1st row except the A column and H column
        if (
            self.current_row == 1
            and self.current_column != valid_columns[0]
            and self.current_column != valid_columns[7]
        ):
            self.available_moves.append(f"{self.previous_column}{self.current_row}")
            self.available_moves.append(f"{self.previous_column}{self.next_row}")
            self.available_moves.append(f"{self.current_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.current_row}")

        # For the 8th row except the A column and H column
        if (
            self.current_row == 8
            and self.current_column != valid_columns[0]
            and self.current_column != valid_columns[7]
        ):
            self.available_moves.append(f"{self.previous_column}{self.current_row}")
            self.available_moves.append(f"{self.previous_column}{self.previous_row}")
            self.available_moves.append(f"{self.current_column}{self.previous_row}")
            self.available_moves.append(f"{self.next_column}{self.previous_row}")
            self.available_moves.append(f"{self.next_column}{self.current_row}")

        # For the A column except the 1st row and 8th row
        if self.column_index == 0 and self.current_row not in [1, 8]:
            self.available_moves.append(f"{self.current_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.current_row}")
            self.available_moves.append(f"{self.next_column}{self.previous_row}")
            self.available_moves.append(f"{self.current_column}{self.previous_row}")

        # For the H column except the 1st row and 8th row
        if self.column_index == 7 and self.current_row not in [1, 8]:
            self.available_moves.append(f"{self.current_column}{self.next_row}")
            self.available_moves.append(f"{self.previous_column}{self.next_row}")
            self.available_moves.append(f"{self.previous_column}{self.current_row}")
            self.available_moves.append(f"{self.previous_column}{self.previous_row}")
            self.available_moves.append(f"{self.current_column}{self.previous_row}")

        # For the rest of columns
        if self.column_index not in [0, 7] and self.current_row not in [1, 8]:
            self.available_moves.append(f"{self.current_column}{self.previous_row}")
            self.available_moves.append(f"{self.previous_column}{self.previous_row}")
            self.available_moves.append(f"{self.previous_column}{self.current_row}")
            self.available_moves.append(f"{self.previous_column}{self.next_row}")
            self.available_moves.append(f"{self.current_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.next_row}")
            self.available_moves.append(f"{self.next_column}{self.current_row}")
            self.available_moves.append(f"{self.next_column}{self.previous_row}")

        return self.available_moves


figures = {
    "pawn": Pawn,
    "knight": Knight,
    "bishop": Bishop,
    "rook": Rook,
    "queen": Queen,
    "king": King,
}

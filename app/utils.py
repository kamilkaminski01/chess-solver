from consts import valid_columns, valid_rows


def is_valid_field(field: str) -> bool:
    if len(field) != 2:
        return False

    column = field[0]
    row = field[1]

    if column.upper() not in valid_columns or row not in valid_rows:
        return False

    return True

def is_valid_field(field: str) -> bool:
    if len(field) != 2:
        return False

    column = field[0]
    row = field[1]

    valid_columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
    valid_rows = ["1", "2", "3", "4", "5", "6", "7", "8"]

    if column.upper() not in valid_columns or row not in valid_rows:
        return False

    return True

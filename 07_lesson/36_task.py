def print_operation_table(operation, num_rows: int, num_columns: int):
    for i in range(1, num_columns + 1):
        string_line = str()
        for j in range(1, num_rows + 1):
            string_line += str(operation(i, j)) + " "
        print(string_line)


print_operation_table(lambda x, y: x * y, 6, 6)

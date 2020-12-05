import numpy as np

file = open('input', 'r')
lines = file.readlines()

values = []
for line in lines:
    line = line.rstrip()
    row = np.arange(0, 128)
    column = np.arange(0, 8)
    for char in line:
        rows_len = row.shape[0] // 2
        column_len = column.shape[0] // 2
        if char == 'B':
            row = row[rows_len:]
        elif char == 'F':
            row = row[0:rows_len]
        elif char == 'R':
            column = column[column_len:]
        elif char == 'L':
            column = column[0:column_len]
    values.append(row[0] * 8 + column[0])

seats = np.arange(0, 128 * 8)
values = np.array(values)
missing = np.setdiff1d(seats, values)
for index, value in enumerate(missing):
    if missing[index + 1] != value + 1 and missing[index - 1] != value - 1:
        print(value)
        exit(0)

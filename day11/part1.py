import numpy as np


def process_input():
    arr = np.zeros(shape=(len(lines), len(lines[0]) - 1))
    as_num = 0
    for index, line in enumerate(lines):
        line = line.rstrip()
        for char_ind, char in enumerate(line):
            if char == '.':
                as_num = 1
            elif char == 'L':
                as_num = 2
            elif char == '#':
                as_num = 3
            arr[index, char_ind] = as_num
    arr = np.pad(arr, pad_width=1, mode='constant')
    return arr


def get_neighbours(index1, index2):
    values = []
    values.append(array[index1 + 1][index2])
    values.append(array[index1 - 1][index2])
    values.append(array[index1 + 1][index2 + 1])
    values.append(array[index1 - 1][index2 + 1])
    values.append(array[index1 + 1][index2 - 1])
    values.append(array[index1 - 1][index2 - 1])
    values.append(array[index1][index2 + 1])
    values.append(array[index1][index2 - 1])
    return np.array(values)


def process_step():
    new_arr = array.copy()
    changes = 0
    for index1, row in enumerate(array):
        for index2, num in enumerate(row):
            if index1 == 0 or index1 == array.shape[0]-1:
                continue
            if index2 == 0 or index2 == array.shape[1] - 1:
                continue
            neighbors = get_neighbours(index1, index2)
            if num == 2 and 3 not in neighbors:
                new_arr[index1, index2] = 3
                changes += 1
            if num == 3:
                occurrences = np.count_nonzero(neighbors == 3)
                if occurrences >= 4:
                    new_arr[index1, index2] = 2
                    changes += 1
    return changes, new_arr


with open('day11/input') as file:
    lines = file.readlines()
    array = process_input()
    steps = 0
    while True:
        changes_count, arr = process_step()
        array = arr
        if changes_count == 0:
            break
    print(np.count_nonzero(array == 3))

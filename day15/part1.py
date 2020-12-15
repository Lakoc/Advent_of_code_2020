import numpy as np

with open('input') as file:
    values = [int(value) for value in file.read().split(',')]
    counter = len(values)
    values_all = np.zeros(2020, dtype='u8')
    values_all[0:len(values)] = values

    for i in range(counter, 2020):
        prev = values_all[0:i - 1]
        last = values_all[i - 1]
        if last in prev:
            indexes = np.argwhere(prev == last)
            max_val = indexes.max(axis=0)[0] + 1
            values_all[i] = i - max_val
        else:
            continue
    print(values_all[2019])

import numpy as np


def find_pair():
    for val1 in values:
        for val2 in values:
            if val1 + val2 == number and val1 != val2:
                return val1, val2
    return False


with open('input', 'r') as file:
    numbers = np.array([int(number) for number in file.read().split()])
    preamble = 25
    for index, number in enumerate(numbers):
        if index < preamble:
            continue
        values = numbers[index - preamble: index]
        if find_pair():
            continue
        else:
            print(number)
            exit(0)

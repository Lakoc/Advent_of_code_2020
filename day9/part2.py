import numpy as np


def find_pair():
    for val1 in values:
        for val2 in values:
            if val1 + val2 == number and val1 != val2:
                return val1, val2
    return False


def find_contiguous(num):
    num_sum = 0
    start = 0
    i = 0
    while i < len(numbers):
        number = numbers[i]
        if num_sum > 0:
            num_sum += number
            if num_sum > num:
                start = start + 1
                i = start
                num_sum = 0
                continue
            if num_sum == num:
                arr = numbers[start:i]
                print(arr.min() + arr.max())
                exit(0)
        else:
            num_sum = number
            start = i
        i += 1


with open('day9/input', 'r') as file:
    numbers = np.array([int(number) for number in file.read().split()])
    preamble = 25
    for index, number in enumerate(numbers):
        if index < preamble:
            continue
        values = numbers[index - preamble: index]
        if find_pair():
            continue
        else:
            find_contiguous(number)
            exit(0)

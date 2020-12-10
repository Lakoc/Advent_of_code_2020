import numpy as np

with open('input', 'r') as file:
    numbers = np.array([int(number) for number in file.read().split()])
    built_in_adapter = numbers.max() + 3
    numbers = np.append(numbers, built_in_adapter)
    value = 0
    one_jump = 0
    three_jump = 0
    while True:
        neighbors = numbers[(numbers > value) & (numbers <= value + 3)]
        if len(neighbors) == 0:
            print(one_jump * three_jump)
            exit(0)
        else:
            neighbor = neighbors.min()
            if neighbor - value == 1:
                one_jump += 1
            elif neighbor - value == 3:
                three_jump += 1
            value = neighbor

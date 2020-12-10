import numpy as np

Done = {}


def find_conf(start, to, count):
    if start == to:
        return count + 1
    else:
        if start in Done:
            return Done[start]
        neighbors = numbers[(numbers > start) & (numbers <= start + 3)]
        for neighbor in neighbors:
            count += find_conf(neighbor, to, 0)
        Done[start] = count
    return count


with open('input', 'r') as file:
    numbers = np.array([int(number) for number in file.read().split()])
    built_in_adapter = numbers.max() + 3
    numbers = np.append(numbers, [0, built_in_adapter])
    numbers = np.sort(numbers)
    print(find_conf(0, built_in_adapter, 0))

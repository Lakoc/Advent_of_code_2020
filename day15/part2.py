with open('input') as file:
    values = [int(value) for value in file.read().split(',')]
    indexes = {}

    for i, val in enumerate(values):
        if i != len(values) - 1:
            indexes[val] = i

    while len(values) < 30000000:
        last = values[-1]
        prev = indexes.get(last, - 1)
        indexes[last] = len(values) - 1
        if prev == -1:
            next_item = 0
        else:
            next_item = len(values) - 1 - prev
        values.append(next_item)

print(values[-1])

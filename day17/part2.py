with open('input') as file:
    lines = [line.strip() for line in file.readlines()]
    active = set()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                active.add((i, j, 0, 0))

    for step in range(0, 6):
        new_active = set()
        for x in range(-15, 15):
            for y in range(-15, 15):
                for z in range(-15, 15):
                    for w in range(-15, 15):
                        active_neighbors = 0
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                for dz in [-1, 0, 1]:
                                    for dw in [-1, 0, 1]:
                                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                            continue
                                        if (x + dx, y + dy, z + dz, w + dw) in active:
                                            active_neighbors += 1
                        if (x, y, z, w) in active and (active_neighbors == 2 or active_neighbors == 3):
                            new_active.add((x, y, z, w))
                        elif (x, y, z, w) not in active and active_neighbors == 3:
                            new_active.add((x, y, z, w))
        active = new_active
    print(len(active))

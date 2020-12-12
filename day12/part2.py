with open('input') as file:
    lines = file.readlines()
    position = [0, 0]
    waypoint_dir = 1
    waypoint = [10, 1]
    for line in lines:
        line = line.rstrip()
        n = int(line[1:])
        if line[0] == 'F':
            position[0] += n * waypoint[0]
            position[1] += n * waypoint[1]
        elif line[0] == 'N':
            waypoint[1] += n
        elif line[0] == 'S':
            waypoint[1] -= n
        elif line[0] == 'E':
            waypoint[0] += n
        elif line[0] == 'W':
            waypoint[0] -= n
        elif line[0] == 'L':
            for _ in range(n // 90):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        elif line[0] == 'R':
            for _ in range(n // 90):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    print(abs(position[0]) + abs(position[1]))

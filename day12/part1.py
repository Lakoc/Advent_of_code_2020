def move_in_direction(direction_to_move, value):
    if direction_to_move == 'E':
        position[0] += value
    elif direction_to_move == 'N':
        position[1] += value
    elif direction_to_move == 'W':
        position[0] -= value
    elif direction_to_move == 'S':
        position[1] -= value


def change_direction(angle):
    directions = ['N', 'E', 'S', 'W']
    current_position = directions.index(direction)
    new_dir_diff = int(angle / 90)
    return directions[(current_position + new_dir_diff) % 4]


with open('input') as file:
    lines = file.readlines()
    direction = 'E'
    position = [0, 0]
    for line in lines:
        line = line.rstrip()
        if line[0] == 'F':
            move_in_direction(direction, int(line[1:]))
        elif line[0] == 'N':
            move_in_direction(line[0], int(line[1:]))
        elif line[0] == 'S':
            move_in_direction(line[0], int(line[1:]))
        elif line[0] == 'W':
            move_in_direction(line[0], int(line[1:]))
        elif line[0] == 'E':
            move_in_direction(line[0], int(line[1:]))
        elif line[0] == 'L':
            direction = change_direction(-int(line[1:]))
        elif line[0] == 'R':
            direction = change_direction(int(line[1:]))
    print(abs(position[0]) + abs(position[1]))

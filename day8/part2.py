file = open('input', 'r')
lines = file.readlines()

last_inst_offset = len(lines) - 1

for index, line in enumerate(lines):
    accumulator = 0
    offset = 0
    performed = []
    instruction = line.rstrip()
    code, change = instruction.split(' ')
    if code == 'nop':
        lines[index] = f'jmp {change}'
    elif code == 'jmp':
        lines[index] = f'nop {change}'
    else:
        continue
    while offset not in performed:
        if offset in performed:
            break
        if offset == last_inst_offset:
            print(accumulator)
            exit(0)

        instruction = lines[offset].rstrip()
        code, change = instruction.split(' ')
        performed.append(offset)
        if code == 'nop':
            offset += 1
        elif code == 'acc':
            accumulator = eval(f'{accumulator}{change}')
            offset += 1
        elif code == 'jmp':
            offset = eval(f'{offset}{change}')
    lines[index] = line

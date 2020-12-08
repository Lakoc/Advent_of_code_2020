file = open('input', 'r')
lines = file.readlines()

accumulator = 0
offset = 0
performed = []

while offset not in performed:
    if offset in performed:
        break
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

print(accumulator)

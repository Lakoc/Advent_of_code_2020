import re


def set_value(val):
    val_to_set = 0
    for index in range(0, len(mask)):
        if mask[index] == '0':
            continue
        elif mask[index] == '1':
            val_to_set += pow(2, (len(mask) - index) - 1)
        else:
            val_to_multiply = int(val[index])
            val_to_set += (pow(2, (len(mask) - index) - 1) * val_to_multiply)
    memory[mem_index] = val_to_set


with open('input') as file:
    lines = [line.rstrip() for line in file.readlines()]
    memory = {}
    mask_re = re.compile(r'mask = ([X01]+)')
    value_re = re.compile(r'mem\[(\d+)] = (\d+)')
    mask = mask_re.search(lines[0])[1]
    for line in lines:
        mask_match = mask_re.search(line)
        if mask_match:
            mask = mask_match[1]
        else:
            value_match = value_re.search(line)
            if not value_match:
                exit(1)
            mem_index = value_match[1]
            value = value_match[2]
            set_value("{:036b}".format(int(value)))
    sum_mem = 0
    for val in memory:
        sum_mem += memory[val]
    print(sum_mem)

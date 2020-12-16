with open('input') as file:
    lines = file.readlines()
    ranges = {}
    category = 0
    err_rate = 0
    tickets = []
    for line in lines:
        if line == '\n':
            category += 1
            continue

        if category == 0:
            line = line.strip()
            key, value = line.split(':')
            values = [item.strip() for item in value.split('or')]
            ranges[key] = [{'min': int(num_range.split('-')[0]), 'max': int(num_range.split('-')[1])} for num_range in
                           values]
        elif category == 1:
            line = line.strip()
            if line == 'your ticket:':
                continue
            tickets.append([int(val) for val in line.split(',')])

        elif category == 2:
            line = line.strip()
            if line == 'nearby tickets:':
                continue
            tickets.append([int(val) for val in line.split(',')])

    for ticket in tickets:
        for val in ticket:
            found = False
            for class_name in ranges:
                for num_range in ranges[class_name]:
                    if num_range['min'] <= val <= num_range['max']:
                        found = True
                        break
                if found:
                    break
            if not found:
                err_rate += val
    print(err_rate)

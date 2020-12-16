with open('input') as file:
    lines = file.readlines()
    ranges = {}
    category = 0
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

    valid_tickets = []
    for ticket in tickets:
        valid = True
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
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    ticket_values_class = []
    for index, ticket in enumerate(valid_tickets):
        ticket_values_class.append([])
        for val_index, val in enumerate(ticket):
            ticket_values_class[index].append(set())
            for class_name in ranges:
                for num_range in ranges[class_name]:
                    if num_range['min'] <= val <= num_range['max']:
                        ticket_values_class[index][val_index].add(class_name)

    merged = []
    for index, ticket in enumerate(ticket_values_class):
        for index_val, val in enumerate(ticket):
            if index == 0:
                merged.append(val)
            else:
                merged[index_val] = merged[index_val].intersection(val)

    i = 0
    while i < len(merged):
        if len(merged[i]) > 1:
            i += 1
        else:
            item_to_remove = list(merged[i])[0]
            removed = False
            for index, item in enumerate(merged):
                if index == i:
                    continue
                if item_to_remove in item:
                    removed = True
                    item.remove(item_to_remove)
            if removed:
                i = 0
            else:
                i += 1

    multiplied = 1
    for index, class_name in enumerate(merged):
        name = class_name.pop()
        if 'departure' in name:
            multiplied *= tickets[0][index]
    print(multiplied)

import re


def count_children(children):
    counted = 0
    for child in children:
        counted += child['value']
        if colors[child['color']]:
            counted += child['value'] * count_children(colors[child['color']])
    return counted


file = open('input', 'r')
lines = file.readlines()
colors = {}
for line in lines:
    match = re.search(r'([^\n]+) bags contain ([^\.]*)', line)
    key = match[1]
    if key not in colors:
        colors[key] = []
    values = match[2].split(', ')
    for value in values:
        match = re.search(r'(\d+)\s(.*) bag(s?)', value)
        if match:
            count = match[1]
            color = match[2]
            if color not in colors[key]:
                colors[key].append({'color': color, 'value': int(count)})

print(count_children(colors['shiny gold']))

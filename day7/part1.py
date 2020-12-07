import re


def find_all_children(color_to_find, color_set):
    color_set_iter = color_set
    for color_child in color_set_iter:
        if color_child == color_to_find or color_child not in colors:
            continue
        color_set = color_set.union(find_all_children(color_child, colors[color_child]))
    return color_set


file = open('input', 'r')
lines = file.readlines()
colors = {}
for line in lines:
    match = re.search(r'([^\n]+) bags contain ([^\.]*)', line)
    key = match[1]
    if key not in colors:
        colors[key] = set()
    values = match[2].split(', ')
    for value in values:
        match = re.search(r'\d+\s(.*) bag(s?)', value)
        if match:
            color = match[1]
            if color not in colors[key]:
                colors[key].add(color)

for color in colors:
    colors[color] = find_all_children(color, colors[color])

counter = 0
for color in colors:
    if 'shiny gold' in colors[color]:
        counter += 1
print(counter)

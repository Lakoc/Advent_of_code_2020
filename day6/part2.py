file = open('input', 'r')
lines = file.readlines()

value = 0
intersection = set({})
intersecting = False
for line in lines:
    if line[0] == '\n':
        value += len(intersection)
        intersecting = False
        intersection = set({})
        continue
    line = line.rstrip()
    set_local = set({})
    for char in line:
        set_local.add(char)
    if intersecting:
        intersecting = True
        intersection = intersection.intersection(set_local)
    else:
        intersecting = True
        intersection = set_local

else:
    value += len(intersection)
print(value)

file = open('input', 'r')
lines = file.readlines()

trees = 0
# Strips the newline character
x = 0
y = 0
for line in lines:
    if y % 2:
        y += 1
        continue
    line = line.rstrip()
    if line[x % len(line)] == '#':
        trees += 1
    x += 1
    y += 1

print(trees)

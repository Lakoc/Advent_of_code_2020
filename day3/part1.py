file = open('input', 'r')
lines = file.readlines()

trees = 0
# Strips the newline character
x = 0
for line in lines:
    line = line.rstrip()
    if line[x % len(line)] == '#':
        trees += 1
    x += 3

print(trees)

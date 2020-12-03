file1 = open('input', 'r')
Lines = file1.readlines()

trees = 0
# Strips the newline character
x = 0
for line in Lines:
    line = line.rstrip()
    if line[x % len(line)] == '#':
        trees += 1
    x += 3

print(trees)

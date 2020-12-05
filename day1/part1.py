file = open('input', 'r')
lines = file.readlines()

valid = 0
values = []
# Strips the newline character
for line in lines:
    values.append(int(line.rstrip()))

for val1 in values:
    for val2 in values:
        if val1 + val2 == 2020:
            print(val1 * val2)
            exit(0)

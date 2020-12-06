file = open('input', 'r')
lines = file.readlines()

value = 0
setUnique = set({})
for line in lines:
    if line[0] == '\n':
        value += len(setUnique)
        setUnique = set({})
        continue
    line = line.rstrip()
    for char in line:
        setUnique.add(char)
else:
    value += len(setUnique)
print(value)

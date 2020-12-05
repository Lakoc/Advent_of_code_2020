file = open('input', 'r')
lines = file.readlines()

valid = 0
# Strips the newline character
for line in lines:
    line.rstrip()
    reg, passwd = line.split(': ')
    values, letter = reg.split(' ')
    ind1, ind2 = values.split('-')
    count = passwd.count(letter)
    ind1 = int(ind1) - 1
    ind2 = int(ind2) - 1
    x = passwd[ind1]
    y = passwd[ind2]
    if (x == letter or y == letter) and x != y:
        valid += 1
print(valid)

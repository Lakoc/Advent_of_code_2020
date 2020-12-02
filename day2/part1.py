file1 = open('input', 'r')
Lines = file1.readlines()

valid = 0
# Strips the newline character
for line in Lines:
    line = line[0:-1]
    reg, passwd = line.split(': ')
    values, letter = reg.split(' ')
    min, max = values.split('-')
    count = passwd.count(letter)
    if int(min) <= count <= int(max):
        valid += 1
print(valid)

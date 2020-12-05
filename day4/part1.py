import re

file = open('input', 'r')
lines = file.readlines()

password = ''
valid_passwords = 0


def check_valid_password(passwd):
    if re.search(r'byr::[^\s]*', passwd):
        if re.search(r'iyr::[^\s]*', passwd):
            if re.search(r'eyr::[^\s]*', passwd):
                if re.search(r'hgt::[^\s]*', passwd):
                    if re.search(r':[^\s]*', passwd):
                        if re.search(r'ecl::[^\s]*', passwd):
                            if re.search(r'pid::[^\s]*', passwd):
                                return 1
    return 0


for line in lines:
    if line == '\n':
        valid_passwords += check_valid_password(password)
        password = ''
    line = line.rstrip()
    password += line
valid_passwords += check_valid_password(password)
print(valid_passwords)

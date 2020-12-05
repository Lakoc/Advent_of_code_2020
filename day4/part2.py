import re

file = open('input', 'r')
lines = file.readlines()

password = ''
valid_passwords = 0


def check_valid_password(passwd):
    if re.search(r'byr:(19[2-9]\d|200[0-2])\s', passwd):
        if re.search(r'iyr:(201\d|2020)\s', passwd):
            if re.search(r'eyr:(202\d|2030)\s', passwd):
                if re.search(r'hgt:((1([5-8]\d|9[0-3])cm)|(59|6\d|7[0-6])in)\s', passwd):
                    if re.search(r'hcl:#([a-f]|[0-9]){6}\s', passwd):
                        if re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\s', passwd):
                            if pid := re.search(r'pid:\d{9}\s', passwd):
                                print(pid)
                                return 1
    return 0


for line in lines:
    if line == '\n':
        valid_passwords += check_valid_password(password)
        password = ''
    password += line
valid_passwords += check_valid_password(password + '\n')
print(valid_passwords)

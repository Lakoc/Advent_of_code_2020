import re


def remove_parentheses(expression):
    parentheses_re = re.compile(r'\([\d+* ]+\)')
    reduce_re = re.compile(r'(\d+ [+*] \d+)')
    match = parentheses_re.search(expression)
    while match:
        reduced = match[0]
        to_reduce = reduce_re.search(reduced)
        while to_reduce:
            sub_result = eval(to_reduce[1])
            reduced = reduced.replace(to_reduce[1], f'{sub_result}', 1)
            to_reduce = reduce_re.search(reduced)
        reduced = reduced.replace('(', '')
        reduced = reduced.replace(')', '')
        expression = expression.replace(match[0], reduced, 1)
        match = parentheses_re.search(expression)
    return expression


def calculate(expression):
    expression = remove_parentheses(expression)
    reduce_re = re.compile(r'(\d+ [+*] \d+)')
    match = reduce_re.search(expression)
    while match:
        sub_result = eval(match[1])
        expression = expression.replace(match[1], f'{sub_result}', 1)
        match = reduce_re.search(expression)
    return int(expression)


with open('input') as file:
    lines = [line.strip() for line in file.readlines()]
    result = 0
    for index, line in enumerate(lines):
        result += calculate(line)
    print(result)

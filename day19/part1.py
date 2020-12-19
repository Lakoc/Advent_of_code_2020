import re

values_to_process = []


def get_content(rule, pre):
    res = rules[rule]
    if len(res) == 1 and "" in res[0]:
        return pre + res[0].replace('"', '')
    else:
        values = []
        for index, rule in enumerate(res):
            values.append(process_rules(rule, pre))
        return values


def process_rules(rule_full, pre):
    full = pre
    for index, rule in enumerate(rule_full.split()):
        res = get_content(rule, full)
        if isinstance(res, str):
            full = res
        else:
            for value in res:
                values_to_process.append({index: index + 1, value: value, rule: rule_full})
            full = values_to_process.pop()
    return full


def process_options(index, pre):
    values = []
    for option in rules[index]:
        values.append(process_rules(option, pre))
    return values


with open('day19/input') as file:
    rules = {}
    line = file.readline()
    while line != '\n':
        line = line.strip()
        rule_id, local_rules = line.split(': ')
        local_rules = local_rules.split('|')
        rules[rule_id] = local_rules
        line = file.readline()

    done_re = re.compile(r'"[a-z]+"')
    valid_values = process_options('0', '')
    valid_count = 0
    while line := file.readline().strip():
        if line in valid_values:
            valid_count += 1
    print(valid_count)

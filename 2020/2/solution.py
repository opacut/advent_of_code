import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")
    lines.pop()
entries = list()
for entry in lines:
    e = dict()
    e['min_occurrences'] = entry.split(' ')[0].split('-')[0]
    e['max_occurrences'] = entry.split(' ')[0].split('-')[1]
    e['pattern'] = entry.split(' ')[1][0]
    e['password'] = entry.split(' ')[2]
    entries.append(e)

def NOR(a, b):
    return a!=b and (a==True or b==True)

def validate_password_count_strategy(entry):
    """Day 2. Find the number of valid passwords according to policy"""
    occurrences = entry['password'].count(entry['pattern'])
    return occurrences >= int(entry['min_occurrences']) and occurrences <= int(entry['max_occurrences'])

def validate_password_positional_strategy(entry):
    a = entry['password'][int(entry['min_occurrences'])-1] == entry['pattern']
    try:
        b = entry['password'][int(entry['max_occurrences'])-1] == entry['pattern']
    except IndexError:
        b = False
    return NOR(a=a, b=b)

valid_passwords = 0
for entry in entries:
    if validate_password_positional_strategy(entry=entry):
        valid_passwords = valid_passwords + 1
print(valid_passwords)
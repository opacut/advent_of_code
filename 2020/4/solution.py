import os
import re

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
ALLOWED_EYE_COLORS = ['amb','blu','brn','gry','grn','hzl','oth']
RULES = {
    'byr': "between 1920 and 2002",
    'iyr': "between 2010 and 2020",
    'eyr': "between 2020 and 2030",
    'hgt': "if cm then between 150 and 193; if in then between 59 and 76",
    'hcl': "a # and six alphanumerics",
    'ecl': "in ['amb','blu','brn','gry','grn','hzl','oth']",
    'pid': "nine digit numeric"
}

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = [s.replace("\n", " ") for s in f.read().split("\n\n")]

for line in lines:
    line.replace("\n", " ")

def process_passports(data):
    passports = []
    passport = dict()
    for line in data:
        passport = dict()
        for entry in line.split(" "):
            if entry == '':
                continue
            passport[entry.split(":")[0]] = entry.split(":")[1]
        passports.append(passport)
    return passports

def get_valid_passports(all_passports):
    valid_passports = []
    for passport in all_passports:
        valid = True
        passport_fields = list(passport.keys())
        for field in required_fields:
            valid = field in passport_fields
            if not valid:
                break
        if valid:
            valid_passports.append(passport)
    return valid_passports

def validate_passports(all_passports):
    passports = get_valid_passports(all_passports=all_passports)
    valid_passports = []
    for passport in passports:
        valid = int(passport['byr']) <= 2002 and int(passport['byr']) >= 1920
        if not valid: 
            print(f"Invalid field: passport['byr']:{passport['byr']}. rule: {RULES['byr']}")
            continue
        valid = valid and (int(passport['iyr'])<=2020 and int(passport['iyr'])>=2010)
        if not valid: 
            print(f"Invalid field: passport['iyr']:{passport['iyr']}. rule: {RULES['iyr']}")
            continue
        valid = int(passport['eyr'])<=2030 and int(passport['eyr'])>=2020
        if not valid: 
            print(f"Invalid field: passport['eyr']:{passport['eyr']}. rule: {RULES['eyr']}")
            continue

        if 'in' in passport['hgt']:
            valid = valid and len(passport['hgt'])==4 and int(passport['hgt'][0]+passport['hgt'][1])>=59 and int(passport['hgt'][0]+passport['hgt'][1])<=76
        elif 'cm' in passport['hgt']:
            valid = valid and len(passport['hgt'])==5 and int(passport['hgt'][0]+passport['hgt'][1]+passport['hgt'][2])>=59 and int(passport['hgt'][0]+passport['hgt'][1]+passport['hgt'][2])<=193
        else:
            valid = False
        if not valid: 
            print(f"Invalid field: passport['hgt']:{passport['hgt']}. rule: {RULES['hgt']}")
            continue

        valid = valid and passport['hcl'][0] == '#' and len(passport['hcl'])==7
        for char in passport['hcl']:
            if char == '#':
                continue
            #pdb.set_trace()
            valid = valid and (char.isnumeric() or char in ['a','b','c','d','e','f'])
            if not valid:
                print(f"Invalid character: {char}")
                break
        if not valid: 
            print(f"Invalid field: passport['hcl']:{passport['hcl']}. rule: {RULES['hcl']}")
            continue

        valid = valid and passport['ecl'] in ALLOWED_EYE_COLORS
        if not valid: 
            print(f"Invalid field: passport['ecl']:{passport['ecl']}. rule: {RULES['ecl']}")
            continue

        valid = valid and len(passport['pid']) == 9
        if not valid: 
            print(f"Invalid field: passport['pid']:{passport['pid']}. rule: {RULES['pid']}")
            continue

        for c in passport['pid']:
            valid = valid and c.isnumeric()
        if not valid: 
            print(f"Invalid field: passport['pid']:{passport['pid']}. rule: {RULES['pid']}")
            continue

        if valid:
            valid_passports.append(passport)
    return valid_passports


print(len(validate_passports(all_passports=process_passports(data=lines))))
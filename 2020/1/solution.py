import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")
entries = zip(lines, [True]*len(lines))

def fix_expense_report(entries):
    """Day 1. Find the two entries that sum to 2020."""
    visited_list = {lines[i]: False for i in range(len(lines))}
    for i in entries:
        if i == '' or visited_list[i]:
            continue
        for j in entries:
            if j == '' or visited_list[j]:
                continue
            for k in entries:
                if k == '' or visited_list[k]:
                    continue
                if int(i)+int(j)+int(k) == 2020:
                    print(int(i)*int(j)*int(k))
        visited_list[i] = True
            
fix_expense_report(entries=lines)
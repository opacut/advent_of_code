import os
import pdb
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")

floor = 0
for index, char in enumerate(lines[0]):
    if char == "(":
        floor += 1
    if char == ")":
        floor -= 1
    if floor == -1:
        print(index)
        print(f"{index}: {floor}")

#print(floor)
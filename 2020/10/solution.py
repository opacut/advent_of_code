import os
import pdb
import numpy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = [0]
with open(os.path.join(__location__, 'proof2.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()
    lines = [int(l) for l in lines]
    lines = sorted(lines)
    lines.append(max(lines)+3)

one_D = 0
two_D = 0
three_D = 0
#
# always see if you can connect i+1, i+2, i+3
# that's how many possibilities there are
#
combinations = dict()
for i, l in enumerate(lines):
    combinations[i] = 1
for index, joltage in enumerate(lines):
    #if index == 0 or index == len(lines)-1:
    #    continue
    print(f"{index}: {joltage}")
    #try:
    #    if lines[index+1] - joltage == 1:
    #        one_D += 1
    #    elif lines[index+1] - joltage == 2:
    #        two_D += 1
    #    elif lines[index+1] - joltage == 3:
    #        three_D += 1
    #except IndexError:
    #    pass
    #try:
    #    if lines[index+1] - joltage == 2:
    #        if lines[index+2] - joltage == 1:
    #except IndexError:
    #    pass
    # can be index, or index+1, or index+2, or index+3
    #combinations[index] += 1
    #try:
    if (len(lines)-1>index+1) and (lines[index+1] - joltage == 1):
        combinations[index] += 1
        if (len(lines)-1>index+2) and (lines[index+2] - joltage == 2):
            combinations[index] += 1
        elif (len(lines)-1>index+2) and (lines[index+2] - joltage == 1):
            combinations[index] += 1
            if (len(lines)-1>index+3) and (lines[index+3] - joltage == 1):
                combinations[index] += 1
    #except IndexError:
    #    pass
    #try:
    if (len(lines)-1>index+1) and (lines[index+1] - joltage == 2):
        combinations[index] += 1
        if (len(lines)-1>index+2) and (lines[index+2] - joltage == 1):
            combinations[index] += 1
    #except IndexError:
    #    pass


print(f"one-diff: {one_D}")
print(f"two-diff: {two_D}")
print(f"three-diff: {three_D}")
print(f"one-diff * three-diff = {one_D*three_D}")
print(f"Combinations: {combinations}")
#print(f"Possibilities: {numpy.prod(list(combinations.values()))}")
print(f"Possibilities: {sum(list(combinations.values()))}")
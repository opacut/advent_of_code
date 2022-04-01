import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

PREAMBLE_LENGTH = 25

def is_valid(number, preamble):
    #print(f"\n Processing is_valid on {number} with preamble {preamble}")
    for i, n in enumerate(preamble):
        #print(f"\ni {i}: {n}")
        for j, _n in enumerate(preamble):
            #print(f"j {j}: {_n}")
            if j <= i:
                #print(f"{j} is lower than {i}")
                continue
            else:
                #print(f"{int(n)}+{int(_n)}")
                if int(n)+int(_n) == number:
                    #print(f"Number {number}'s preamble is {preamble}. It's valid because {int(n)}+{int(_n)}={int(n)+int(_n)}")
                    return True
    return False

def find_set_of_numbers(n, lines):
    st = list()
    lines = [int(l) for l in lines]
    for index, start in enumerate(lines):
        sequence = list()
        count = start
        sequence.append(start)
        for nxt in lines[index+1:]:
            count += nxt
            sequence.append(nxt)
            if count == n:
                return sequence
            elif count > n:
                break
    return []

for i, n in enumerate(lines):
    if i < PREAMBLE_LENGTH:
        continue
    preamble = lines[i-PREAMBLE_LENGTH:i]
    if not is_valid(number=int(n), preamble=preamble):
        print(f"Number {n} at position {i} is not valid.")
        sequence = find_set_of_numbers(n=int(n), lines=lines)
        print(f"Sequence is {sequence}. Sum is {sum(sequence)}")
        print(f"Max is {max(sequence)}.")
        print(f"Min is {min(sequence)}.")
        print(f"Sum of min and max is {max(sequence)+min(sequence)}")
        break
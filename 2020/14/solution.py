import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

def apply_mask(mask, binary_value):
    binary_string = str(binary_value).split("b")[1]
    while len(binary_string)<36:
        binary_string = '0'+binary_string
    new_binary_string = ['0']*36
    for index, bit in enumerate(binary_string):
        if mask[index] != bit and mask[index] != 'X':
            new_binary_string[index] = mask[index]
        else:
            new_binary_string[index] = binary_string[index]
    return ''.join(new_binary_string)

mask = ''
mem = dict()
for line in lines:
    if 'mask' in line:
        mask = line.split(" = ")[1]
    else:
        memory_address = line.split('[')[1].split(']')[0]
        masked_string = apply_mask(mask=mask, binary_value=bin(int(line.split(" = ")[1])))
        masked_value = int(masked_string, 2)
        mem[memory_address] = masked_value

print(f"Sum of all values in memory is {sum(list(mem.values()))}")
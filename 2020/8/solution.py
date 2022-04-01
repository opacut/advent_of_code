import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()


changable_lines = [(index, line) for index, line in enumerate(lines) if line.split(" ")[0] == "jmp" or line.split(" ")[0] == "nop"]
indices = [i[0] for i in changable_lines]

def repair_line(index, lines):
    new_lines = list()
    for i, line in enumerate(lines):
        if i == index:
            if line.split(" ")[0] == "jmp":
                new_lines.append("nop "+line.split(" ")[1])
            elif line.split(" ")[0] == "nop":
                new_lines.append("jmp "+line.split(" ")[1])
        else: 
            new_lines.append(line)
    return new_lines

for index in indices:
    _lines = repair_line(index=index, lines=lines)
    read_index = 0
    accumulator = 0
    visited_instructions = list()

    while read_index > -1 and read_index < len(_lines):
        if read_index in visited_instructions:
            #print(f"Infinite loop detected on line {read_index}. ACC value before loop: {accumulator}. Already visited: {visited_instructions}")
            break
        visited_instructions.append(read_index)
        instruction = _lines[read_index]
        operation = instruction.split(" ")[0]
        argument = int(instruction.split(" ")[1])
        #print(f"{read_index}: {operation} {argument}")
        if operation == "acc":
            accumulator += argument
            read_index += 1
        elif operation == "jmp":
            read_index += argument
        else:
            read_index += 1
    else:
        print(f"Program finished. Accumulator value is {accumulator}")

import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = dict()
with open(os.path.join(__location__, 'input.txt')) as f:
    read_lines = f.read().split("\n")
for line in read_lines:
    lines[line] = False


addresses = dict()

def parse_instruction(instruction):
    if len(instruction) == 1: 
        return int(instruction[0])
    elif len(instruction) == 2 and instruction[0] == "NOT":
        return ~ int(instruction[1])
    return 0

def process(temp_lines):
    for line, processed in temp_lines.items():
        #instruction = parse_instruction(line.split()[:-1][:-1])
        if processed:
            continue
        instruction = line.split()[:-1][:-1]
        address = line.split()[-1]
        
        # just number into address
        if len(instruction) == 1 and instruction[0].isnumeric():
            addresses[address] = int(instruction[0])
            lines[line] = True
            print(f"Reading {instruction} into {address}")

        # address into address
        elif len(instruction) == 1 and instruction[0] in addresses.keys():
            addresses[address] = int(addresses[instruction[0]])
            lines[line] = True
            print(f"Reading {addresses[instruction[0]]} into {address}")
        
        # not number
        elif len(instruction) == 2 and instruction[0] == "NOT" and instruction[1].isnumeric():
            #addresses[address] = ~int(instruction[1])
            addresses[address] = 65535-int(instruction[1])
            lines[line] = True
            #print(f"Reading {~int(instruction[1])} into {address}")
            print(f"Reading {65535-int(instruction[1])} into {address}")
    
        # not address
        elif len(instruction) == 2 and instruction[0] == "NOT" and instruction[1] in addresses.keys():
            #addresses[address] = ~int(addresses[instruction[1]])
            addresses[address] = 65535-int(addresses[instruction[1]])
            lines[line] = True
            #print(f"Reading {~int(addresses[instruction[1]])} into {address}")
            print(f"Reading {65535-int(addresses[instruction[1]])} into {address}")

        # AND
        elif len(instruction) == 3 and instruction[1] == "AND":
            if instruction[0].isnumeric():
                first_operand = instruction[0]
            elif instruction[0] in addresses.keys():
                first_operand = addresses[instruction[0]]
            else:
                continue
            if instruction[2].isnumeric():
                second_operand = instruction[2]
            elif instruction[2] in addresses.keys():
                second_operand = addresses[instruction[2]]
            else:
                continue
            addresses[address] = int(first_operand) & int(second_operand)
            lines[line] = True
            print(f"Reading {int(first_operand) & int(second_operand)} into {address}.")
        
        # OR
        elif len(instruction) == 3 and instruction[1] == "OR":
            if instruction[0].isnumeric():
                first_operand = instruction[0]
            elif instruction[0] in addresses.keys():
                first_operand = addresses[instruction[0]]
            else:
                continue
            if instruction[2].isnumeric():
                second_operand = instruction[2]
            elif instruction[2] in addresses.keys():
                second_operand = addresses[instruction[2]]
            else:
                continue
            addresses[address] = int(first_operand) | int(second_operand)
            lines[line] = True
            print(f"Reading {int(first_operand) | int(second_operand)} into {address}.")

        # RSHIFT
        elif len(instruction) == 3 and instruction[1] == "RSHIFT":
            if instruction[0].isnumeric():
                first_operand = instruction[0]
            elif instruction[0] in addresses.keys():
                first_operand = addresses[instruction[0]]
            else:
                continue
            if instruction[2].isnumeric():
                second_operand = instruction[2]
            elif instruction[2] in addresses.keys():
                second_operand = addresses[instruction[2]]
            else:
                continue
            addresses[address] = int(first_operand) >> int(second_operand)
            lines[line] = True
            print(f"Reading {int(first_operand) >> int(second_operand)} into {address}.")

        # LSHIFT
        elif len(instruction) == 3 and instruction[1] == "LSHIFT":
            if instruction[0].isnumeric():
                first_operand = instruction[0]
            elif instruction[0] in addresses.keys():
                first_operand = addresses[instruction[0]]
            else:
                continue
            if instruction[2].isnumeric():
                second_operand = instruction[2]
            elif instruction[2] in addresses.keys():
                second_operand = addresses[instruction[2]]
            else:
                continue
            addresses[address] = int(first_operand) << int(second_operand)
            lines[line] = True
            print(f"Reading {int(first_operand) << int(second_operand)} into {address}.")


#print(f"Addresses at the beginning:")
#for address, value in addresses.items():
#    print(f"{address}: {value}")
#print(f"Process round 1")
#process(temp_lines=lines.copy())
#print(f"Addresses after round 1:")
#for address, value in addresses.items():
#    print(f"{address}: {value}")
#print(f"Process round 2")
#process(temp_lines=lines.copy())
#print(f"Addresses after round 2:")
#for address, value in addresses.items():
#    print(f"{address}: {value}")
while not all(lines.values()):
    process(temp_lines=lines.copy())

print(f"Addresses:")
for address, value in addresses.items():
    print(f"{address}: {value}")
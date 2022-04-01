import os
import pdb
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

def unpack_addresses(addresses):
    lists_to_investigate = list(addresses)
    flat_addresses = list()
    while len(lists_to_investigate)>0:
        for index, address in enumerate(lists_to_investigate):
            if len(address) == 36:
                flat_addresses.append(int(''.join(address)))
            else:
                lists_to_investigate.append(address[0])
                lists_to_investigate.append(address[1])
            del lists_to_investigate[index]
    return flat_addresses


def generate_addresses(binary_address, mask):
    first_X_index = None
    mask = list(mask)
    for i, b in enumerate(binary_address):
        if b == 'X':
            first_X_index = i
    if first_X_index == None:
        return ''.join(binary_address)
    bin_0 = list(copy.deepcopy(binary_address))
    bin_1 = list(copy.deepcopy(binary_address))
    bin_0[first_X_index] = '0'
    bin_1[first_X_index] = '1'
    mask[first_X_index] = '0'
    return [generate_addresses(binary_address=bin_0, mask=mask), generate_addresses(binary_address=bin_1, mask=mask)]


def apply_mask(mask, original_address):
    binary_string = str(original_address).split("b")[1]
    while len(binary_string)<36:
        binary_string = '0'+binary_string
    new_binary_string = ['0']*36

    for index, _ in enumerate(binary_string):
        if mask[index] == '1':
            new_binary_string[index] = '1'
        elif mask[index] == 'X':
            new_binary_string[index] = 'X'
        else:
            new_binary_string[index] = binary_string[index]
            
    recursive_addresses = generate_addresses(binary_address=new_binary_string, mask=mask)
    unpacked_addresses = unpack_addresses(addresses=recursive_addresses)
    return unpacked_addresses

mask = ''
mem = dict()
for line in lines:
    if 'mask' in line:
        mask = line.split(" = ")[1]
    else:
        memory_address = line.split('[')[1].split(']')[0]
        value_to_write = int(line.split(" = ")[1])
        binary_address = bin(int(memory_address))
        addresses_to_write = apply_mask(mask=mask, original_address=binary_address)
        for address in addresses_to_write:
            mem[address] = value_to_write

print(f"Sum of all values in memory is {sum(list(mem.values()))}")
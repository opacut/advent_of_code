import os
import pdb
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = [l.split('x') for l in f.read().split("\n") if l != '']

def calculate_ribbon(lines):
    total_ft = 0
    for line in lines:
        l = int(line[0])
        w = int(line[1])
        h = int(line[2])
        longest = max(l,w,h)
        if longest == l:
            smallest_perimeter = 2*w+2*h
        elif longest == w:
            smallest_perimeter = 2*l+2*h
        elif longest == h:
            smallest_perimeter = 2*l+2*w
        volume = l*w*h
        ribbon_ft = smallest_perimeter+volume
        total_ft += ribbon_ft
    return total_ft
        

def calculate_paper(lines):
    total_sqft = 0
    for line in lines:
        l = int(line[0])
        w = int(line[1])
        h = int(line[2])
        side_a = l*w
        side_b = l*h
        side_c = w*h
        extra_side = min(side_a, side_b, side_c)
        sqft = 2*side_a+2*side_b+2*side_c
        total_sqft += sqft+extra_side
        #print(f"box: {line}. l: {l}, w: {w}, h: {h}. side_a: {side_a}, side_b: {side_b}, side_c: {side_c}, extra_side: {extra_side}. sqft: {sqft}, paper needed: {sqft+extra_side}.")
        #print(f"total sqft is {total_sqft}")
    return total_sqft



print(f"Square feet of paper necessary: {calculate_paper(lines=lines)}")
print(f"Feet of ribbon necessary: {calculate_ribbon(lines=lines)}")
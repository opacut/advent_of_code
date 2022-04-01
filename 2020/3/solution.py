import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

d_x = 3
d_y = 1
slope = [3,1]
tree_symbol = "#"
trees_n = 0



def toboggan_down(slope, map_lines):
    global trees_n
    x = 0
    y = 0
    pattern_length = len(map_lines[0])
    while y < len(map_lines):
        #print(f"Investigating x: {x}, y: {y}, symbol: {map_lines[y][x]}")
        if map_lines[y][x] == tree_symbol:
            trees_n += 1
        
        x = x+slope[0] 
        if x >= pattern_length:
            x = x - pattern_length
        y = y+slope[1]

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
answer = 1
for slope in slopes:
    toboggan_down(slope=slope, map_lines=lines)
    print(f"For slope {slope}, we encounter {trees_n} trees.")
    answer = answer * trees_n
    trees_n = 0    
#toboggan_down(slope=slope, map_lines=lines)
#print(trees_n)
print(f"Answer is {answer}")
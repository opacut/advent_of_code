import pdb
import re
from classes import Board, Point

f = open("13/input.txt", "r")
lines = f.read().split("\n")
print(f"There are {len(lines)} lines.")
#print(lines)
all_points = []
folds = []
print(f"Processing lines...")
for line in lines: 
    point_match = re.search(r"^([0-9]+),([0-9]+)$", line)
    if point_match:
        all_points.append(Point(x=int(point_match.groups()[1]),y=int(point_match.groups()[0]), marked=True))
    fold_match = re.search(f"^fold along ([xy])=(.*)$", line)
    if fold_match:
        folds.append((fold_match.groups()[0], int(fold_match.groups()[1])))
print(f"There are {len(all_points)} points and {len(folds)} folds.")
    

#pdb.set_trace()
size = 0
for point in all_points:
    if point.x > size:
        size = point.x
    if point.y > size:
        size = point.y
size += 1
print(f"Size at the beginning should be {size}")
#pdb.set_trace()
print(f"Building up a board...")
b = Board(size=size, marked_points=all_points)
print(f"Board built!")
#print(f"Board: {b.display()}")
print(f"Folds:")
for fold in folds:
    #fold = folds[0]
    print(f"Applying fold {fold[0]}: {str(fold[1])}")
    b.apply_fold(axis=fold[0], pivot=fold[1])
print(f"There are {b.dot_count} dots.")
print(f"Board: {b.display()}")
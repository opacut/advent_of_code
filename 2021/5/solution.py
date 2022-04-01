import re
from classes import Board, Point, Vector

f = open("5/input.txt", "r")
lines = f.read().split("\n")
#print(f"LINES: {lines}")

all_points = []
all_vectors = []
for line in lines:
    #for point in line.split(" -> "):
    p1 = Point(x=int(line.split(" -> ")[0].split(",")[0]),y=int(line.split(" -> ")[0].split(",")[1]))
    p2 = Point(x=int(line.split(" -> ")[1].split(",")[0]),y=int(line.split(" -> ")[1].split(",")[1]))
    v = Vector(start=p1, stop=p2)
    all_points.append(p1)
    all_points.append(p2)
    all_vectors.append(v)
        #print(f"Point: {point}")
        #print(point)
    #print(f"Line: {line}")
#print(lines)
#b = Board(size=10)
size = 0
for point in all_points:
    if point.x > size:
        size = point.x
    if point.y > size:
        size = point.y
b = Board(size=size+1)
for v in all_vectors:
    b.apply_vector(vector=v)
#print(b.display())
#for p in all_points:
#    print(p.display())
#for v in all_vectors:
#    print(v.display())
print(b.display())
print(f"The greatest overlap is {b.greatest_overlap_value} and it's present on {b.greatest_overlap_count} squares. ")
print(f"At least two overlap on {b.at_least_two_count} squares.")
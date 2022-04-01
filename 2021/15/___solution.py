import pdb
f = open("2021/15/3x3.txt", "r")
lines = f.read().split("\n")
print(f"There are {len(lines)} lines.")
#print(f"{lines}")
points = [[int(p) for p in row] for row in lines]
print(f"{points}")
size = len(points[0])-1
print(f"Size is {size}.")
all_paths = []
initial_point = (0,0)

def generate_paths(point):
    print(f"Processing point {point}")
    if point[0] < size and point[1] < size:
        generate_paths((point[0]+1, point[1]))
        generate_paths((point[0], point[1]+1))
    #pass

print(generate_paths(point=initial_point))
print(all_paths)
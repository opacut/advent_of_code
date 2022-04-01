f = open("2021/15/input.txt", "r")
lines = f.read().split("\n")
print(f"There are {len(lines)} lines.")
#print(f"{lines}")


def get_forward_path():
    points = [[int(pt) for pt in line] for line in lines]
    initial_point = (0,0)
    final_point = (len(lines[-1]), len(lines))
    #print(f"We need to get from {initial_point} to {final_point}")
    current_x = 0
    current_y = 0
    current_point = (current_x,current_y)
    path = []
    value = 0
    while current_x < final_point[0]-1 or current_y < final_point[1]-1:
        #print(f"Visiting point ({current_x},{current_y}), value {points[current_x][current_y]}")
        if current_x >= len(points[0])-1:
            current_y += 1
            path.append((current_x, current_y))
        elif current_y >= len(points[0])-1:
            current_x += 1
            path.append((current_x, current_y))
        else:
            point_right = (current_x, current_y+1)
            point_down = (current_x+1, current_y)
            next_point = point_right if points[current_x][current_y+1] < points[current_x+1][current_y] else point_down
            current_x = next_point[0]
            current_y = next_point[1]
            path.append(next_point)
        value += int(points[current_x][current_y])
    #print(f"Points visited: {path}")
    #print(f"Total value is {value}")
    return path, value

def get_backpath():
    points = [[int(pt) for pt in line] for line in lines]
    final_point = (0,0)
    initial_point = (len(lines[-1])-1, len(lines[-1])-1)
    #print(f"We need to get from {final_point} to {initial_point}")
    current_x = initial_point[0]
    current_y = initial_point[1]
    current_point = (current_x,current_y)
    path = []
    value = 0 - points[current_x][current_y]
    #print(f"Initial value is {value}")
    while current_x > 0 or current_y > 0:
        #print(f"Visiting point ({current_x},{current_y}), value {points[current_x][current_y]}")
        if current_x == 0:
            current_y -= 1
            path.append((current_x, current_y))
        elif current_y == 0:
            current_x -= 1
            path.append((current_x, current_y))
        else:
            point_left = (current_x, current_y-1)
            point_up = (current_x-1, current_y)
            next_point = point_left if points[current_x][current_y-1] < points[current_x-1][current_y] else point_up
            current_x = next_point[0]
            current_y = next_point[1]
            path.append(next_point)
        value += int(points[current_x][current_y])
    #print(f"Points visited: {path}")
    #print(f"Total value is {value}")
    return path, value

front_path, front_path_value = get_forward_path()
backpath, backpath_value = get_backpath()
#print(f"Front path has value {front_path_value} and is {front_path}")
#print(f"Backpath has value {backpath_value} and is {backpath}")
mergers = []
for pt in front_path:
    if pt in backpath:
        mergers.append(pt)
splitters = []
for pt in front_path:
    if pt not in backpath and (pt[0], pt[1]+1) in backpath and (pt[0], pt[1]+1) not in front_path:
        splitters.append((pt, (pt[0],pt[1]+1)))
    if pt not in backpath and (pt[0]+1, pt[1]) in backpath and (pt[0]+1, pt[1]) not in backpath:
        splitters.append((pt, (pt[0]+1,pt[1])))
print(f"Mergers: {mergers}")
print(f"Splitter pairs: {splitters}")

# LESS THAN 960
# LESS THAN 915
subgraph_1_start = (0,1)
subgraph_1_end = (50,57)

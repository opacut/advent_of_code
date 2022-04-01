import os
import pdb
import pprint
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
original_seat_map = []
with open(os.path.join(__location__, 'input.txt')) as f:
    original_seat_map += f.read().split("\n")
    original_seat_map.pop()
    original_seat_map = [list(l) for l in original_seat_map]

EMPTY = "L"
OCCUPPIED = "#"
FLOOR = "."

# for round 2, develop a line-of-sight algorithm
def get_visible(x,y, s_m):
    neighbors = list()
    if s_m[x][y] == '.':
        return neighbors
    log = False
    # tl
    tmp_x=x-1
    tmp_y=y-1
    while tmp_x>-1 and tmp_y>-1:
        if s_m[tmp_x][tmp_y] in ['#', 'L']:
            neighbors.append(s_m[tmp_x][tmp_y])
            if log: 
                print(f"Getting a neighbor of ({x},{y}): ({tmp_x},{tmp_y}) {s_m[tmp_x][tmp_y]}")
            break
        else:
            tmp_x -= 1
            tmp_y -= 1
        
    # t
    tmp_x=x-1
    while tmp_x>-1:
        if s_m[tmp_x][y] in ['#','L']:
            neighbors.append(s_m[tmp_x][y])
            if log:
                print(f"Getting a neighbor of ({x},{y}): ({tmp_x},{y}) {s_m[tmp_x][y]}")
            break
        else:
            tmp_x -= 1
    # tr
    tmp_x=x-1
    tmp_y=y+1
    while tmp_x>-1 and tmp_y<len(s_m[x-1]):
        if s_m[tmp_x][tmp_y] in ['#','L']:
            neighbors.append(s_m[tmp_x][tmp_y])
            if log:
                print(f"Getting a neighbor of ({x},{y}): ({tmp_x},{tmp_y}) {s_m[tmp_x][tmp_y]}")
            break
        else:
            tmp_x -= 1
            tmp_y += 1
    # l
    tmp_y=y-1
    while tmp_y>-1:
        if s_m[x][tmp_y] in ['#','L']:
            neighbors.append(s_m[x][tmp_y])
            if log:
                print(f"Getting a neighbor of ({x},{y}): ({x},{tmp_y}) {s_m[x][tmp_y]}")
            break
        else:
            tmp_y -= 1
    # r
    tmp_y=y+1
    while tmp_y<len(s_m[x]):
        if s_m[x][tmp_y] in ['#','L']:
            neighbors.append(s_m[x][tmp_y])
            if log:
                print(f"Getting a neighbor of ({x},{y}): ({x},{tmp_y}) {s_m[x][tmp_y]}")
            break
        else:
            tmp_y += 1
    # bl
    tmp_x=x+1
    tmp_y=y-1
    while tmp_x<len(s_m) and tmp_y>-1:
        if s_m[tmp_x][tmp_y] in ['#','L']:
            neighbors.append(s_m[tmp_x][tmp_y])
            if log:
                print(f"Getting a neighbor of ({x},{y}): ({tmp_x},{tmp_y}) {s_m[tmp_x][tmp_y]}")
            break
        else:
            tmp_x += 1
            tmp_y -= 1
    # b
    tmp_x=x+1
    while tmp_x<len(s_m):
        if s_m[tmp_x][y] in ['#','L']:
            neighbors.append(s_m[tmp_x][y])
            if log:
                print(f"Getting a neighbor of ({x},{y}): ({tmp_x},{y}) {s_m[tmp_x][y]}")
            break
        else:
            tmp_x += 1
    # br
    tmp_x=x+1
    tmp_y=y+1
    while tmp_x<len(s_m) and tmp_y<len(s_m[x+1]):
        if s_m[tmp_x][tmp_y] in ['#','L']:
            neighbors.append(s_m[tmp_x][tmp_y])
            if log:
                print(f"Getting a neighbor of ({x},{y}): ({tmp_x},{tmp_y}) {s_m[tmp_x][tmp_y]}")
            break
        else:
            tmp_x += 1
            tmp_y += 1
    if log:
        pdb.set_trace()
    return neighbors

def get_adjacent(x,y, s_m):
    neighbors = list()
    # tl
    if x>0 and y>0:
        neighbors.append(s_m[x-1][y-1])
    # t
    if x>0:
        neighbors.append(s_m[x-1][y])
    # tr
        if y<len(s_m[x-1])-1:
            neighbors.append(s_m[x-1][y+1])
    # l
    if y>0:
        neighbors.append(s_m[x][y-1])
    # r
    if y<len(s_m[x])-1:
        neighbors.append(s_m[x][y+1])
    # bl
    if x<len(s_m)-1 and y>0:
        neighbors.append(s_m[x+1][y-1])
    # b
    if x<len(s_m)-1:
        neighbors.append(s_m[x+1][y])
    # br
        if y<len(s_m[x+1])-1:
            neighbors.append(s_m[x+1][y+1])
    return neighbors



def evolve(seat_map):
    #get_neighbors = get_adjacent
    get_neighbors = get_visible
    new_seat_map = copy.deepcopy(seat_map)
    for row_index, row in enumerate(seat_map):
        for seat_index, seat in enumerate(row):
            neighbors = get_neighbors(x=row_index,y=seat_index, s_m=seat_map)
            if seat_map[row_index][seat_index] == "L" and "#" not in neighbors:
                new_seat_map[row_index][seat_index] = "#"
            # for round 2, here should be 5 seats
            elif seat_map[row_index][seat_index] == "#" and len([s for s in neighbors if s == "#"])>=5:
                new_seat_map[row_index][seat_index] = "L"
    return new_seat_map

def play(seat_map):
    occuppied = 0
    new_occuppied = 0
    round_states = dict()
    current_round_index = 1
    begin_round_seat_map = evolve(seat_map=seat_map)
    for row in begin_round_seat_map:
            for seat in row:
                if seat == "#":
                    new_occuppied += 1
    round_states[current_round_index] = new_occuppied
    print(f"occuppied: {new_occuppied}")
    current_round_index += 1
    begin_round_seat_map = evolve(seat_map=begin_round_seat_map)
    for row in begin_round_seat_map:
            for seat in row:
                if seat == "#":
                    new_occuppied += 1
    round_states[current_round_index] = new_occuppied
    print(f"occuppied: {new_occuppied}")
    while round_states[current_round_index] != round_states[current_round_index-1]:
        current_round_index += 1
        occuppied = 0
        for row in begin_round_seat_map:
            for seat in row:
                if seat == "#":
                    occuppied += 1
        round_states[current_round_index] = occuppied
        print(f"occuppied: {occuppied}")
        begin_round_seat_map = evolve(seat_map=begin_round_seat_map)
        


play(seat_map=original_seat_map)

import os
import pdb
from itertools import cycle

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

#current_ship_x = 0
#current_ship_y = 0
#facing = 'E'
#directions = cycle(['N','W','S','E'])
directions_clockwise = ['E','N','W','S']
directions_counterclockwise = ['E','S','W','N']
# {
#   E: y
#   W: -y
#   N: x
#   S: -x
# }

def move_ship_a(lines):
    current_ship_x = 0
    current_ship_y = 0
    facing = 'E'
    for instruction in lines:
        #print(f"Current position: ({current_ship_x},{current_ship_y}). Facing: {facing}. Processing {instruction}.")
        operation = instruction[0]
        argument = int(instruction[1:])
        if (operation == "N") or (operation=="F" and facing=="N"):
            #print(f"Moving {argument} points to the N.")
            current_ship_x += argument
            #print(f"New position is ({current_ship_x}, {current_ship_y})")
        elif (operation == "S") or (operation=="F" and facing=="S"):
            #print(f"Moving {argument} points to the S.")
            current_ship_x -= argument
            #print(f"New position is ({current_ship_x}, {current_ship_y})")
        elif (operation == "E") or (operation=="F" and facing=="E"):
            #print(f"Moving {argument} points to the E.")
            current_ship_y += argument
            #print(f"New position is ({current_ship_x}, {current_ship_y})")
        elif (operation == "W") or (operation=="F" and facing=="W"):
            #print(f"Moving {argument} points to the W.")
            current_ship_y -= argument
            #print(f"New position is ({current_ship_x}, {current_ship_y})")
        elif operation == "L":
            #print(f"Turning {argument} degrees to the {operation}.")
            number_of_turns = int(argument/90)
            current_direction_index = directions_clockwise.index(facing)
            current_direction = directions_clockwise[current_direction_index]
            new_direction_raw = current_direction_index+number_of_turns
            new_direction = directions_clockwise[new_direction_raw%len(directions_clockwise)]
            facing = new_direction
            #print(f"New facing is {facing}")
        elif operation == "R":
            #print(f"Turning {argument} degrees to the {operation}.")
            number_of_turns = int(argument/90)
            current_direction_index = directions_counterclockwise.index(facing)
            current_direction = directions_counterclockwise[current_direction_index]
            new_direction_raw = current_direction_index+number_of_turns
            new_direction = directions_counterclockwise[new_direction_raw%len(directions_counterclockwise)]
            facing = new_direction
            #print(f"New facing is {facing}")

    if current_ship_x > 0:
        x_halfplane = "north"
    else:
        current_ship_x = current_ship_x*-1
        x_halfplane = "south"
    if current_ship_y > 0:
        y_haflplane = "east"
    else:
        current_ship_y = current_ship_y*-1
        y_haflplane = "west"
    return current_ship_x, x_halfplane, current_ship_y, y_haflplane

def rotate_waypoint(x,y,direction, ship_x, ship_y):#, number_of_turns):
    print(f"Rotating waypoint from ({x},{y}) in the direction of")
    x_delta = int(abs(x-ship_x))
    y_delta = int(abs(y-ship_y))
    if direction == "R":
        # xsova suradnica je -y
        # yova suradnica je x
        x_d = -y_delta
        y_d = x_delta
        #x_d = -x_delta
        #y_d = y_delta
        #pdb.set_trace()   
    else:
        #pdb.set_trace()   
        x_d = x_delta
        y_d = -y_delta
        #x_d = y_delta
        #y_d = -x_delta
        #pdb.set_trace()   
    #pdb.set_trace()
    print(f"Rotating waypoint. Ship is at ({ship_x},{ship_y}), waypoint's delta is ({(ship_x-x)*-1 if ship_x>x else x-ship_x},{(ship_y-y)*-1 if ship_y>y else y-ship_y}) which puts it at ({x},{y})")
    print(f"Will be rotated to the {direction}.")
    x = ship_x+x_d
    y = ship_y+y_d
    print(f"Rotated to ({x},{y})")
    return x,y

def calculate_position(x,y):
    ret = []
    if x < 0:
        ret.append("south "+str(x*-1))
    else:
        ret.append("north "+str(x))
    if y < 0:
        ret.append("west "+str(y*-1))
    else:
        ret.append("east "+str(y))
    return ret

def move_waypoint(instructions, x,y, ship_x, ship_y):
    current_waypoint_x = x
    current_waypoint_y = y
    for instruction in instructions:
        operation = instruction[0]
        argument = int(instruction[1:])
        if (operation == "N"):
            current_waypoint_x += argument
        elif (operation == "S"):
            current_waypoint_x -= argument
        elif (operation == "E"):
            current_waypoint_y += argument
        elif (operation == "W"):
            current_waypoint_y -= argument
        elif operation == "L":
            #print(f"Turning: ({calculate_position(x=current_waypoint_x,y=current_waypoint_y)}) to the left.")
            for i in range(int(argument/90)):
                current_waypoint_x, current_waypoint_y = rotate_waypoint(x=current_waypoint_x, y=current_waypoint_y, direction="L", ship_x=ship_x, ship_y=ship_y)#, number_of_turns=int(argument/90))
            #print(f"Turned to ({current_waypoint_x},{current_waypoint_y})")
            #print(f"Turned to ({calculate_position(x=current_waypoint_x,y=current_waypoint_y)})")
        elif operation == "R":
            #print(f"Turning: ({calculate_position(x=current_waypoint_x,y=current_waypoint_y)}) to the right.")
            for i in range(int(argument/90)):
                current_waypoint_x, current_waypoint_y = rotate_waypoint(x=current_waypoint_x, y=current_waypoint_y, direction="R", ship_x=ship_x, ship_y=ship_y)#, number_of_turns=int(argument/90))
        print(f"After instruction {instruction}, waypoint is at ({(ship_x-current_waypoint_x)*-1 if ship_x>current_waypoint_x else current_waypoint_x-ship_x},{(ship_y-current_waypoint_y)*-1 if ship_y>current_waypoint_y else current_waypoint_y-ship_y})")
            #print(f"Turned to ({calculate_position(x=current_waypoint_x,y=current_waypoint_y)})")
            #x > y ? x - y : y - x;

    return current_waypoint_x, current_waypoint_y

def move_ship_to_waypoint(waypoint_x, waypoint_y, ship_x, ship_y, times):
    for i in range(int(times)):
        x_direction = "-" if waypoint_x<ship_x else ""
        y_direction = "-" if waypoint_y<ship_y else ""
        x_delta_value = int(abs(waypoint_x-ship_x))
        #print(f"x_delta_value = int(abs({waypoint_x}-{ship_x})) = {int(abs(waypoint_x-ship_x))}")
        y_delta_value = int(abs(waypoint_y-ship_y))
        #print(f"y_delta_value = int(abs({waypoint_y}-{ship_y})) = {int(abs(waypoint_y-ship_y))}")
        x_delta = x_delta_value*-1 if x_direction=="-" else x_delta_value
        y_delta = y_delta_value*-1 if y_direction=="-" else y_delta_value
        #print(f"ship_x += x_delta == {ship_x} += {x_delta} == {ship_x+x_delta}")
        ship_x += x_delta
        #print(f"ship_y += y_delta == {ship_y} += {y_delta} == {ship_y+y_delta}")
        ship_y += y_delta
        waypoint_x = ship_x + x_delta
        waypoint_y = ship_y + y_delta
    return waypoint_x, waypoint_y, ship_x, ship_y

operation_index = 0
waypoint_x = 1
waypoint_y = 10
ship_x = 0
ship_y = 0
print(f"Initial waypoint: ({waypoint_x},{waypoint_y})")
while operation_index < len(lines):
    next_waypoint_move = list()
    for line in lines[operation_index:]:
        operation_index += 1
        if line[0] == "F":
            break
        next_waypoint_move.append(line)
    print(f"\nNext waypoint move: {next_waypoint_move}")
    waypoint_x, waypoint_y = move_waypoint(instructions=next_waypoint_move, x=waypoint_x,y=waypoint_y, ship_x=ship_x, ship_y=ship_y)
    print(f"Waypoint is at ({waypoint_x},{waypoint_y}), delta ({waypoint_x-ship_x},{waypoint_y-ship_y})")
    if lines[operation_index-1][0] == "F":
        print(f"Moving {lines[operation_index-1][1:]} times. Ship is at ({ship_x},{ship_y}) or {calculate_position(x=ship_x,y=ship_y)}")
        waypoint_x, waypoint_y, ship_x, ship_y = move_ship_to_waypoint(waypoint_x=int(waypoint_x),waypoint_y=int(waypoint_y), ship_x=int(ship_x), ship_y=int(ship_y), times=int(lines[operation_index-1][1:]))
        print(f"Moved. Ship is now at ({ship_x},{ship_y}) or {calculate_position(x=ship_x,y=ship_y)}, waypoint is at ({waypoint_x},{waypoint_y}) or {calculate_position(x=waypoint_x,y=waypoint_y)}")
        print(f"Waypoint is at ({(ship_x-waypoint_x)*-1 if ship_x>waypoint_x else waypoint_x-ship_x},{(ship_y-waypoint_y)*-1 if ship_y>waypoint_y else waypoint_y-ship_y}) relative to the ship.")

print(f"Manhattan distance from origin to {calculate_position(x=ship_x,y=ship_y)} is {int(abs(ship_x))+int(abs(ship_y))}")

# NOT 752515
# NOT 120645
# NOT 115437

# I feel like we need to rewrite the whole thing to always take into acocunt the relative position of the waypoint
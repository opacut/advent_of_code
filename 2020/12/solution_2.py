import os
import pdb
from itertools import cycle

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

directions_clockwise = ['E','N','W','S']
directions_counterclockwise = ['E','S','W','N']

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

def rotate_waypoint(x,y,direction):
    # case quadrant   I
    if x>=0 and y>=0:
        #if direction=="R":
        if direction=="L":
            new_x = y
            new_y = -x
        #elif direction=="L":
        elif direction=="R":
            new_x = -y
            new_y = x
    # case quadrant  II
    elif x>=0 and y<0:
        #if direction=="R":
        if direction=="L":
            new_x = y
            new_y = -x
        #elif direction=="L":
        elif direction=="R":
            new_x = -y
            new_y = x
    # case quadrant III
    elif x<0 and y<0:
        #if direction=="R":
        if direction=="L":
            new_x = y
            new_y = -x
        #elif direction=="L":
        elif direction=="R":
            new_x = -y
            new_y = x
    # case quadrant  IV
    elif x<0 and y>=0:
        #if direction=="R":
        if direction=="L":
            new_x = y
            new_y = -x
        #if direction=="L":
        if direction=="R":
            new_x = -y
            new_y = x
    return new_x, new_y

def move_waypoint(instructions, x,y):
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
            for i in range(int(argument/90)):
                current_waypoint_x, current_waypoint_y = rotate_waypoint(x=current_waypoint_x, y=current_waypoint_y, direction="L")
        elif operation == "R":
            for i in range(int(argument/90)):
                current_waypoint_x, current_waypoint_y = rotate_waypoint(x=current_waypoint_x, y=current_waypoint_y, direction="R")
        print(f"After instruction {instruction}, waypoint is at ({current_waypoint_x},{current_waypoint_y}), which is {calculate_position(x=current_waypoint_x,y=current_waypoint_y)}")
            #print(f"Turned to ({calculate_position(x=current_waypoint_x,y=current_waypoint_y)})")
            #x > y ? x - y : y - x;

    return current_waypoint_x, current_waypoint_y

def move_ship_to_waypoint(waypoint_x,waypoint_y,ship_x,ship_y,times):
    for i in range(times):
        ship_x += waypoint_x
        ship_y += waypoint_y
    return ship_x, ship_y


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
    waypoint_x, waypoint_y = move_waypoint(instructions=next_waypoint_move, x=waypoint_x,y=waypoint_y)
    print(f"Waypoint is at ({waypoint_x},{waypoint_y})")
    if lines[operation_index-1][0] == "F":
        print(f"Moving {lines[operation_index-1][1:]} times. Ship is at ({ship_x},{ship_y}) or {calculate_position(x=ship_x,y=ship_y)}")
        ship_x, ship_y = move_ship_to_waypoint(waypoint_x=int(waypoint_x),waypoint_y=int(waypoint_y), ship_x=int(ship_x), ship_y=int(ship_y), times=int(lines[operation_index-1][1:]))

print(f"Manhattan distance from origin to {calculate_position(x=ship_x,y=ship_y)} is {int(abs(ship_x))+int(abs(ship_y))}")

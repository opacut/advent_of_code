import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")[0]

def move_santa(move_data):
    santa = True
    visited = dict()
    visited[(0,0)] = 1
    current_position_santa = (0,0)
    current_position_robot = (0,0)
    for char in move_data:
        if santa:
            if char == "^":
                current_position_santa = (current_position_santa[0]+1, current_position_santa[1])
            elif char == "v":
                current_position_santa = (current_position_santa[0]-1, current_position_santa[1])
            elif char == "<":
                current_position_santa = (current_position_santa[0], current_position_santa[1]-1)
            elif char == ">":
                current_position_santa = (current_position_santa[0], current_position_santa[1]+1)
        if not santa:
            if char == "^":
                current_position_robot = (current_position_robot[0]+1, current_position_robot[1])
            elif char == "v":
                current_position_robot = (current_position_robot[0]-1, current_position_robot[1])
            elif char == "<":
                current_position_robot = (current_position_robot[0], current_position_robot[1]-1)
            elif char == ">":
                current_position_robot = (current_position_robot[0], current_position_robot[1]+1)
        already_visited = False
        for pos in list(visited.keys()):
            if santa:
                if (current_position_santa[0] == pos[0] and current_position_santa[1] == pos[1]):
                    already_visited = True
                    visited[pos] += 1
            else:
                if (current_position_robot[0] == pos[0] and current_position_robot[1] == pos[1]):
                    already_visited = True
                    visited[pos] += 1
        if not already_visited:
            if santa:
                visited[current_position_santa] = 1
            else:
                visited[current_position_robot] = 1
        santa = not santa
    return visited
    


visited = move_santa(move_data=lines)
houses_visited = len(list(visited.keys()))
print(f"houses visited = {houses_visited}")
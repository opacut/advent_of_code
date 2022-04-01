import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")

#class Light:
#    def __init__(self,x,y,on):
#        self.x = x
#        self.y = y
#        self.on = on
#
#    def turn_on(self):
#        self.on = True
#
#    def turn_off(self):
#        self.on = False
#
#    def toggle(self):
#        if self.on:
#            self.on = False
#        else:
#            self.on = True

class Command:
    def __init__(self, action, start, stop):
        self.action = action
        self.start = start
        self.stop = stop


class Grid:
    def __init__(self, width, height):
        self.lights = dict()
        for i in range(height):
            for j in range(width):
                #self.lights.append((j,i,False))#Light(x=j,y=i, on=False))
                self.lights[(j,i)] = 0

    def get_lights_in_interval(self, start, stop):
        x0 = start[0]
        y0 = start[1]
        x1 = stop[0]+1
        y1 = stop[1]+1
        lights = []
        for i in range(x0,x1):
            for j in range(y0,y1):
                lights.append((i,j))
                #lights.append([light for light in self.lights if light[0]==i and light[1]==j][0])
        return lights

    def apply_command(self, command):
        print(f"Applying command: {command.action} from {command.start} to {command.stop}.")
        lights_in_interval = self.get_lights_in_interval(start=command.start, stop=command.stop)
        print(f"Will use this many lights: {len(lights_in_interval)}.")
        #for light, on in lights_in_interval.items():
        for light in lights_in_interval:
            if command.action == 'toggle':
                self.lights[light] += 2
            if command.action == 'turn_on':
                self.lights[light] += 1
            if command.action == 'turn_off':
                if self.lights[light] > 0:
                    self.lights[light] -= 1


def parse_command(command):
    command_sliced = command.split(' ')
    action = None
    start = None
    stop = None
    if command_sliced[0] == 'toggle':
        action = 'toggle'
        start = (int(command_sliced[1].split(',')[0]),int(command_sliced[1].split(',')[1]))
        stop = (int(command_sliced[3].split(',')[0]), int(command_sliced[3].split(',')[1]))
    elif command_sliced[0] == 'turn':
        if command_sliced[1] == 'on':
            action = 'turn_on'
        else: 
            action = 'turn_off'
        start = (int(command_sliced[2].split(',')[0]),int(command_sliced[2].split(',')[1]))
        stop = (int(command_sliced[4].split(',')[0]), int(command_sliced[4].split(',')[1]))
    return Command(action=action, start=start, stop=stop)


grid = Grid(width=1000, height=1000)
print(f"Loaded grid of width 1000 and height 1000.")
for line in lines:
    if line != '':
        #print(f"Parsing line {line}.")
        command = parse_command(command=line)
        #print(f"Applying command: {command.action} from {command.start} to {command.stop}.")
        grid.apply_command(command)

#print(f"Lights on: {len([y for y in grid.lights if y.on])}")
print(f"Lights on: {len([k for k,v in grid.lights.items() if v])}")
#print(f"Lights off: {len([y for y in grid.lights if not y.on])}")
print(f"Lights off: {len([k for k,v in grid.lights.items() if not v])}")
print(f"Total number: {sum([v for k,v in grid.lights.items()])}")
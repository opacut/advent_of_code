from queue import Queue
import pdb

class Octopus:
    def __init__(self, x, y, energy_level):
        self.x = int(x)
        self.y = int(y)
        self.energy_level = int(energy_level)
        self.flashed = False

    def display(self):
        return f"[{self.x},{self.y}]({self.energy_level})"

    def __eq__(self, other):
        if (isinstance(other, Octopus)):
            return self.x == other.x and self.y == other.y and self.energy_level == other.energy_level


class OctopusSwarm:
    def __init__(self, data):
        self.octopi = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.octopi.append(Octopus(x=i,y=j,energy_level=data[i][j]))
        self.flash_count = 0
        self.synchronization_quotient = 0
        self.synchronization_turn = 0
    
    def xs(self, x):
        octs = []
        for octopus in self.octopi:
            if octopus.x == x:
                octs.append(octopus)
        return octs

    def ys(self, y):
        octs = []
        for octopus in self.octopi:
            if octopus.y == y:
                octs.append(octopus)
        return octs

    def get_octopus_by_coords(self, x, y):
        for octopus in self.octopi:
            if octopus.x == x and octopus.y == y:
                return octopus

    def get_neighbors(self, octopus):
        octs = []
        octs.append(self.get_octopus_by_coords(x=octopus.x, y=octopus.y+1))
        octs.append(self.get_octopus_by_coords(x=octopus.x, y=octopus.y-1))
        octs.append(self.get_octopus_by_coords(x=octopus.x-1, y=octopus.y))
        octs.append(self.get_octopus_by_coords(x=octopus.x+1, y=octopus.y))
        octs.append(self.get_octopus_by_coords(x=octopus.x+1, y=octopus.y+1))
        octs.append(self.get_octopus_by_coords(x=octopus.x+1, y=octopus.y-1))
        octs.append(self.get_octopus_by_coords(x=octopus.x-1, y=octopus.y+1))
        octs.append(self.get_octopus_by_coords(x=octopus.x-1, y=octopus.y-1))
        return [oct for oct in octs if oct]

    
    def display(self):
        ret_str = "\n"
        for row_index in range(len(self.xs(x=0))):
            for octopus in self.xs(x=row_index):
                ret_str += " "+str(octopus.energy_level)
            ret_str += "\n"
        print(ret_str)
                
    def evolve_steps(self, steps=1):
        for s in range(steps):
            self.evolve()
            #print(f"After step {s}:")
            #print(self.display())

    def evolve(self):
        for octopus in self.octopi:
            octopus.energy_level += 1
        changed = True
        while changed:
            changed = False
            for octopus in self.octopi:
                if octopus.energy_level > 9 and not octopus.flashed:
                    changed = True
                    octopus.flashed = True
                    self.flash_count += 1
                    octopus.energy_level = 0
                    for neighbor in self.get_neighbors(octopus=octopus):
                        if not neighbor.flashed:
                            neighbor.energy_level += 1
        for octopus in self.octopi:
            octopus.flashed = False

    @property
    def synchronized(self):
        for i in range(10):
            for octopus in self.octopi:
                if octopus.energy_level != i:
                    break
            else:
                return i
    
    def synchronize(self):
        count = 0
        while not self.synchronized:
            self.evolve()
            count += 1
        self.synchronization_turn = count
        self.synchronization_quotient = self.synchronized
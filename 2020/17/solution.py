import os
import pdb
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'proof.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

ACTIVE="#"
INACTIVE="."


class Cube:
    def __init__(self, x, y, z, active=False):
        self.x = x
        self.y = y
        self.z = z
        self.active = active
    
    def __eq__(self, other):
        if isinstance(other, Cube):
            return self.name == other.name
        return False

    @property
    def name(self):
        return f"({self.x},{self.y},{self.z}, {self.active})"

    #@property
    #def active_neighbors(self):
    #    [neighbor for neighbor in self.neighbors if neighbor.active]


class Space:
    def __init__(self, init_string_list):
        self.cubes = list()
        #self.active_cubes = list()
        for x_index, line in enumerate(lines):
            for y_index, cube in enumerate(line):
                #if cube==ACTIVE:
                #    self.active_cubes.append(Cube(x=x_index, y=y_index, z=0, active=True))
                    #self.cubes.append(Cube(x=x_index, y=y_index, z=0, active=True))
                #else:
                    #active_cubes.append(Cube(x=x_index, y=y_index, z=0, active=False))
                self.cubes.append(Cube(x=x_index, y=y_index, z=0, active=cube==ACTIVE))
        self.append_border_planes()
    
    #@property
    #def cubes(self):
    #    return self.cubes
    def get_cube(self, x,y,z):
        try:
            return [cube for cube in self.cubes if x==cube.x and y==cube.y and z==cube.z][0]
        except IndexError:
            return None

    def neighbors(self, x,y,z):
        neighbors = list()
        cube = self.get_cube(x=x,y=y,z=z)
        # z0_tl
        if self.get_cube(x=cube.x-1, y=cube.y-1, z=cube.z):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y-1, z=cube.z))
        else:    
            neighbors.append(Cube(x=cube.x-1, y=cube.y-1, z=cube.z))
        #z0_t
        if self.get_cube(x=cube.x-1, y=cube.y, z=cube.z):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y, z=cube.z))
        else:
            neighbors.append(Cube(x=cube.x-1, y=cube.y, z=cube.z))
        #z0_tr
        if self.get_cube(x=cube.x-1, y=cube.y+1, z=cube.z):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y+1, z=cube.z))
        else:
            neighbors.append(Cube(x=cube.x-1, y=cube.y+1, z=cube.z))
        #z0_l
        if self.get_cube(x=cube.x, y=cube.y-1, z=cube.z):
            neighbors.append(self.get_cube(x=cube.x, y=cube.y-1, z=cube.z))
        else:
            neighbors.append(Cube(x=cube.x, y=cube.y-1, z=cube.z))
        #z0_r
        if self.get_cube(x=cube.x, y=cube.y+1, z=cube.z):
            neighbors.append(self.get_cube(x=cube.x, y=cube.y+1, z=cube.z))
        else:
            neighbors.append(Cube(x=cube.x, y=cube.y+1, z=cube.z))
        #z0_bl
        if self.get_cube(x=cube.x+1, y=cube.y-1, z=cube.z):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y-1, z=cube.z))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y-1, z=cube.z))
        #z0_b
        if self.get_cube(x=cube.x+1, y=cube.y, z=cube.z):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y, z=cube.z))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y, z=cube.z))
        #z0_br
        if self.get_cube(x=cube.x+1, y=cube.y+1, z=cube.z):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y+1, z=cube.z))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y+1, z=cube.z))

        # z1_tl
        if self.get_cube(x=cube.x-1, y=cube.y-1, z=cube.z+1):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y-1, z=cube.z+1))
        else:    
            neighbors.append(Cube(x=cube.x-1, y=cube.y-1, z=cube.z+1))
        #z1_t
        if self.get_cube(x=cube.x-1, y=cube.y, z=cube.z+1):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y, z=cube.z+1))
        else:
            neighbors.append(Cube(x=cube.x-1, y=cube.y, z=cube.z+1))
        #z1_tr
        if self.get_cube(x=cube.x-1, y=cube.y+1, z=cube.z+1):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y+1, z=cube.z+1))
        else:
            neighbors.append(Cube(x=cube.x-1, y=cube.y+1, z=cube.z+1))
        #z1_l
        if self.get_cube(x=cube.x, y=cube.y-1, z=cube.z+1):
            neighbors.append(self.get_cube(x=cube.x, y=cube.y-1, z=cube.z+1))
        else:
            neighbors.append(Cube(x=cube.x, y=cube.y-1, z=cube.z+1))
        #z1_r
        if self.get_cube(x=cube.x, y=cube.y+1, z=cube.z+1):
            neighbors.append(self.get_cube(x=cube.x, y=cube.y+1, z=cube.z+1))
        else:
            neighbors.append(Cube(x=cube.x, y=cube.y+1, z=cube.z+1))
        #z1_bl
        if self.get_cube(x=cube.x+1, y=cube.y-1, z=cube.z+1):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y-1, z=cube.z+1))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y-1, z=cube.z+1))
        #z1_b
        if self.get_cube(x=cube.x+1, y=cube.y, z=cube.z+1):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y, z=cube.z+1))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y, z=cube.z+1))
        #z1_br
        if self.get_cube(x=cube.x+1, y=cube.y+1, z=cube.z+1):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y+1, z=cube.z+1))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y+1, z=cube.z+1))

        # zminus_tl
        if self.get_cube(x=cube.x-1, y=cube.y-1, z=cube.z-1):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y-1, z=cube.z-1))
        else:    
            neighbors.append(Cube(x=cube.x-1, y=cube.y-1, z=cube.z-1))
        #zminus_t
        if self.get_cube(x=cube.x-1, y=cube.y, z=cube.z-1):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y, z=cube.z-1))
        else:
            neighbors.append(Cube(x=cube.x-1, y=cube.y, z=cube.z-1))
        #zminus_tr
        if self.get_cube(x=cube.x-1, y=cube.y+1, z=cube.z-1):
            neighbors.append(self.get_cube(x=cube.x-1, y=cube.y+1, z=cube.z-1))
        else:
            neighbors.append(Cube(x=cube.x-1, y=cube.y+1, z=cube.z-1))
        #zminus_l
        if self.get_cube(x=cube.x, y=cube.y-1, z=cube.z-1):
            neighbors.append(self.get_cube(x=cube.x, y=cube.y-1, z=cube.z-1))
        else:
            neighbors.append(Cube(x=cube.x, y=cube.y-1, z=cube.z-1))
        #zminus_r
        if self.get_cube(x=cube.x, y=cube.y+1, z=cube.z-1):
            neighbors.append(self.get_cube(x=cube.x, y=cube.y+1, z=cube.z-1))
        else:
            neighbors.append(Cube(x=cube.x, y=cube.y+1, z=cube.z-1))
        #zminus_bl
        if self.get_cube(x=cube.x+1, y=cube.y-1, z=cube.z-1):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y-1, z=cube.z-1))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y-1, z=cube.z-1))
        #zminus_b
        if self.get_cube(x=cube.x+1, y=cube.y, z=cube.z-1):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y, z=cube.z-1))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y, z=cube.z-1))
        #zminus_br
        if self.get_cube(x=cube.x+1, y=cube.y+1, z=cube.z-1):
            neighbors.append(self.get_cube(x=cube.x+1, y=cube.y+1, z=cube.z-1))
        else:
            neighbors.append(Cube(x=cube.x+1, y=cube.y+1, z=cube.z-1))
        return neighbors

    def evolve(self):
        cubes_copy = copy.deepcopy(self.cubes)
        for cube_index, cube in enumerate(self.cubes):
            active_neighbors = [n for n in self.neighbors(x=cube.x,y=cube.y,z=cube.z) if n.active]
            if cube.active: 
                if len(active_neighbors)==2 or len(active_neighbors)==3:
                    continue
                else:
                    cubes_copy[cube_index].active = False
            else:
                if len(active_neighbors)==3:
                    cubes_copy[cube_index].active = True
        self.cubes = copy.deepcopy(cubes_copy)
        self.append_border_planes()

    def print(self):
        min_z = min([cube.z for cube in self.cubes])
        max_z = max([cube.z for cube in self.cubes])
        z_range = range(min_z, max_z+1)
        print("Board:")
        for z in z_range:
            print(f"z={z}")
            print(f"{[cube.name for cube in self.cubes if cube.z==z]}")


    @property
    def active_cubes(self):
        return [cube for cube in self.cubes if cube.active]     

    def append_border_planes(self):
        #retlist = cubes_list
        
        min_x = min([cube.x for cube in self.active_cubes])
        max_x = max([cube.x for cube in self.active_cubes])
        #x_range = range(min_x, max_x+1)
    
        min_y = min([cube.y for cube in self.active_cubes])
        max_y = max([cube.y for cube in self.active_cubes])
        #y_range = range(min_y, max_y+1)

        min_z = min([cube.z for cube in self.active_cubes])
        max_z = max([cube.z for cube in self.active_cubes])
        #z_range = range(min_z, max_z+1)

        for cube in self.active_cubes:
            if cube.x == max_x:
                self.cubes.append(Cube(x=max_x+1, y=cube.y, z=cube.z))
            if cube.x == min_x:
                self.cubes.append(Cube(x=min_x-1, y=cube.y, z=cube.z))
            if cube.y == max_y:
                self.cubes.append(Cube(x=cube.x, y=max_y+1, z=cube.z))
            if cube.y == min_y:
                self.cubes.append(Cube(x=cube.x, y=min_y-1, z=cube.z))
            if cube.z == max_z:
                self.cubes.append(Cube(x=cube.x, y=cube.y, z=max_z+1))
            if cube.z == min_z:
                self.cubes.append(Cube(x=cube.x, y=cube.y, z=min_z-1))
        #return retlist

#active_cubes = list()
#all_cubes = list()
#for x_index, line in enumerate(lines):
#    for y_index, cube in enumerate(line):
#        if cube==ACTIVE:
#            active_cubes.append(Cube(x=x_index, y=y_index, z=0, active=True))
#            all_cubes.append(Cube(x=x_index, y=y_index, z=0, active=True))
#        else:
#            active_cubes.append(Cube(x=x_index, y=y_index, z=0, active=False))
#            all_cubes.append(Cube(x=x_index, y=y_index, z=0, active=False))
        #all_cubes.append(Cube(x=x_index, y=y_index, z=-1, active=False))
        #all_cubes.append(Cube(x=x_index, y=y_index, z=1, active=False))
    #if y_index == 0:
    #    active_cubes.append(Cube(x=x_index, y=-1, z=0, active=False))
    #if y_index == len(line)-1:
    #    active_cubes.append(Cube(x=x_index, y=len(line), z=0))
#if x_index == 0:
#    active_cubes.append(Cube(x=-1,y=,x=, active=False))

space = Space(init_string_list=lines)

#print(f"pre-cycle active cubes: {[cube.name for cube in space.active_cubes]}")
#for z in 
print("Start")
space.print()
print("\n\nEvolving...")
space.evolve()
space.print()

#for cycle_index in range(1,7):
#    print(f"Cycle {cycle_index}")
#    space.evolve()
#    space.print()

    
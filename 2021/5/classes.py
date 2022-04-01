from math import sqrt
import pdb

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def display(self):
        return f"[{self.x},{self.y}]"

    @property
    def dist_from_origin(self):
        return sqrt(self.x * self.x) + sqrt(self.y * self.y)
    
class Vector:
    def __init__(self, start, stop):
        if start.dist_from_origin > stop.dist_from_origin:
            self.start = stop
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.x_inc = self.stop.x - self.start.x
        self.y_inc = self.stop.y - self.start.y
        
    @property
    def x_inc_unit(self):
        return int(self.x_inc / self.number_of_steps)

    @property
    def y_inc_unit(self):
        return int(self.y_inc / self.number_of_steps)

    @property
    def length(self):
        pass

    def display(self):
        return f"{self.start.display()} -> {self.stop.display()}"
    
    def swap(self):
        tmp = self.start
        self.start = self.stop
        self.stop = tmp

    @property
    def number_of_steps(self):
        if self.x_inc == 0:
            return abs(self.y_inc)
        return abs(self.x_inc)

    #def modulus(self):
    #    return sqrt(self.x*self.x + self.y*self.y)

class Board:
    def __init__(self, size):
        self.size = size
        self.squares = []
        for i in range(size):
            self.squares.append([])
            for j in range(size):
                self.squares[i].append(0)

    @property    
    def greatest_overlap_value(self):
        greatest = 0
        for row in self.squares:
            for sq in row:
                if sq > greatest:
                    greatest = sq
        return greatest

    @property
    def greatest_overlap_count(self):
        count = 0
        val = self.greatest_overlap_value
        for row in self.squares:
            for sq in row:
                if sq == val:
                    count += 1
        return count

    @property
    def at_least_two_count(self):
        count = 0
        for row in self.squares:
            for sq in row:
                if sq > 1:
                    count += 1
        return count
        

    def apply_vector(self, vector):
        #x_diff = vector.stop.x - vector.start.x
        #y_diff = vector.stop.y - vector.start.y
        #print(f"Processing vector {vector.display()}. X diff is {x_diff}, Y diff is {y_diff}")
        points_visited = []
        if vector.x_inc != 0 and vector.y_inc != 0:
            #print("Not a valid vector.")
            points_visited.append(vector.start)
            print(f"We have a diagonal vector: {vector.display()}")
            #pdb.set_trace()
            #pdb.set_trace()
            for i in range(vector.number_of_steps):
                print(f"Adding point [{vector.start.x+vector.x_inc_unit*i+vector.x_inc_unit*1},{vector.start.y+vector.y_inc_unit*i+vector.y_inc_unit*1}]")
                points_visited.append(Point(x=vector.start.x+vector.x_inc_unit*i+vector.x_inc_unit*1, y=vector.start.y+vector.y_inc_unit*i+vector.y_inc_unit*1))
        elif vector.x_inc != 0:
            points_visited.append(vector.start)
            for i in range(vector.x_inc):
                points_visited.append(Point(x=vector.start.x+i+1, y=vector.start.y))
        elif vector.y_inc != 0:
            points_visited.append(vector.start)
            for i in range(vector.y_inc):
                points_visited.append(Point(x=vector.start.x, y=vector.start.y+i+1))
        for point in points_visited:
            self.squares[point.y][point.x] += 1
        #print(self.display())


    def display(self):
        display_string = ""
        for i in range(self.size):
            display_string += "\n"
            for j in range(self.size):
                display_string += str(self.squares[i][j])
        return display_string

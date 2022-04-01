import pdb

class Point:
    def __init__(self, x, y, marked=False):
        self.x = x
        self.y = y
        self.marked = marked

    def __eq__(self, other):
        if (isinstance(other, Point)):
            return self.x == other.x and self.y == other.y

    def display(self):
        if self.marked:
            return "#"
        return "."

class Board:
    def __init__(self, size, marked_points):
        self.size = size
        self.points = []
        self.marked_points = []
        for point in marked_points:
            if point not in self.marked_points:
                self.marked_points.append(point)
        print(f"There are {len(self.marked_points)} marked points.")
        #for j in range(size):
        #    print(f"Processing row {j} of {size}")
        #    for i in range(size):
        #        pt = Point(x=j,y=i)
        #        if pt in marked_points:
        #            pt.marked = True
        #            self.points.append(pt)
        #            #self.points.append(Point(x=i,y=j, marked=True))
        #        else:
        #            self.points.append(pt)

    def update(self, size, marked_points):
        self.size = size
        self.points = []
        self.marked_points = []
        for point in marked_points:
            if point not in self.marked_points:
                self.marked_points.append(point)
        print(f"There are {len(self.marked_points)} marked points.")
        #for j in range(size):
        #    print(f"Processing row {j} of {size}")
        #    for i in range(size):
        #        pt = Point(x=j,y=i)
        #        if pt in marked_points:
        #            pt.marked = True
        #            self.points.append(pt)
        #        else:
        #            #self.points.append(pt)

    def get_point(self, x, y):
        for point in self.marked_points:
            if point.x == x and point.y == y:
                return point
        else:
            #return Point(x=x, y=y, marked=False)
            return None

    @property
    def dot_count(self):
        return len([point for point in self.marked_points])

    def apply_fold(self, axis, pivot):
        if axis == 'y':
            new_marked_points = []
            for point in self.marked_points:
                if point.x < pivot:
                    #print(f"Point [{point.x},{point.y}] stays where it was.")
                    new_marked_points.append(Point(x=point.x, y=point.y, marked=True))
                elif point.x > pivot:
                    #print(f"Projecting point [{point.x},{point.y}] to [{pivot-(point.x-pivot)},{point.y}].")
                    new_marked_points.append(Point(x=pivot-(point.x-pivot), y=point.y, marked=True))
        elif axis == 'x':
            new_marked_points = []
            for point in self.marked_points:
                if point.y < pivot:
                    #print(f"Point [{point.x},{point.y}] stays where it was.")
                    new_marked_points.append(Point(x=point.x, y=point.y, marked=True))
                elif point.y > pivot:
                    #print(f"Projecting point [{point.x},{point.y}] to [{point.x},{pivot-(point.y-pivot)}].")
                    new_marked_points.append(Point(x=point.x, y=pivot-(point.y-pivot), marked=True))
        size = 0
        for point in new_marked_points:
            if point.x > size:
                size = point.x
            if point.y > size:
                size = point.y
        for point in self.marked_points:
            if point.x > size:
                size = point.x
            if point.y > size:
                size = point.y
        self.update(size=size, marked_points=new_marked_points)
            

    def display(self):
        print("Printing row.")
        display_string = ""
        for i in range(self.size+2):
            print(f"Printing row {i} of {self.size+2}")
            display_string += "\n"
            for j in range(self.size+2):
                #display_string += str(self.get_point(x=i, y=j).display())
                pt = self.get_point(x=i,y=j)
                if pt:
                    display_string += pt.display()
                else:
                    display_string += "."
        return display_string

        
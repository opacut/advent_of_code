from queue import Queue

class Point:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height

    def display(self):
        return f"[{self.x},{self.y}]({self.height})"

    def __eq__(self, other):
        if (isinstance(other, Point)):
            return self.x == other.x and self.y == other.y and self.height == other.height


class HeightMap:
    def __init__(self, data):
        self.points = []
        #for row in data:
        for i in range(len(data)):
            #self.areas.append([])
            for j in range(len(data[i])):
                self.points.append(Point(x=i,y=j,height=data[i][j]))
            #for c in data[i]:
                #self.areas[i].append(int(c))
    
    def xs(self, x):
        pts = []
        for point in self.points:
            if point.x == x:
                pts.append(point)
        return pts

    def ys(self, y):
        pts = []
        for point in self.points:
            if point.y == y:
                pts.append(point)
        return pts

    def get_point_by_coords(self, x, y):
        for point in self.points:
            if point.x == x and point.y == y:
                return point

    def get_neighbors(self, point):
        pts = []
        pts.append(self.get_point_by_coords(x=point.x, y=point.y+1))
        pts.append(self.get_point_by_coords(x=point.x, y=point.y-1))
        pts.append(self.get_point_by_coords(x=point.x-1, y=point.y))
        pts.append(self.get_point_by_coords(x=point.x+1, y=point.y))
        return [pt for pt in pts if pt]

    def get_low_points(self):
        pts = []
        for point in self.points:
            #print(f"\nProcessing point on position x: {point.x} and y: {point.y}. It's height is {point.height}")
            for neighbor in self.get_neighbors(point=point):
                #print(f"Processing it's neighbor on position x: {neighbor.x}")
                if not neighbor:
                    #print("Neighbor non-existent.")
                    continue
                #print(f"Processing it's neighbor on position x: {neighbor.x} and y: {neighbor.y} with height {neighbor.height}.")
                if neighbor.height <= point.height:
                    #print(f"It has a smaller neighbor. Skipping...")
                    break
            else:
                #print(f"Adding the point to list.")
                pts.append(point)
        return pts
    
    def get_low_points_values(self):
        return [p.height for p in self.get_low_points()]

    def get_risk_level(self):
        return sum([int(v)+1 for v in self.get_low_points_values()])


    def display(self):
        #print("\n")
        ret_str = "\n"
        for row_index in range(len(self.xs(x=0))):
            for point in self.xs(x=row_index):
                #print(" "+str(point.height))
                ret_str += " "+str(point.height)
            #print("")
            ret_str += "\n"
        print(ret_str)

    def get_basin_points(self, low_point):
        basin_points = []
        q = Queue()
        q.put(low_point)
        #for 
        #print(f"Current basin points: {[pt.display() for pt in basin_points]}")
        #print(f"Beginning basin definition for point {low_point.display()}:")
        while not q.empty():
            #print(f"Current basin points: {[pt.display() for pt in basin_points]}")
            point = q.get(block = False)
            #print(f"Processing point {point.display()}:")
            if int(point.height) == 9:
                #print(f"Point is boundary. Skipping...")
                continue
            if point not in basin_points:
                #print(f"Point not processed yet.")
                basin_points.append(point)
                #print(f"Found neighbors: {[pt.display() for pt in self.get_neighbors(point=point)]}")
                for neighbor in self.get_neighbors(point=point):
                    #print(f"Processing neighbor {neighbor.display()}")
                    if int(neighbor.height) == 9:
                        #print(f"Neighbor {neighbor.display()} is boundary. Skipping...")
                        continue
                    if neighbor not in basin_points:
                        #print(f"Adding neighbor {neighbor.display()} to queue.")
                        q.put(neighbor)
                        #basin_points.append(neighbor)
                    else:
                        #print(f"Neighbor {neighbor.display()} already processed. moving on.")
                        continue
                #basin_points.append(point)
            #else:
                #print(f"Point {point.display()} already processed. Moving on.")
        return basin_points
                

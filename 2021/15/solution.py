import pdb
from classes import Node

f = open("2021/15/3x3.txt", "r")
lines = f.read().split("\n")
print(f"There are {len(lines)} lines.")
#print(f"{lines}")

points = [[int(pt) for pt in line] for line in lines]
#print(f"Points: {points}")

size = len(points)
initial_point = (0,0)



path = []


def add_neighbors(pt):
    path1 = [(0,0), (0,1), (0,2), (1,2), (2,2)]
    path2 = [(0,0), (0,1), (1,1), (1,2), (2,2)]
    path3 = [(0,0), (0,1), (1,1), (2,1), (2,2)]
    path4 = [(0,0), (1,0), (2,0), (2,1), (2,2)]
    path5 = [(0,0), (1,0), (1,1), (1,2), (2,2)]
    path6 = [(0,0), (1,0), (1,1), (2,1), (2,2)]
    

def generate_path(graph):
    new_path = []
    #print(f"({graph[0][0]},{graph[0][1]})")
    new_path.append(graph[0])
    for i in graph[1:]:
        #new_path.append(graph[0])
        if i.__class__ is list:
            new_path.append(generate_path(i))
            #return new_path
            #return generate_path(i)
        else:
            #new_path.append(i)
            return i
    return new_path

def generate_all_possible_paths(graph):
    #all_paths = []
    return generate_path(graph)


#all_possible_paths = generate_all_possible_paths(initial_point)
#print(f"{generate_all_possible_paths(initial_point)}")
#print(f"Add neighbors: {generate_binary_graph(initial_point)}")
#graph = generate_binary_graph(initial_point)
#paths = generate_all_possible_paths(graph)
#print(f"path: {path}")
#print(f"{[points[pt[0]][pt[1]] for pt in path]}")


# dostanes 3 elementy
# prvy pridaj do cesty
# vytvor novu cestu
#all_paths = []
#def try_adding_paths(graph, path):
#    path_being_processed = path
#    for i in graph:
#        if i.__class__ is tuple:
#            path_being_processed.append(i)
#        else:
#            path_being_processed.append(try_adding_paths(i, path_being_processed))
#    return path_being_processed
#
##print(try_adding_paths(graph, []))
#a = try_adding_paths(graph, [])
#pdb.set_trace()

### THIS IS WORKING, HOW WE MAKE A GRAPH ###
#def generate_binary_graph(pt):
#    path.append((pt[0], pt[1]))
#    if pt[0] == size-1 and pt[1] == size-1:
#        return (pt[0], pt[1])
#        pass
#    elif pt[0] == size-1:
#        return [(pt[0], pt[1]), generate_binary_graph((pt[0], pt[1]+1))]
#    elif pt[1] == size-1:
#        return [(pt[0], pt[1]), generate_binary_graph((pt[0]+1, pt[1]))]
#    else: # the only bifurcation
#        return [(pt[0], pt[1]), generate_binary_graph((pt[0], pt[1]+1)), generate_binary_graph((pt[0]+1, pt[1]))]
### THIS IS WORKING, HOW WE MAKE A GRAPH ###

def generate_binary_graph(pt):
    path.append((pt[0], pt[1]))
    if pt[0] == size-1 and pt[1] == size-1:
        return (pt[0], pt[1])
        pass
    elif pt[0] == size-1:
        return [(pt[0], pt[1]), generate_binary_graph((pt[0], pt[1]+1))]
    elif pt[1] == size-1:
        return [(pt[0], pt[1]), generate_binary_graph((pt[0]+1, pt[1]))]
    else: # the only bifurcation
        return [(pt[0], pt[1]), generate_binary_graph((pt[0], pt[1]+1)), generate_binary_graph((pt[0]+1, pt[1]))]

def print_array(ints, ln):
    for i in ints[0:ln]:
        print(i," ",end="")
    print()

def print_paths_rec(root, path, path_length):
    if root is None:
        return
    if len(path) > path_length:
        path[path_length] = root.data
    else:
        path.append(root.data)
    
    path_length += 1

    if root.left is None and root.right is None:
        print_array(path, path_length)
    else:
        print_paths_rec(root.left, path, path_length)
        print_paths_rec(root.right, path, path_length)


def print_paths(root):
    path = []
    print_paths_rec(root, path, 0)

graph = []
def build_graph(root):
    for i in range(size):
        for j in range(size):
            #if i < size-1:
            graph.append(Node(data=points[i][j]))
            print(points[i][j])
#    for row in points:
#       for val in row:

#print(do_NOT_generate_binary_graph(initial_point))
#print(path)
p = generate_binary_graph(pt=initial_point)
build_graph(initial_point)
#print(graph)
print(points)
#pdb.set_trace()
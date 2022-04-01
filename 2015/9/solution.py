import re
from classes import Vertex, Edge, Graph


f = open("2015/9/example.txt", "r")
lines = f.read().split("\n")
print(lines)
print(f"There are {len(lines)} lines.")

all_vertices = []
all_edges = []
for line in lines:
    x = re.match(r"(.+) to (.+) = ([0-9]+)", line)
    if x:
        print(f"Found edge from {x.groups()[0]} to {x.groups()[1]} with weight {x.groups()[2]}.")
        if x.groups()[0] not in [y.name for y in all_vertices]:
            all_vertices.append(Vertex(name=x.groups()[0], index=len(all_vertices)))
        if x.groups()[1] not in [y.name for y in all_vertices]:
            all_vertices.append(Vertex(name=x.groups()[1], index=len(all_vertices)))
        v1 = [vertex for vertex in all_vertices if vertex.name == x.groups()[0]][0]
        v2 = [vertex for vertex in all_vertices if vertex.name == x.groups()[1]][0]
        all_edges.append(Edge(start_vertex=v1, end_vertex=v2, weight=x.groups()[2]))
g = Graph(vertices=all_vertices, edges=all_edges)
print(f"All vertices: {[v.name for v in all_vertices]}")
print(f"All edges: {[edge.display() for edge in all_edges]}")
print(f"Adjacency matrix: {g.adjacency_list}")
par, dist = g.bfs(starting_vertex_name="London")
print(f"Parent: {par}")
print(f"dist: {dist}")
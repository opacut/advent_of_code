from re import S
from collections import deque


class Vertex:
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def __eq__(self, other):
        return self.name == other.name

    #def display(self)


class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight
    
    def __eq__(self, other):
        return (self.start_vertex == other.start_vortex and self.end_vertex == other.end_vertex) or (self.start_vertex == other.end_vertex and self.end_vertex == other.start_vertex)

    def display(self):
        return f"{self.start_vertex.name} to {self.end_vertex.name} = {self.weight}"


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def get_routes(self):
        pass

    def get_edge_weight(self, v1_name, v2_name):
        for e in self.edges:
            if e.start_vertex.name == v1_name and e.end_vertex.name == v2_name:
                return int(e.weight)
            if e.start_vertex.name == v2_name and e.end_vertex.name == v1_name:
                return int(e.weight)


    def bfs(self, starting_vertex_name):
        adj = self.adjacency_list
        parent = {starting_vertex_name: None}
        distances_from_start = {starting_vertex_name: 0}

        queue = deque()
        queue.append(starting_vertex_name)

        while queue:
            u = queue.popleft()
            print(f"u: {u}")
            for n in adj[u]:
                print(f"n: {n}")
                if n not in distances_from_start:
                    parent[n] = u
                    distances_from_start[n] = distances_from_start[u] + self.get_edge_weight(v1_name=n, v2_name=u)
                    #print(f"d[n]: {distances_from_start[n]}, d[u]: {distances_from_start[u]}")
                    queue.append(n)
        return parent, distances_from_start

    #def dfs(self, current_vertex, visited):
    #    visited.append(current_vertex)
    #    for vertex in self.get_vertex:
    #        if vertex not in visited:


    @property
    def adjacency_list(self):
        l = {}
        for vertex in self.vertices:
            l[vertex.name] = self.get_neighbors(vertex_name=vertex.name)
        return l

    def get_neighbors(self, vertex_name):
        neighbors = []
        for edge in self.edges:
            if edge.start_vertex.name == vertex_name:
                neighbors.append(edge.end_vertex.name)
            elif edge.end_vertex.name == vertex_name:
                neighbors.append(edge.start_vertex.name)
        return neighbors

    
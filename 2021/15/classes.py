class Node:
    def __init__(self, data, left=None, right=None):
        self.l = data
        self.left = left
        self.right = right

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

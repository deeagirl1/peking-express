# a class to connect the vertices, define the price
# between two vertices and set the critical of the graph
class Vertex:

    def __init__(self, index, critical=False):
        self.index = index
        self.critical = critical
        self.neighbours = {}

    # add neighbour to the vertex and define the price between them
    def add_neighbour(self, vertex, weight=0):
        self.neighbours[vertex] = weight

    # get all neighbours of the vertex
    def get_neighbours(self):
        return list(self.neighbours.keys())

    # get the distances between the vertex and its neighbours
    def weight(self, vertex):
        return self.neighbours[vertex]

    def set_critical(self, critical):
        self.critical = critical

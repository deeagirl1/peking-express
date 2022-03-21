class Vertex:

    def __init__(self, index, critical=False):
        self.index = index
        self.critical = critical
        self.neighbours = {}

    def add_neighbour(self, vertex, weight=0):
        self.neighbours[vertex] = weight

    def get_neighbours(self):
        return list(self.neighbours.keys())

    def weight(self, vertex):
        return self.neighbours[vertex]

    def set_critical(self, critical):
        self.critical = critical

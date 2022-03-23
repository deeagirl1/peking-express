from Vertex import Vertex


class Graph:

    def __init__(self):
        self.vertices = {}

    # function to add the vertex to the graph
    def add_vertex(self, node):
        self.num_vertices += 1
        self.vertices[node] = Vertex(node)

    # For each vertex, we need to add edges to the graph
    def add_edge(self, source, target, price):

        if source not in self.vertices:
            self.add_vertex(source)

        if target not in self.vertices:
            self.add_vertex(target)

        # We add the neighbours for u and v
        self.vertices[source].add_neighbour(target, price)
        self.vertices[target].add_neighbour(source, price)

    def get_vertices(self):
        return self.vertices

    def get_vertex(self, vertex):
        return self.vertices[vertex] if vertex in self.vertices else None

    def get_neighbours(self):
        return list(self.get_vertices())

    # Keep updating the critical vertex
    def update_critical(self, vertex, critical=True):
        self.get_vertex(vertex)
        Vertex.set_critical(self, critical)

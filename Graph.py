from Vertex import Vertex


class Graph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    # For each vertex, we need to add edges to the graph
    def add_edge(self, vertex1, vertex2, weight):

        # We add vertex u.
        if vertex1 not in self.vertices:
            self.vertices[vertex1] = Vertex(vertex1)

        # We add vertex v.
        if vertex2 not in self.vertices:
            self.vertices[vertex2] = Vertex(vertex2)

        # We add the neighbours for u and v
        self.vertices[vertex1].add_neighbour(vertex2, weight)
        self.vertices[vertex2].add_neighbour(vertex1, weight)

        self.num_vertices += 2

    def get_vertices(self):
        return self.vertices

    def get_vertex(self, vertex):
        return self.vertices[vertex] if vertex in self.vertices else None

    def get_neighbours(self):
        return list(self.get_vertices())

    # If we have any vertices which are critical, then add them to the critical_vertices list.
    def get_critical_vertices(self):
        critical_vertices = []
        for u in self.vertices:
            if self.vertices[u].critical:
                critical_vertices += [self.vertices[u]]

        return critical_vertices

    # Keep updating the critical vertex
    def update_critical(self, vertex, critical=True):
        self.get_vertex(vertex)
        Vertex.set_critical(self, critical)

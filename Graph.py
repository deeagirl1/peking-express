from Vertex import Vertex


class Graph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    # For each vertex, we need to add edges to the graph
    def add_edge(self, source, target, price):

        # We add vertex u.
        if source not in self.vertices:
            self.vertices[source] = Vertex(source)

        # We add vertex v.
        if target not in self.vertices:
            self.vertices[target] = Vertex(target)

        # We add the neighbours for u and v
        self.vertices[source].add_neighbour(target, price)
        self.vertices[target].add_neighbour(source, price)

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

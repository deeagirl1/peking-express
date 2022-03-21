from Vertex import Vertex


class Graph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_edge(self, u, v, w):

        # We add vertex u.
        if u not in self.vertices:
            self.vertices[u] = Vertex(u)

        # We add vertex v.
        if v not in self.vertices:
            self.vertices[v] = Vertex(v)

        self.vertices[u].add_neighbour(v, w)
        self.vertices[v].add_neighbour(u, w)

        self.num_vertices += 2

    def get_vertices(self):
        return self.vertices

    def get_vertex(self, u):
        return self.vertices[u] if u in self.vertices else None

    def get_neighbours(self):
        return list(self.get_vertices())

    def get_critical_vertices(self):
        critical_vertices = []
        for u in self.vertices:
            if self.vertices[u].critical:
                critical_vertices += [self.vertices[u]]

        return critical_vertices

    def update_critical(self, u, critical=True):
        self.get_vertex(u)
        Vertex.set_critical(self, critical)


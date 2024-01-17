def is_hashable(value):
    try:
        hash(value)
        return True
    except Exception as err:
        raise TypeError(f"Value must be immutable and hashable.\n{err}")


class Vertex:
    def __init__(self, value):
        if is_hashable(value):
            self.value = value
        self.neighbors = {}

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def add_update_neighbor(self, vertex, weight=0):
        """
        Input vertex instance of the neighbor vertex and weight of the edge, default 0:
        Output nothing, changes inplace.
        """
        if isinstance(vertex, Vertex) and isinstance(weight, int):
            self.neighbors[vertex] = weight
        else:
            raise TypeError("Must vertex as Vertex Instance and weight as integer.")


class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, value0, value1, weight=0):
        """
        """
        if value0 not in self.graph: raise ValueError(f"{value0} not found in graph.")
        if value1 not in self.graph: raise ValueError(f"{value1} not found in graph.")
        vertex0 = self.graph[value0]
        vertex1 = self.graph[value1]
        vertex0.add_update_neighbor(vertex1, weight)
        vertex1.add_update_neighbor(vertex0, weight)

    def add_vertex(self, value):
        """"""
        if is_hashable(value):
            if value in self.graph:
                raise ValueError(f"Vertex already exists in graph. {value}")
            self.graph[value] = Vertex(value)

    def get_vertices(self):
        """"""
        return [vertex for vertex in self.graph.values()]

    def get_neighbors(self, value):
        """"""
        if is_hashable(value):
            if value not in self.graph:
                raise ValueError(f"Vertex doesn't exists in graph. {value}")
            return self.graph[value].neighbors

    def size(self):
        """"""
        return len(self.graph)


# if __name__=="__main__":
#     graph0 = Graph()
#     graph0.add_vertex("a")
#     graph0.add_vertex("b")
#     graph0.add_vertex("c")
#     graph0.add_edge("a","b",1)
#     graph0.add_edge("b", "c", 1)
#     graph0.add_edge("c","a")
#     print(graph0.size())
#     print(graph0.get_neighbors("a"))
#     print(graph0.get_vertices())

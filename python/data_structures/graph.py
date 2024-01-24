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
            self.neighbors[vertex.value] = {"neighbor": vertex, "weight": weight}
        else:
            raise TypeError("Must vertex as Vertex Instance and weight as integer.")


class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, value0, value1, weight=0):
        """
        """
        if isinstance(value0, Vertex):
            value0 = value0.value
        if isinstance(value1, Vertex):
            value1 = value1.value
        if value0 not in self.graph: raise KeyError(f"{value0} not found in graph.")
        if value1 not in self.graph: raise KeyError(f"{value1} not found in graph.")
        vertex0 = self.graph[value0]
        vertex1 = self.graph[value1]
        vertex0.add_update_neighbor(vertex1, weight)
        vertex1.add_update_neighbor(vertex0, weight)

    def add_vertex(self, value)->Vertex:
        """"""
        if isinstance(value, Vertex):
            value = value.value
        if is_hashable(value):
            if value in self.graph:
                raise ValueError(f"Vertex already exists in graph. {value}")
            self.graph[value] = Vertex(value)
            return self.graph[value]

    def contains(self,value):
        if isinstance(value, Vertex):
            value = value.value
        return value in self.graph

    def get_vertices(self):
        """"""
        return [vertex for vertex in self.graph.values()]

    def get_neighbors(self, value):
        """"""
        if isinstance(value, Vertex):
            value = value.value
        if is_hashable(value):
            if value not in self.graph:
                raise KeyError(f"Vertex doesn't exists in graph. {value}")
            return self.graph[value].neighbors

    def depth_first_search(self, root: Vertex) -> list:
        if not root or not isinstance(root, Vertex):
            raise TypeError("Root must be a vertex instance.")
        if not self.graph or not self.contains(root):
            return []
        curr = self.graph.get(root.value)
        visited = set()
        collection = list()

        def helper(node):
            nonlocal visited
            nonlocal collection
            if node.value in visited:
                return
            collection.append(node.value)
            visited.add(node.value)
            neighbors = [item.get("neighbor") for item in node.neighbors.values()]
            for neighbor in neighbors:
                helper(neighbor)
            return

        helper(curr)
        return collection

    def size(self):
        """"""
        return len(self.graph)



# if __name__=="__main__":
#     graph0 = Graph()
#     a = graph0.add_vertex("a")
#     b = graph0.add_vertex("b")
#     c = graph0.add_vertex("c")
#     d = graph0.add_vertex("d")
#     graph0.add_edge("a","b",1)
#     graph0.add_edge("b", "c", 1)
#     graph0.add_edge("c","a")
#     graph0.add_edge("a","d", 1)
    # print(graph0.size())
    # print(graph0.get_neighbors("a"))
    # print(graph0.get_vertices())
    # print(graph0.depth_first_search(d))
    # print(graph0.contains(a))
    # print(a.neighbors)

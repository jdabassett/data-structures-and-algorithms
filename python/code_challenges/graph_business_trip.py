from data_structures.graph import Graph


def direct_flights(graph: Graph, itinerary):

    if not isinstance(graph, Graph) or not isinstance(itinerary,list):
        raise TypeError("graph and itinerary parameters must be type Graph and list respectively.")
    if 0 == len(itinerary) or not all([True if isinstance(string,str) else False for string in itinerary]) :
        raise ValueError("itinerary parameter must be a list containing strings.")


    if all([graph.contains(place) for place in itinerary]):
        neighbors = dict()
        neighbors[itinerary[0]] = {"neighbor": itinerary[0], "weight": 0}
        cumul = 0
        visited = set()

        for place in itinerary:
            if place not in neighbors and place not in visited:
                return False, 0
            cumul += neighbors.get(place).get("weight")
            neighbors = graph.get_neighbors(place)
            visited.add(place)

        return True, cumul

    return False, 0

import pytest
from data_structures.graph import Graph, Vertex


def test_exists():
    assert Graph


# @pytest.mark.skip("TODO")
def test_add_vertex():
    graph = Graph()
    expected = "spam"
    graph.add_vertex(expected)
    assert graph.graph[expected].value == expected
    assert graph.graph[expected].neighbors == {}


# @pytest.mark.skip("TODO")
def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_size():
    graph = Graph()
    graph.add_vertex("spam")
    graph.add_vertex("ham")
    expected = 2
    actual = graph.size()
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_add_edge():
    graph = Graph()
    a = Vertex("a")
    b = Vertex("b")
    graph.add_vertex(a)
    graph.add_vertex("b")
    graph.add_edge("a", b, 5)
    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 1
    assert neighbors[b.value]['weight'] == 5
    neighbors = graph.get_neighbors("a")
    assert len(neighbors) == 1
    assert neighbors[b.value]['weight'] == 5


# @pytest.mark.skip("TODO")
def test_bouquet():
    graph = Graph()
    a = graph.add_vertex("a")
    graph.add_edge(a, a, 10)
    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 1
    assert neighbors[a.value]["neighbor"] == a
    assert neighbors[a.value]["weight"] == 10


# @pytest.mark.skip("TODO")
def test_add_edge_interloper_start():
    graph = Graph()
    start = Vertex("start")
    end = graph.add_vertex("end")
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# @pytest.mark.skip("TODO")
def test_add_edge_interloper_end():
    graph = Graph()
    end = Vertex("end")
    start = graph.add_vertex("start")
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# @pytest.mark.skip("TODO")
def test_get_nodes():
    graph = Graph()
    b = graph.add_vertex("b")
    a = graph.add_vertex("a")
    c = Vertex("c")
    expected = 2
    actual = len(graph.get_vertices())
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_get_neighbors():
    graph = Graph()
    b = graph.add_vertex("b")
    a = graph.add_vertex("a")
    graph.add_edge(a, b, 44)
    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 1
    neighbor_edge = neighbors[b.value]
    assert neighbor_edge["neighbor"] == b
    assert neighbor_edge["weight"] == 44

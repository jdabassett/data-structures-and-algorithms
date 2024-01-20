import pytest
from data_structures.graph import Graph
from code_challenges.graph_business_trip import direct_flights


# @pytest.mark.skip("TODO")
def test_metroville_pandora(planets):
    names = ["Metroville", "Pandora"]
    assert direct_flights(planets, names) == (True, 82)


# @pytest.mark.skip("TODO")
def test_metroville_monstropolis(planets):
    names = ["Metroville", "New Monstropolis"]
    assert direct_flights(planets, names) == (True, 105)


# @pytest.mark.skip("TODO")
def test_arendelle_monstropolis_naboo(planets):
    names = ["Arendelle", "New Monstropolis", "Naboo"]
    assert direct_flights(planets, names) == (True, 115)


# @pytest.mark.skip("TODO")
def test_naboo_pandora(planets):
    names = ["Naboo", "Pandora"]
    assert direct_flights(planets, names) == (False, 0)


# @pytest.mark.skip("TODO")
def test_narnia_arendelle_naboo(planets):
    names = ["Narnia", "Arendelle", "Naboo"]
    assert direct_flights(planets, names) == (False, 0)

# @pytest.mark.skip("TODO")
def test_all_positive(planets):
    names = ["Pandora", "Metroville","Narnia","Naboo","New Monstropolis","Arendelle"]
    assert direct_flights(planets, names) == (True, 484)


# @pytest.mark.skip("TODO")
def test_duplicated_caught(planets):
    names = ["Naboo","Pandora", "Metroville","Narnia","Naboo","New Monstropolis","Arendelle"]
    assert direct_flights(planets, names) == (False,0)

# @pytest.mark.skip("TODO")
def test_graph_type_error():
    with pytest.raises(TypeError):
        direct_flights({},[])

# @pytest.mark.skip("TODO")
def test_itinerary_type_error():
    with pytest.raises(TypeError):
        direct_flights(Graph(),{})

# @pytest.mark.skip("TODO")
def test_itinerary_value_error():
    with pytest.raises(ValueError):
        direct_flights(Graph(),[])
    with pytest.raises(ValueError):
        direct_flights(Graph(),[1,2,3])



@pytest.fixture
def planets():
    graph = Graph()

    metroville = graph.add_vertex("Metroville")
    pandora = graph.add_vertex("Pandora")
    arendelle = graph.add_vertex("Arendelle")
    new_monstropolis = graph.add_vertex("New Monstropolis")
    naboo = graph.add_vertex("Naboo")
    narnia = graph.add_vertex("Narnia")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, pandora, 150)

    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(metroville, pandora, 82)

    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(arendelle, metroville, 99)

    graph.add_edge(new_monstropolis, arendelle, 42)
    graph.add_edge(arendelle, new_monstropolis, 42)

    graph.add_edge(new_monstropolis, metroville, 105)
    graph.add_edge(metroville, new_monstropolis, 105)

    graph.add_edge(new_monstropolis, naboo, 73)
    graph.add_edge(naboo, new_monstropolis, 73)

    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, metroville, 26)

    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(narnia, metroville, 37)

    graph.add_edge(narnia, naboo, 250)
    graph.add_edge(naboo, narnia, 250)

    return graph

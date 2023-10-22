import pytest
from code_challenges.stack_queue_animal_shelter import AnimalShelter, Dog, Cat
from data_structures.invalid_operation_error import InvalidOperationError


class Turtle:
    species='turtle'
    def __init__(self,name:str=None):
        self.name=name


# @pytest.mark.skip("TODO")
def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual


# @pytest.mark.skip()
def test_enqueue_wrong_animal_class():
    shelter = AnimalShelter()
    turtle = Turtle("Harvey")
    with pytest.raises(TypeError):
        shelter.enqueue(turtle)

# @pytest.mark.skip()
def test_dequeue_from_empty_queue():
    shelter = AnimalShelter()
    with pytest.raises(InvalidOperationError):
        shelter.dequeue()


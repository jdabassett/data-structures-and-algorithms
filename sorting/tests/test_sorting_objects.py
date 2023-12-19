import pytest
from sorting_objects.test import expected1, expected2
from sorting_objects.movies import movies
from sorting_objects.sorting_objects import sort_by_title, sort_by_year

# movies = [
#   {
#     "title": "The Intouchables",
#     "year": 2011,
#
#     "genres": ["Biography", "Comedy", "Drama"],
#   },
#   {
#     "title": "Valkyrie",
#     "year": 2008,
#     "genres": ["Drama", "History", "Thriller"],
#   },
#   {
#     "title": "Ratatouille",
#     "year": 2007,
#     "genres": ["Animation", "Comedy", "Family"],
#   },
#   {
#     "title": "Stardust",
#     "year": 2007,
#     "genres": ["Adventure", "Family", "Fantasy"],
#   },
#   {
#     "title": "City of God",
#     "year": 2002,
#
#     "genres": ["Crime", "Drama"],
#   },
#   {
#     "title": "Memento",
#     "year": 2000,
#
#     "genres": ["Mystery", "Thriller"],
#   },
#   {
#     "title": "The Shawshank Redemption",
#     "year": 1994,
#     "genres": ["Crime", "Drama"],
#   },
#   {
#     "title": "Beetlejuice",
#     "year": 1988,
#     "genres": ["Comedy", "Fantasy"],
#   },
#   {
#     "title": "Crocodile Dundee",
#     "year": 1986,
#
#     "genres": ["Adventure", "Comedy"],
#   },
#   {
#     "title": "The Cotton Club",
#     "year": 1984,
#     "genres": ["Crime", "Drama", "Music"],
#   },
# ]

# @pytest.mark.skip("TODO")


# @pytest.mark.skip("TODO)
def test_sort_by_year():
    actual_dict = sort_by_year(movies)
    actual = [item.get("title") for item in actual_dict]
    assert actual == expected1

# @pytest.mark.skip("TODO)
def test_sort_by_title():
    actual_dict = sort_by_title(movies)
    actual = [item.get("title") for item in actual_dict]
    assert actual == expected2


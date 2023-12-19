from sorting_objects.movies import movies


def sort_by_year(list_movies: list[dict]) -> list[dict]:
    """
    Input a list of dictionaries with one key of 'year'.
    Output a list of dictionaries sorted in descending order based on the year key.
    :param list_movies: list[dict]
    :return: list[dict]
    """
    return sorted(movies, key=lambda x: int(x.get('year')), reverse=True)





def sort_by_title(list_movies: list[dict]) -> list[dict]:
    """
    Input a list of dictionaries with one key of 'year'.
    Output a list of dictionaries sorted in descending order based on the year key.
    :param list_movies: list[dict]
    :return: list[dict]
    """

    def helper(movie):
        omitted = ["A ", "An ", "The "]
        title = movie.get('title')
        for i in omitted:
            if title.startswith(i):
                return title[len(i):]
        return title
    
    return sorted(movies, key= lambda x: helper(x))


# if __name__ == "__main__":
#     print(sort_by_year(movies))
#     print()
#     print(sort_by_title(movies))

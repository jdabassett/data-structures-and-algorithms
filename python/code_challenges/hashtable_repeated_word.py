from data_structures.hashtable import Hashtable
from re import split
import string

def remove_punctuation_spaces_lower(word: str = "") -> str:
    """
    Input word as string.
    Output is the string without punctuation, spaces, and converted to lowercase.
    """
    if isinstance(word,str):
        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        return word.translate(translator).strip().lower()
    else:
        raise TypeError("Input must be a string.")


def first_repeated_word(input_str: str = "") -> str or None:
    """
    Input string of sentence.
    Output first repeated word or None if there isn't any.
    """
    try:
        if isinstance(input_str, str):
            if len(input_str) > 0:
                counter = Hashtable()
                input_list = split(r"[\n\s]+", input_str)
                for word in input_list:
                    word = remove_punctuation_spaces_lower(word)
                    if counter.has(word):
                        return word
                    else:
                        counter.set(word,1)
            return None
        else:
            raise TypeError('Input must be a string.')
    except Exception as error:
        raise Exception(f"{error}")


def word_count(input_str: str = "") -> str or None:
    """
    Input string of sentence.
    Output Hashtable containing the word count of input.
    """
    if isinstance(input_str, str):
        counter = Hashtable()
        if len(input_str) > 0:
            input_list = split(r"[\n\s]+", input_str)
            for word in input_list:
                word = remove_punctuation_spaces_lower(word)
                counter.update(word,1)
        return counter
    else:
        raise TypeError('Input must be a string.')


def word_sort(input_str: str = "") -> list[str]:
    """
    Input string of sentence.
    Output list of words sorted in descending order of count.
    """
    counter_dict = word_count(input_str)
    counter_list = [pair for pair in counter_dict.convert_to_list()]
    counter_sorted = sorted(counter_list, key=lambda x: x[-1], reverse=True)
    return [pair[0] for pair in counter_sorted]


if __name__=="__main__":
    print(first_repeated_word("a b C c"))
    print(first_repeated_word())
    print(word_count("a b c c c"))
    print(word_sort("a a A a A b b c c c"))


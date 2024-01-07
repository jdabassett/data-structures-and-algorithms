from data_structures.hashtable import Hashtable


def left_join(fir_dict: dict, sec_dict: dict) -> dict:
    """
    Input two dictionaries, first with key value strings that are synonyms and the second parameter with key value strings that are antonyms.
    Output, left joined dictionary with key string and value dictionary of synonym and antonym.
    """
    if not isinstance(fir_dict, dict) or not isinstance(sec_dict, dict):
        raise TypeError("Input parameters must both be type dictionary")
    ret_dict = {}
    for key, value in fir_dict.items():
        if key in sec_dict:
            ret_dict[key] = {"synonym":value,"antonym":sec_dict.get(key)}
        else:
            ret_dict[key] = {"synonym": value, "antonym": None}
    return ret_dict



# if __name__ == "__main__":
#     synonyms = {
#         "diligent": "employed",
#         "fond": "enamored",
#         "guide": "usher",
#         "outfit": "garb",
#         "wrath": "anger",
#     }
#     antonyms = {
#         "diligent": "idle",
#         "fond": "averse",
#         "guide": "follow",
#         "flow": "jam",
#         "wrath": "delight",
#     }
#     print(left_join(synonyms, antonyms))
#
#     left_join({},{})

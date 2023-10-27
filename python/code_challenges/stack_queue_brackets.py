from data_structures.queue import Queue


def multi_bracket_validation(str_par:str)->bool:
    que_cur = Queue()
    que_sqr = Queue()
    que_par = Queue()

    for i in str_par:
        if i == "{":
            que_cur.enqueue("{")
        elif i == "[":
            que_sqr.enqueue('[')
        elif i == "(":
            que_par.enqueue('(')
        elif i == "}":
            if que_cur.is_empty():
                return False
            que_cur.dequeue()
        elif i == "]":
            if que_sqr.is_empty():
                return False
            que_sqr.dequeue()
        elif i == ")":
            if que_par.is_empty():
                return False
            que_par.dequeue()

    return que_par.is_empty() and que_sqr.is_empty() and que_cur.is_empty()

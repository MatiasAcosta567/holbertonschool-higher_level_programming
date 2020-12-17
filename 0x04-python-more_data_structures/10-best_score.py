#!/usr/bin/python3
def best_score(a_dictionary):
    maximo = 0
    llave = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for key, value in a_dictionary.items():
        if value > maximo:
            llave = key
            maximo = value
    return llave

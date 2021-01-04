#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
       return fct(args[0],args[1])
    except Exception as ex:
        message = "Exception: " + str(ex) + "\n"
        sys.stderr.write(message)
        return None

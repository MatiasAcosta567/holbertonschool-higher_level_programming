#!/usr/bin/python3
"""Start link class to table in database"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)

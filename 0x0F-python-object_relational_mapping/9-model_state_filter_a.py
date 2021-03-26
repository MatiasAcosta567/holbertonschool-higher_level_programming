#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == '__main__':
    if (len(argv) == 4):
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, dbname), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        session = Session()
        for state in session.query(State).order_by(State.id).all():
            for letter in state.name:
                if (letter == 'a'):
                    print("{}: {}".format(state.id, state.name))
                    break
        session.close() 
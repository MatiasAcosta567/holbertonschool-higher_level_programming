#!/usr/bin/python3
""" Documentation """
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
        state = session.query(State).filter(State.id == 2).first()
        state.name = "New Mexico"
        session.add(state)
        session.commit()
        session.close()

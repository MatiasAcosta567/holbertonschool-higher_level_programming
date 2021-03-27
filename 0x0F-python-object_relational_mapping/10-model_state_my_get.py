#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == '__main__':
    if (len(argv) == 5):
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        state_param = argv[4]
        flag = 0
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, dbname), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(
            State.name == state_param).first()
        if (state != None):
            print("{}".format(state.id))
        else:
            print("Not found")
        session.close()
        
            
#!/usr/bin/python3
"""a script that lists all `State` objects that contain
the letter `a` from the database `hbtn_0e_6_usa`"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy import func


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], quote_plus(sys.argv[2]), sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(
            State.name.contains(func.binary('A'))).order_by(State.id):
        # if str(state.name).find('a') != -1:
        #     print("{}: {}".format(state.id, state.name))
        print("{}: {}".format(state.id, state.name))

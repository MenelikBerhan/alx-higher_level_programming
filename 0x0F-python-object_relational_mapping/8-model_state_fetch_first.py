#!/usr/bin/python3
"""a script that prints the first `State` object
from the database `hbtn_0e_6_usa`"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], quote_plus(sys.argv[2]), sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State.id, State.name).order_by(State.id).first()
    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

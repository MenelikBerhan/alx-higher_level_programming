#!/usr/bin/python3
"""a script that creates the State “California” with the City
“San Francisco” from the database `hbtn_0e_100_usa`"""


import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], quote_plus(sys.argv[2]), sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='California')
    state.cities.append(City(name='San Francisco'))
    session.add(state)
    session.commit()
    session.close()

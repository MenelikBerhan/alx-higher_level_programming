#!/usr/bin/python3
"""a script that lists all `City` objects
from the database `hbtn_0e_101_usa`"""


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
    for city in session.query(City).order_by(City.id):
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

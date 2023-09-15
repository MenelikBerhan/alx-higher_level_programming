#!/usr/bin/python3
"""Contains the class definition of a State and
an instance Base = declarative_base()"""

# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# engine = create_engine('mysql+mysqldb://root:Mysql%40alx1@localhost
# :3306/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    """Defines a class that represents a relational db table `states`"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

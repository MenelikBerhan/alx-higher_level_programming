#!/usr/bin/python3
"""Contains the class definition of a State and
an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines a class that represents a relational db table `states`"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state', order_by='City.id',
                          cascade="all, delete-orphan")

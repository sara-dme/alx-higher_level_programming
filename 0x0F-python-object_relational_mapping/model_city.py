#!/usr/bin/python3
""" Define a city class and Base class
to work with MySQLAlchemy ORM """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """City class 
    Attributes:
        id  (int): the id
        name (str): name
        __tablename__ (str): table name of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id', nullable=False)
    name = Column(String(128), nullable=False)

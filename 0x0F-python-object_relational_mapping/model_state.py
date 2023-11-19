#!/usr/bin/python3
""" Define a State class and Base class
to work with MySQLAlchemy ORM """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        id  (int): the state id
        name (str): state name
        __tablename__ (str): table name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

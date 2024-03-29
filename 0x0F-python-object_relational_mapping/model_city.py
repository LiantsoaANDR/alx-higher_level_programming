#!/usr/bin/python3
""" Defines the City class """

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class, inherits from Base

    Attributes:
        __tablename__ : the name of our db table
        id : a column of an auto-generated, unique integer,
             can’t be null and is a primary key
        name : a column of a string of 128 characters and can’t be null
        state_id : represents a column of an integer, can’t be null
                   and is a foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

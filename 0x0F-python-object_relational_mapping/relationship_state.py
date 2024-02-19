#!/usr/bin/python3
""" Defines the Statwe class """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class, inherits from Base

    Attributes:
        __tablename__ : the name of our db table
        id : a column of an auto-generated, unique integer,
             can’t be null and is a primary key
        name :  a column of a string with maximum 128 characters
                and can’t be null
        cities : a relationship with the class City
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

#!/usr/bin/python3
"""Import sqlalchemy module."""
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """ State class inherits from Base class."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

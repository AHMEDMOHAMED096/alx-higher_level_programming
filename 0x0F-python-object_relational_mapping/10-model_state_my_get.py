#!/usr/bin/python3
"""Import sqlalchemy module."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def find_state(username, password, database_name, state_name):
    # Create engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == state_name).first()

    if query:
        print(query.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    find_state(username, password, database_name, state_name)

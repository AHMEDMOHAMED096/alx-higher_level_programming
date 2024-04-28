#!/usr/bin/python3
"""Import Modules."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_state_name(username, password, database_name):
    """Create engine to connect to the MySQL server"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    change_state_name(username, password, database_name)

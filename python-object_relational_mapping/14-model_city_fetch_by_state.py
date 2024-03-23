#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


def fetch_all():
    """prints all City objects from the database hbtn_0e_14_usa"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    fetch_all()

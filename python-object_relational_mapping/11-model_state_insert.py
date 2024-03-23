#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_all():
    """adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='Louisiana')
    row = session.add(state)
    session.commit()
    print("{}".format(state.id))
    session.close()


if __name__ == "__main__":
    fetch_all()

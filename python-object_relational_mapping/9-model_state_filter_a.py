#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_all():
    """prints the first State object from the database hbtn_0e_6_usa"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).filter(State.name.contains('a'))
    if rows.count() == 0:
        print("Nothing")
    else:
        for row in rows:
            print("{}: {}".format(row.id, row.name))
    session.close()


if __name__ == "__main__":
    fetch_all()

#!/usr/bin/python3
"""
A script that deletes all `State` objects with a name containing the letter `a`
from the database `hbtn_0e_6_usa`
"""


def main():
    """
    Main function for the script
    """
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()

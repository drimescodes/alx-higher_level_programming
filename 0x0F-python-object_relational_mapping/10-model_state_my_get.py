#!/usr/bin/python3
"""
A script that prints the `State` object with the `name` passed as argument \
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

    state = session.query(State).filter(State.name == argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()

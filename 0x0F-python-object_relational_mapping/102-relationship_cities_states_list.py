#!/usr/bin/python3
"""
A script that lists all `City` objects from the database `hbtn_0e_101_usa`
"""


def main():
    """
    Main function for the script
    """
    from sys import argv
    from relationship_state import Base
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()


if __name__ == "__main__":
    main()

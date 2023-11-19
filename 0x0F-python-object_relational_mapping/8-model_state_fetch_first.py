#!/usr/bin/python3
""" script that prints the first State object
from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Get a state from the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    st = session.query(State).order_by(State.id).first()
    if st is not None:
        print('{}: {}'.format(st.id, st.name))
    else:
        print("Nothing")

    session.close()

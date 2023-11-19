#!/usr/bin/python3
"""script that prints the State object
with the name passed as argument from
the database hbtn_0e_6_usa"""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """Get a state from the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],
                                   sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    st = session.query(State).filter(State.name == argv[4]).first()
    if st is not None:
        print('{}'.format(st.id))
    else:
        print("Not found")

    session.close()

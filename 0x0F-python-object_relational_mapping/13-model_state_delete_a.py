#!/usr/bin/python3
""" that deletes all State objects with a name
 containing the letter a from the database hbtn_0e_6_usa"""


from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """delete state on the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    
    stat = session.query(State).filter(State.name.contains('a'))
    if stat is not None:
        for s in stat:
            session.delete(s)
    session.commit()

    session.close()

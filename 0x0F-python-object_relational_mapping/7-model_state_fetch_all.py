#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker

if __name__ = "__main__":
    engine= create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                          format(sys.argiv[1], sys.argiv[2], sys.argiv[3]),
                          pool_pre_ping= True)

    #Initialize engine
    Base.metadata.create_all(engine)

    #Initialize session
    Session = sessionmaker(bind = engine)
    session= Session()

    #Query
    query= session.query(State).order_by(State.id).all()

    #Print query
    for record in query:
        print("{}: {}".format(record.id, record.name))


    # Close session
    Session.close()

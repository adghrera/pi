'''
Created on May 9, 2015

@author: Aman
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pi import app

engine = create_engine('mysql+mysqlconnector://blog1:blog1@192.168.2.85:3306/blog1', pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import pi.db.models
    
    Base.metadata.create_all(bind=engine)
    

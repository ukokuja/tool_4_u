from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import database_exists, create_database



T4U_BASE = declarative_base()

def init_db():
    engine = create_engine('sqlite:///tool_4_u.db?check_same_thread=False')
    Session = sessionmaker(bind=engine)
    session = Session()
    if not database_exists(engine.url):
        create_database(engine.url)
        T4U_BASE.metadata.create_all(bind=engine, checkfirst=True)
    session.commit()
    return session

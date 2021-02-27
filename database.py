import io
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy_utils import database_exists, create_database

from util.sql import get_sql

T4U_BASE = declarative_base()
def init_db():
    engine = create_engine('sqlite:///tool_4_u.db?check_same_thread=False')
    Session = sessionmaker(bind=engine)
    session = Session()
    if not database_exists(engine.url):
        print("Creating database")
        print("Installing modules")
        create_database(engine.url)
        T4U_BASE.metadata.create_all(bind=engine, checkfirst=True)
        add_fixtures(engine, session)
    session.commit()
    return session


def add_fixtures(engine, session):
    sql = get_sql()
    buf = io.StringIO(sql)
    line = buf.readline()
    while line:
        print(".", end="")
        engine.execute(text(line[:-2]))
        session.commit()
        line = buf.readline()
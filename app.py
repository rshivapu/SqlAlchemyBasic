import sqlalchemy
# print(sqlalchemy.__version__)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


db_engine = create_engine('sqlite:///:memory:', echo = False)
Base = declarative_base()
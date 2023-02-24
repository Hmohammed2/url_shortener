from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

# entry point to the database
engine = create_engine(get_settings().db_url, connect_args={"check_same_thread": False})

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base function returns a class that connects the database engine 
# to the SQLAlchemy functionality of the models.

base = declarative_base()
from sqlalchemy import (Column, Integer, String, PrimaryKeyConstraint)
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///example.db')

Base = declarative_base()

class SuperHero(Base):

    __tablename__ = 'super_heroes'

    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    name = Column(String())
    attribute = Column(String())

    
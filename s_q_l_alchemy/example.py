from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, Date

from datetime import date

engine = create_engine("sqlite:///sqlalchemy_example.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date


# generate database schema
Base.metadata.create_all(engine)
# create a new session
session = Session()

# create some Movie data
bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
furious_7 = Movie("Furious 7", date(2015, 4, 2))
pain_and_gain = Movie("Pain & Gain", date(2013, 8, 23))

# save and commit and close
session.add(bourne_identity)
session.add(furious_7)
session.add(pain_and_gain)

session.commit()
session.close()

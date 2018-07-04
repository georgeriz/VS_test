from base import Session
from movie import Movie

session = Session()

session.query(Movie).filter_by(id=2).delete()
session.commit()
session.close()
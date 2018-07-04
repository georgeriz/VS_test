from base import Session
from movie import Movie

for movie in Session().query(Movie).all():
    print movie.title

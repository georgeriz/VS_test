from base import Session, engine
from sqlalchemy import inspect

from sqlalchemy import MetaData, Table

inspector = inspect(engine)

for table in inspector.get_table_names():
    print table
    for column in inspector.get_columns(table):
        print '     ', column['name']

# in order to use ORM queries
meta = MetaData()

movies = Table("movies", meta)

# connect Table object with databse based on introspection
inspector.reflecttable(movies, None)

# example Query
session = Session(bind=engine)
print session.query(movies).count()
session.close()
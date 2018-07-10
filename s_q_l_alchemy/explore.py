from base import Session, engine
from sqlalchemy import inspect

inspector = inspect(engine)

for table in inspector.get_table_names():
    print table
    for column in inspector.get_columns(table):
        print '     ', column['name']
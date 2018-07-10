from base import Session, engine
from sqlalchemy import inspect

inspector = inspect(engine)

print inspector.get_table_names()

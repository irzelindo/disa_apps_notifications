from .paths import *
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.exc import DatabaseError

connection_url = URL.create(
    "mssql+pyodbc",
    username=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    host=SERVER,
    database=DATABASE,
    query={
        "driver": "ODBC Driver 11 for SQL Server",
    },
)

def setup():
    '''
        Connects to the database
        Returns:
        >>> connection
    '''
    try:
        engine = create_engine(connection_url)
    except DatabaseError as e:
        print(e)
        return None
    return engine

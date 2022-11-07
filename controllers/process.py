import psutil
import pandas as pd
import time
import pygetwindow as gw
from configs import db_setup
from sql_queries import get_processes
from urllib import request
from configs.paths import *

def database():
    """
    Connect to the database.
    Parameters: 
        None
    Returns: 
        Object: connection engine object
    """
    engine = db_setup.setup()
    return engine

def get_process(**kwargs):
    """
    Get the process from the database.
    Parameters: 
        None
    Returns: 
        Dataframe: df
    """
    query = get_processes.query
    
    for k, v in kwargs.items():
        if k == 'process_name':
            process_name = v
            query = get_processes.query_process_params(process_name)
        elif k == 'dates':
            start = v.start
            end = v.end
            query = get_processes.query_date_params(start, end,
                                                    parse_dates={
                                                        'Current_Date': {
                                                            'format': '%d-%m-%Y'
                                                        },
                                                        'Previous_Date': {
                                                            format: '%d-%m-%Y'
                                                    }})
    with database().connect() as connection:
        df = pd.read_sql(query, connection)
    return df


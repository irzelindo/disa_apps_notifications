import psutil
import pandas as pd
from configs import db_setup
from datetime import datetime


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


def check(process_name):
    """
    Check if there is any running process that contains the given name process_name.
    Parameters:
        String: process_name
    Returns:
        Boolean: True or False depending if the process is running
    """
    for process in psutil.process_iter():
        # print(process.name())
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(e)
    return False


def start(process_name):
    """
    Start the process if it's not running.
    Parameters: 
        String: process_name
    Returns: 
        String: "Process started" or "Process already running"
    """
    if check(process_name):
        return "Process already running"
    else:
        # Start the process
        psutil.Popen(process_name)
        return f"Process {process_name} started..."


def add_process(process_name, process_path, df):
    """
    Add current status to the dataframe.
    Parameters: 
        String: process_name
        String: process_path
    Returns: 
        String: "Process added"
    """
    data = {
        'Process': process_name,
        'Path': process_path,
        'Status': 'Running' if check(process_name) else 'Stopped',
        'Date': pd.Timestamp.now()
    }
    
    df = df.append(data, ignore_index=True)
    return df

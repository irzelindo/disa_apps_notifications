import psutil
import pandas as pd
import time
import pygetwindow as gw
from configs import db_setup


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


def start(process_name, process_path, df):
    """
    Start the process if it's not running.
    Parameters: 
        String: process_name
    Returns: 
        String: "Process started" or "Process already running"
    """
    if check(process_name):
        return
    else:
        # Start the process
        psutil.Popen(process_path)
        # Minimize the process window
        # print(process_name)
        # Wait for the window to open
        time.sleep(3)
        # Get the window object
        window = gw.getActiveWindow()
        # Minimize the window
        window.minimize()
        return update_process(process_name, process_path, df)

def update_process(process_name, process_path, df):
    """
    Update current status to the dataframe.
    Parameters: 
        String: process_name
        String: process_path
    Returns: 
        Dataframe: df with updated status
    """
    df.loc[df['Process'] == process_name, 'Current_State'] = 'Running' if check(
        process_name) else 'Stopped'
    df.loc[df['Process'] == process_name, 'Updated_At'] = pd.Timestamp.now()
    return df

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
        'Previous_State': 'Running' if check(process_name) else 'Stopped',
        'Date': pd.Timestamp.now(),
        'Current_State': None,
        'Updated_At': None,
    }
    
    df = df.append(data, ignore_index=True)
    return df

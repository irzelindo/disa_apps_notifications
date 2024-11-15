import time
import socket
import pygetwindow as gw
from configs import db_setup
from urllib import request

import pandas as pd
import psutil
import pygetwindow as gw

from configs import db_setup
from configs.paths import *

def socket_server():
    """
    Create a socket server.
    Parameters: 
        None
    Returns: 
        Object: socket server object
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST_NAME, int(HOST_PORT)))
    server.listen(5)
    return server

def internet_connectivity(host):
    """
    Check if there is internet connectivity.
    Parameters: 
        host: str
            The host to check the connectivity to.
    Returns:
        bool
            True if there is internet connectivity, False otherwise.
    """
    try:
        request.urlopen(host)
        return True
    except:
        return False


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
    # Start the process
    try:
        psutil.Popen(process_path, cwd=r"C:\Disalab")
    except Exception as e:
        df.loc[df['Process'] == process_name,
               'Previous_State'] = 'Process not found'
        df.loc[df['Process'] == process_name,
               'Current_State'] = 'Process not found'
        df.loc[df['Process'] == process_name,
               'Current_Date'] = pd.Timestamp.now()
        return df
        # print(e)
    # Minimize the process window
    # print(process_name)
    # Wait for the window to open
    time.sleep(3)
    # Get the window object
    window = gw.getActiveWindow()
    # Minimize the window
    # window.minimize()
    return update_process(process_name, df)


def update_process(process_name, df):
    """
    Update current status to the dataframe.
    Parameters: 
        String: process_name
    Returns: 
        Dataframe: df with updated status
    """
    df.loc[df['Process'] == process_name, 'Current_State'] = 'Running' if check(
        process_name) else 'Stopped'
    df.loc[df['Process'] == process_name, 'Current_Date'] = pd.Timestamp.now()
    return df


def add_process(process_name, df):
    """
    Add current status to the dataframe.
    Parameters: 
        String: process_name
    Returns: 
        String: "Process added"
    """
    # print(check(process_name))
    data = {
        'Lab_Code': LAB_PREFIX,
        'Lab_Name': LAB_NAME,
        'Process': process_name,
        'Previous_State': 'Running' if check(process_name) else 'Stopped',
        'Previous_Date': pd.Timestamp.now(),
        'Current_State': None,
        'Current_Date': None,
        'Internet_Connectivity': 'Connected' if internet_connectivity('https://www.google.com') else 'Disconnected',
        'Disa_Version': None
    }

    new_row = pd.DataFrame(data, index=[0])

    df = pd.concat([df, new_row], ignore_index=True)

    # df = df.append(data, ignore_index=True)
    return df


def insert_data(df):
    """
    Insert data to the database.
    Parameters: 
        Dataframe: df
    Returns: 
        None
    """
    with database().connect() as connection:
        # print(connection)
        # df.head()
        df.to_sql('State', connection, if_exists='append', index=False)

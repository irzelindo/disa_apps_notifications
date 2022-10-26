import os
from configparser import ConfigParser

cfg = ConfigParser()

BASE_PATH = os.path.join(os.path.dirname(os.path.abspath('')), 'openldr-epts')

CONFIG_PATH = os.path.join(BASE_PATH, 'configs\config.ini')

# print(CONFIG_PATH)

FILE_PATH = os.path.join(BASE_PATH, 'reports')

cfg.read(CONFIG_PATH)

# Default Configurations
PORT = cfg.get('default', 'port')
TLS = cfg.get('default', 'tls')
## Lab Configurations
LAB_NAME = cfg.get('default', 'lab_name')
LAB_PREFIX = cfg.get('default', 'lab_prefix')

# GMAIL Email configurations
GMAIL_HOST = cfg.get('smtp_gmail', 'server')
GMAIL_FROM_ADDR = cfg.get('smtp_gmail', 'from_addr')
GMAIL_EMAIL_USERNAME = cfg.get('smtp_gmail', 'username')
GMAIL_EMAIL_PASSWORD = cfg.get('smtp_gmail', 'password')

# OUTLOOK Email configurations
OUTLOOK_HOST = cfg.get('smtp_outlook', 'server')
OUTLOOK_FROM_ADDR = cfg.get('smtp_outlook', 'from_addr')
OUTLOOK_EMAIL_USERNAME = cfg.get('smtp_outlook', 'username')
OUTLOOK_EMAIL_PASSWORD = cfg.get('smtp_outlook', 'password')

# OUTLOOK DCL Email configurations
DCL_OUTLOOK_HOST = cfg.get('smtp_outlook_dcl', 'server')
DCL_OUTLOOK_FROM_ADDR = cfg.get('smtp_outlook_dcl', 'from_addr')
DCL_OUTLOOK_EMAIL_USERNAME = cfg.get('smtp_outlook_dcl', 'username')
DCL_OUTLOOK_EMAIL_PASSWORD = cfg.get('smtp_outlook_dcl', 'password')

# SQL Server Database Configurations
DATABASE = cfg.get('sql_server', 'database')
SERVER = cfg.get('sql_server', 'server')
DATABASE_USERNAME = cfg.get('sql_server', 'username')
DATABASE_PASSWORD = cfg.get('sql_server', 'password')



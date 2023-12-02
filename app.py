import pandas as pd

from configs.addresses import *
from configs.paths import *
from configs.processes import processes
from controllers.email import *
from controllers.process import *

pd.set_option('display.max_columns', None)

df = pd.DataFrame()

SUBJECT = f'{LAB_NAME} Processes Monitor'
TEXT = f'Hello,\n\nThis is an automated email to inform you about the running process:\n\n Regards,\n\n{LAB_NAME}'
EMAILS = EMAILS_ADDR
CC_EMAILS = EMAILS_CC_ADDR

# server = socket_server()

# conn, address = server.accept()

# print(f'Connection from {address} has been established!')

# while True:
#     msg = conn.recv(1024).decode('utf-8')
#     if msg == 'exit':
#         break
#     print(msg)
#     conn.send(bytes('I can listen to you!', 'utf-8'))
    
# conn.close()

for process in processes:
    if check(process['name']):
        df = add_process(process['name'], df)
        df = update_process(process['name'], df)
    else:
        df = add_process(process['name'], df)
        try:
            df = start(process['name'], process['path'], df)
        except Exception as e:
            df = update_process(process['name'], df)
# print(df.head(10))

if not df.empty:
    insert_data(df)
    # send_email(
    #     OUTLOOK_HOST,
    #     PORT,
    #     OUTLOOK_EMAIL_USERNAME,
    #     OUTLOOK_EMAIL_PASSWORD,
    #     SUBJECT,
    #     EMAILS,
    #     CC_EMAILS,
    #     TEXT,
    #     None,
    #     None,
    #     df
    # )
else:
    exit(1)

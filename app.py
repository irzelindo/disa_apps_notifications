import pandas as pd
from controllers.process import *
from controllers.email import *
from configs.processes import processes
from configs.paths import *
from configs.addresses import *

pd.set_option('display.max_columns', None)

df = get_process()

SUBJECT = f'{LAB_NAME} Processes Monitor'
TEXT = f'Hello,\n\nThis is an automated email to inform you about the running process:\n\n Regards,\n\n{LAB_NAME}'
EMAILS = EMAILS_ADDR
CC_EMAILS = EMAILS_CC_ADDR

if not df.empty:
    send_email(
        OUTLOOK_HOST,
        PORT,
        OUTLOOK_EMAIL_USERNAME,
        OUTLOOK_EMAIL_PASSWORD,
        SUBJECT,
        EMAILS,
        CC_EMAILS,
        TEXT,
        None,
        None,
        df
    )
else:
    exit(1)
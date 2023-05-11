import pandas as pd
from controllers.process import *
from controllers.email import *
from configs.paths import *
from configs.addresses import *

pd.set_option('display.max_columns', None)

df, total = get_process()

SUBJECT = f'{LAB_NAME} Processes Monitor'
TEXT = f'Hello,\n\nThis is an automated email to inform you about processes status on reference labs servers...'
EMAILS = EMAILS_ADDR
CC_EMAILS = EMAILS_CC_ADDR

# print(df.head(), total.head())

labs = total.iloc[0]['Total_Checked_Labs']

# print(labs)

if df.empty:
    exit(1)
else:
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
        df,
        labs
    )
    # print(df.head(), total.head())

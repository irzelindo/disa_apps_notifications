from redmail import EmailSender
from pathlib import Path


def send_email(host, port, username, password, subject, receivers, cc_emails, text, html, files, df):
    email = EmailSender(
        host=host,
        port=port,
        username=username,
        password=password
    )

    email.send(
        subject=subject,
        sender=username,
        receivers=map(lambda x: x.strip(), receivers),
        cc=map(lambda x: x.strip(), cc_emails),
        text=text,
        html='{{table}}',
        body_tables={
            'table': df
        },
        # attachments={
        #     file['name']: Path(file['path']) for file in files
        # }
    )

    print("Email sent successfully")

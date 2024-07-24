from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr

conf = ConnectionConfig(
    MAIL_USERNAME="sankar71711243@gmail.com",
    MAIL_PASSWORD="jwaihzcccwzctxko",
    MAIL_FROM="sankar71711243@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,   
    MAIL_SSL_TLS=False,   
    USE_CREDENTIALS=True
)

def send_registration_email(email_to: EmailStr, background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject="Welcome!",
        recipients=[email_to],
        body="You have successfully signed up!",
        subtype="plain"
    )
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)

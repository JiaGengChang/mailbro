from fastapi import HTTPException, status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType

# user modules
from models import Email
from variables import MAIL_USERNAME, MAIL_PASSWORD, MAIL_SERVER

conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_FROM=MAIL_USERNAME,
    MAIL_PORT=587,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)

async def send_email(payload: Email) -> None:
    message = MessageSchema(
        subject=payload.subject,
        recipients=payload.recipient_list,
        body=payload.body,
        subtype=MessageType.html
    )
    try:
        mail_client = FastMail(conf)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create email client. Error: " + str(e))
    
    try:
        await mail_client.send_message(message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Failed to send email to {payload.recipient_list}. Error: " + str(e))

def cleanup_recipient_list(recipient: str) -> list[str]:
    return [eml.strip() for eml in recipient.split(",") if "@" in eml]    

__all__ = [
    "cleanup_recipient_list",
    "send_email"
]
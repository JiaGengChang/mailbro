import sys
from typing_extensions import Annotated

from fastapi import FastAPI, HTTPException, Form, status, Request

# user modules
from security import verify_request
from mail import send_email, cleanup_recipient_list
from models import Email

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    await verify_request(request)
    return {"message": f"Hello! This server is running Python {version}."}


@app.post("/send")
async def send_custom_email(recipient: Annotated[str, Form()], subject: Annotated[str, Form()], body: Annotated[str, Form()], request:Request):
    await verify_request(request)
    recipient_list = cleanup_recipient_list(recipient)
    email = Email(
        recipient_list=recipient_list,
        subject=subject,
        body=body
    )
    await send_email(email)
    return {"message": f"Email sent to {recipient_list}."}


@app.post("/configure")
async def configure_email(recipient: Annotated[str, Form()], subject: Annotated[str, Form()], body: Annotated[str, Form()], request: Request):
    await verify_request(request)
    app.state.recipient_list = cleanup_recipient_list(recipient)
    app.state.subject = subject
    app.state.body = body
    return {"message": "Email configuration is set. Call /send_preconfigured to send the email."}


@app.post("/send_preconfigured")
async def send_email_endpoint(request:Request):
    await verify_request(request)
    if not hasattr(app.state, "recipient_list"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email configuration not set. Please call /configure first.")
    
    email = Email(
        recipient_list=app.state.recipient_list,
        subject=app.state.subject,
        body=app.state.body
    )
    await send_email(email)
    return {"message": f"Email sent to {app.state.recipient_list}."}

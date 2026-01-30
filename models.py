from typing import Union
from pydantic import BaseModel

class Email(BaseModel):
    recipient_list: Union[str, list[str]]
    subject: str | None = None
    body: str | None = None

__all__ = [
    "Email"
]
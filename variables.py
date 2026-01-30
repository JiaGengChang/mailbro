import os

MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
MAIL_SERVER=os.environ.get("MAIL_SERVER")

assert MAIL_USERNAME is not None, "MAIL_USERNAME environment variable is not set"
assert MAIL_PASSWORD is not None, "MAIL_PASSWORD environment variable is not set"
assert MAIL_SERVER is not None, "MAIL_SERVER environment variable is not set"

__all__ = [
    "MAIL_USERNAME",
    "MAIL_PASSWORD",
    "MAIL_SERVER",
]